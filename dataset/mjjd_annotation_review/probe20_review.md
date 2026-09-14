# 20 探针种子人工复核表（v2，已修非目标门清零）

> 检查项：目标路线门 label=1、非目标门 label=0、gt_terminal、judgment_text 清空、注入背景行。

> 已知上游原文措辞：case 91916【新增事实】含「原告原告樊善学」（六枝 B2 枝 added_world_fact 原文如此，非转换 bug，忠实提取保留）。

## withdraw_ci (case 902)

- 基底 original_id=902  gt_terminal=first_withdrawal  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=1 ◀目标
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方当事人指令】原告金南山明确指令：与被告私下达成还款安排后，必须撤回起诉，不继续开庭。

## withdraw_ci (case 1102)

- 基底 original_id=1102  gt_terminal=first_withdrawal  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=1 ◀目标
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方当事人指令】原告王雷明确指令：与被告私下达成还款安排后，必须撤回起诉，不继续开庭。

## withdraw_ci (case 3502)

- 基底 original_id=3502  gt_terminal=first_withdrawal  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=1 ◀目标
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方当事人指令】原告缑正军明确指令：与被告私下达成还款安排后，必须撤回起诉，不继续开庭。

## withdraw_ci (case 4702)

- 基底 original_id=4702  gt_terminal=first_withdrawal  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=1 ◀目标
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方当事人指令】原告李树盛明确指令：与被告私下达成还款安排后，必须撤回起诉，不继续开庭。

## withdraw_ci (case 6902)

- 基底 original_id=6902  gt_terminal=first_withdrawal  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=1 ◀目标
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方当事人指令】原告李江娈明确指令：与被告私下达成还款安排后，必须撤回起诉，不继续开庭。

## mediation_ci (case 101)

- 基底 original_id=101  gt_terminal=first_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方底线】本金按实际出借额（考虑预扣或已还后的余额）必须拿回；利息可让至年利率保护上限以内；不追加案外人。
  【被告方底线】同意还实际出借本金；利息不超过保护上限；可分期。

## mediation_ci (case 401)

- 基底 original_id=401  gt_terminal=first_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方底线】本金按实际出借额（考虑预扣或已还后的余额）必须拿回；利息可让至年利率保护上限以内；保证人可保留。
  【被告方底线】同意还实际出借本金；利息不超过保护上限；可分期。

## mediation_ci (case 1201)

- 基底 original_id=1201  gt_terminal=first_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方底线】本金按实际出借额（考虑预扣或已还后的余额）必须拿回；利息可让至年利率保护上限以内；不追加案外人。
  【被告方底线】同意还实际出借本金；利息不超过保护上限；可分期。

## mediation_ci (case 2101)

- 基底 original_id=2101  gt_terminal=first_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方底线】本金按实际出借额（考虑预扣或已还后的余额）必须拿回；利息可让至年利率保护上限以内；不追加案外人。
  【被告方底线】同意还实际出借本金；利息不超过保护上限；可分期。

## mediation_ci (case 2201)

- 基底 original_id=2201  gt_terminal=first_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: (空)
- 注入背景行:
  【原告方底线】本金按实际出借额（考虑预扣或已还后的余额）必须拿回；利息可让至年利率保护上限以内；不追加案外人。
  【被告方底线】同意还实际出借本金；利息不超过保护上限；可分期。

## gold_task_non_acceptance (case 25914)

- 基底 original_id=25914  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】原告向与被告住所地、合同履行地均无管辖连接点的法院递交起诉状（不是乌兰县人民法院）。

## gold_task_reject_complaint (case 36916)

- 基底 original_id=36916  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】立案后查明：起诉状所列原告孙世英并非债权人，仅是资金转账经办人，债权人为案外人且未授权。

## gold_task_reject_complaint (case 58916)

- 基底 original_id=58916  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】立案后查明：起诉状所列原告程学群并非债权人，仅是资金转账经办人，债权人为案外人且未授权。

## gold_task_reject_complaint (case 70916)

- 基底 original_id=70916  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】立案后查明：起诉状所列原告赵富田并非债权人，仅是资金转账经办人，债权人为案外人且未授权。

## gold_task_reject_complaint (case 76916)

- 基底 original_id=76916  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】立案后查明：起诉状所列原告刘晋舟并非债权人，仅是资金转账经办人，债权人为案外人且未授权。

## gold_task_reject_complaint (case 91916)

- 基底 original_id=91916  gt_terminal=first_procedural  胜败=lose/win
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: (空)
- judgment_text_second: (空)
- 注入背景行:
  【新增事实】立案后查明：起诉状所列原告原告樊善学并非债权人，仅是资金转账经办人，债权人为案外人且未授权。

## mediation_cia (case 2103)

- 基底 original_id=2103  gt_terminal=second_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: 非空（CIA 探针，二审终局需历史一审判决）

## withdraw_appeal (case 2204)

- 基底 original_id=2204  gt_terminal=second_withdraw_appeal  胜败=win/lose
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=1 ◀目标, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: 非空（CIA 探针，二审终局需历史一审判决）

## mediation_cia (case 2303)

- 基底 original_id=2303  gt_terminal=second_mediation  胜败=draw/draw
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=1 ◀目标, withdraw_appeal=0, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: 非空（CIA 探针，二审终局需历史一审判决）

## withdraw_appeal (case 2404)

- 基底 original_id=2404  gt_terminal=second_withdraw_appeal  胜败=win/lose
- 门标签: preservation_pre=0, counterclaim=0, preservation_mid=0, mediation=0, withdraw_appeal=1 ◀目标, withdraw_lawsuit=0
- judgment_text_first: 非空（仅 AD/AR 可见，CI 探针无影响）
- judgment_text_second: 非空（CIA 探针，二审终局需历史一审判决）

## 核对结论（人工填写）
- [ ] 20 条全部与上述检查项一致？不一致请报 case_id + 字段。
