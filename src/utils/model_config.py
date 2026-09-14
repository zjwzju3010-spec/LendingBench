"""Runtime model configuration helpers."""

from __future__ import annotations

import os
from typing import Any


DEFAULT_RUNTIME_OPENAI_MODEL = "qwen3.5-flash"
_ENABLE_THINKING_MODEL_PREFIXES = ("qwen",)

# 默认端点/密钥环境变量（沿用 legacy OPENAI_* 约定，供未映射的模型回退）。
_DEFAULT_API_KEY_ENV = "OPENAI_API_KEY"


def _normalize_model_name(value: Any) -> str:
    return str(value or "").strip()


def _supports_enable_thinking_toggle(model_name: Any) -> bool:
    """Return whether the model family accepts Qwen-style enable_thinking."""
    normalized = _normalize_model_name(model_name).lower()
    if not normalized:
        return False
    return normalized.startswith(_ENABLE_THINKING_MODEL_PREFIXES)


# 模型 → 端点/密钥/额外参数 注册表。
#
# 每个条目：
#   api_key_env   : 从中读取密钥的环境变量名（不直接写密钥，密钥在 .env）。
#   base_url      : 端点 URL（或 None 表示沿用 OPENAI_API_BASE_URL）。
#   extra_config  : 额外**请求级**参数（如 deepseek 的 reasoning_effort / extra_body），
#                   与 build_runtime_openai_chat_config 的结果合并，优先级更高。
#   client_kwargs : 额外**客户端构造级**参数（如 OpenAI(default_headers=...)），
#                   经 ModelFactory.create(**client_kwargs) 透传给 OpenAI(...)，
#                   **不能**并入 model_config_dict（否则会被当成请求参数报 TypeError）。
#
# 新增基线模型时在此登记一条即可；未登记的模型回退到 OPENAI_* 环境变量。
_MODEL_ENDPOINTS: dict[str, dict[str, Any]] = {
    "deepseek-flash": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url": "https://api.deepseek.com",
        "extra_config": {
            "reasoning_effort": "high",
            "extra_body": {"thinking": {"type": "enabled"}},
        },
    },
    "grok-4.6": {
        "api_key_env": "GETOKEN_API_KEY",
        "base_url": "https://api.getoken.tech/v1",
        # getoken 平台按 User-Agent 识别并拦截 OpenAI SDK 默认 UA（403），
        # 用无歧义的自定义 UA 覆盖（客户端级，走 client_kwargs 而非 extra_config）。
        "client_kwargs": {"default_headers": {"User-Agent": "getoken-client/1.0"}},
        # 2026-09-12：xAI 实测透传 reasoning_effort（none 会 400；low 使思考
        # 产出约 -35%、单案预计 -40% 时长）。基线列统一用 low，论文需注明。
        "extra_config": {"reasoning_effort": "low"},
    },
    # getoken 按模型类别独立授权：Gemini / Terra 各用专属 key（.env）。
    "gemini-3.8-flash": {
        "api_key_env": "GETOKEN_GEMINI_KEY",
        "base_url": "https://api.getoken.tech/v1",
        "client_kwargs": {"default_headers": {"User-Agent": "getoken-client/1.0"}},
    },
    "gpt-5.6-terra": {
        "api_key_env": "GETOKEN_TERRA_KEY",
        "base_url": "https://api.getoken.tech/v1",
        "client_kwargs": {"default_headers": {"User-Agent": "getoken-client/1.0"}},
    },
    # 2026-09-12：Terra 通道弃用，第四基线改用 DMXAPI 平台的 gpt-5.6-luna
    # （DMXAPI = OPENAI_* 环境变量端点，key 已在 .env，无需新登记密钥）。
    "gpt-5.6-luna": {
        "api_key_env": "OPENAI_API_KEY",
        "base_url": "https://www.dmxapi.cn/v1",
    },
    # 2026-09-12：第二篇规划实验统一口径——deepseek 改走 DMXAPI 官转通道。
    # 不带 reasoning_effort/thinking extra_config（chat/completions 对不支持
    # 的组合会 400，参照 luna 教训）；api.deepseek.com 的 deepseek-flash 原条目
    # 保留不动，第一篇基线批仍在使用。
    "deepseek-flash-guan": {
        "api_key_env": "OPENAI_API_KEY",
        "base_url": "https://www.dmxapi.cn/v1",
    },
}


def get_model_endpoint(model_name: Any) -> dict[str, Any]:
    """Return the (api_key_env, base_url, extra_config) for a model.

    Falls back to the legacy OPENAI_* environment variables when the model is
    not registered. ``extra_config`` defaults to an empty dict.
    """
    normalized = _normalize_model_name(model_name).lower()
    entry = _MODEL_ENDPOINTS.get(normalized)
    if entry is None:
        return {
            "api_key_env": _DEFAULT_API_KEY_ENV,
            "base_url": None,
            "extra_config": {},
            "client_kwargs": {},
        }
    return {
        "api_key_env": entry.get("api_key_env") or _DEFAULT_API_KEY_ENV,
        "base_url": entry.get("base_url"),
        "extra_config": dict(entry.get("extra_config") or {}),
        "client_kwargs": dict(entry.get("client_kwargs") or {}),
    }


def resolve_model_client_kwargs(model_name: Any) -> dict[str, Any]:
    """Return client-constructor kwargs for a model (e.g. default_headers).

    These must be passed to ``ModelFactory.create(**kwargs)`` so they reach the
    OpenAI client constructor, NOT merged into ``model_config_dict``.
    """
    return dict(get_model_endpoint(model_name)["client_kwargs"])


def resolve_openai_chat_model(
    explicit_model: Any = None,
    *,
    env_var: str = "OPENAI_MODEL_NAME",
    default_model: str = DEFAULT_RUNTIME_OPENAI_MODEL,
) -> str:
    """Resolve the runtime chat model with explicit override precedence.

    Order:
    1. explicit fallback passed by caller
    2. environment variable
    3. repository runtime default
    """
    explicit = _normalize_model_name(explicit_model)
    if explicit:
        return explicit

    env_model = _normalize_model_name(os.environ.get(env_var))
    if env_model:
        return env_model

    return _normalize_model_name(default_model) or DEFAULT_RUNTIME_OPENAI_MODEL


def build_runtime_openai_chat_config(
    *,
    model_name: Any = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> dict[str, Any]:
    """Build runtime chat config for OpenAI-compatible backends.

    Only inject provider-specific reasoning toggles for model families that
    are known to accept them. This avoids passing non-standard parameters
    like ``enable_thinking`` to models such as ``gpt-5-mini``.
    """
    config: dict[str, Any] = {}
    if temperature is not None:
        config["temperature"] = temperature
    if max_tokens is not None:
        config["max_tokens"] = max_tokens
    if _supports_enable_thinking_toggle(model_name):
        config["extra_body"] = {"enable_thinking": False}
    # 合并模型注册表中的额外请求参数（deepseek reasoning_effort/extra_body 等），
    # 其优先级高于默认 enable_thinking 注入。
    endpoint = get_model_endpoint(model_name)
    extra = endpoint["extra_config"]
    for key, value in extra.items():
        if key == "extra_body" and "extra_body" in config:
            merged = dict(config["extra_body"])
            merged.update(value)
            config["extra_body"] = merged
        else:
            config[key] = value
    return config


def resolve_model_credentials(model_name: Any) -> tuple[str | None, str | None]:
    """Return (api_key, base_url) for a model from the environment.

    ``api_key`` is read from the model's registered env var (falling back to
    OPENAI_API_KEY); ``base_url`` is the registered endpoint or None (falling
    back to OPENAI_API_BASE_URL in the camel backend).
    """
    endpoint = get_model_endpoint(model_name)
    api_key = os.environ.get(endpoint["api_key_env"]) or None
    base_url = endpoint["base_url"]
    return api_key, base_url


__all__ = [
    "DEFAULT_RUNTIME_OPENAI_MODEL",
    "resolve_openai_chat_model",
    "build_runtime_openai_chat_config",
    "get_model_endpoint",
    "resolve_model_credentials",
    "resolve_model_client_kwargs",
]