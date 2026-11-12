# AI 继续维护入口

此文件是接续索引，易变状态须通过 Git、文件和实际验证重新校准，不替代实时证据。

## 接手校准

先读 [维护规则](AGENTS.md)、[使用说明](README.md)、[Skill](SKILL.md) 和相关 references，再执行：


```sh
git status --short
git branch --show-current
git remote -v
git log -5 --oneline
python scripts/validate.py
git diff --check
```

## 当前快照（2026-11-12）

- 本阶段：补充成员有界预算、兼容任务优先复用和可验证的结束/清理规则。维护来源仍是根目录 skill。
- 仓库目标：https://github.com/Kratosmax/team-development-skill ，公开，默认 main。
- 本阶段起点：c961118a17620fca9b5151a56e53b59fc230b898；接手时 main 工作区干净，远程 origin 指向上述仓库。该提交是校准基线，当前 HEAD 与推送状态仍须读取 Git。
- 本地：新增 [成员生命周期](references/agent-lifecycle.md)，同步核心规则、路由、派工记录与用户说明；没有修改客户端、删除会话文件或伪装物理资源已释放。
- 线上：2026-11-06 已通过 gh repo view 确认 PUBLIC/main；首次推送后 git ls-remote 与当时的首次发布提交 485f724 一致，GitHub contents API 的 SKILL.md blob SHA 与本地 git hash-object 一致。公开 HTTPS 克隆与快进更新已成功，克隆中的校验通过。后续接手仍须重新核对实时状态。

## 当前待办

本阶段规则修订、独立审核与文件校验已完成，随阶段提交同步；没有后续功能待办。当前提交/远程状态需用接手命令实时校准。当前仅能在工具暴露能力内减少新建并管理停止/退出；历史卡片清理与平台内存回收没有已注册接口，不宣称完成。

## 关键入口

- [SKILL.md](SKILL.md)：运行时能力探测、角色、多级并行、隔离升级、验收。
- [模型路由](references/model-routing.md)：偏好基线、实际接口与新版核验；模型版本不是软件包版本。
- [派工记录](references/dispatch-reporting.md)：分级、显式选型、启动 ID 与执行型号证据的对话呈现。
- [AGENTS.md](AGENTS.md)：阶段完成后的自动提交推送约定及其仓库范围。
- [验证脚本](scripts/validate.py)：Python 3.10+ 标准库，无第三方依赖。
- [变更记录](CHANGELOG.md)：记录每个已交付阶段。

## 兼容与边界

必须保留多级多名并行、升级新上下文、实际模型证据、唯一写入负责人及独立验收。生图服务按可用接口选择，不假装能按次切换模型。第三方无需安装作者其他私有或个人 skill。

维护 agent 已获阶段完成且验证通过后自动提交推送此仓库的授权，具体范围见 AGENTS.md；不扩大到业务项目、fork 用户、标签、Release 或全局配置。账号凭据和机器路径不进入仓库。

## 验证记录

- 2026-11-12：开始及审核结束后的 list_agents 均仅返回 Leader，没有可寻址的复用目标；该查询不证明所有历史普通子代理终态。当前接口支持通信和中断，未暴露成员删除/关闭/归档；本次不执行伪清理。
- 2026-11-12：本阶段仅新增 1 名独立高级审核者，显式请求 magpie-responses / yzcodex/gpt-6.1-sol / high；创建回执无执行型号，实际型号未独立核实。审核结果已回收并收到运行时完成通知，未启动子代理或后台任务，结束后不再派工。就本阶段跟踪范围：运行 0、保留待命 0、新建 1、续派 0；平台历史保留/物理释放状态不可观测。
- 2026-11-12：八类生命周期场景的独立规则推演通过（非平台删除/内存回收实测）。python scripts/validate.py、git diff --check 与 git diff --cached --check 通过；新生命周期参考文件已显式纳入阶段提交。

- 2026-11-11：当前正式列表仍提供 GPT-6.1 Sol、GLM-5.3、GLM-5.3-Flash；本次文档委派显式请求 GLM-5.3/high，创建回执只返回代理 ID，未独立确认执行型号。独立审核用全新 GPT Sol/high 请求并已返回结果；两次创建回执均仅含代理 ID，执行型号未独立核实，不能让代理自报身份充当证据。
- 2026-11-11：核心独立只读审核通过，覆盖漏传参数、ID 无型号、不可选但有元数据、路由不一致、升级替换、批量并行和 GUI 不显示七种规则推演；不是实际运行七批代理的测试。Leader 已复核并行文档及整体差异。
- 2026-11-11：新增规则、示例和文档后 python scripts/validate.py、git diff --check 通过；提交前仍需执行暂存区检查，远程提交通过 Git 独立核对。不以文本规则保证未来 agent 绝不会漏执行。

- 2026-11-06：python scripts/validate.py 通过（元数据、UTF-8、必需文件、设备路径与本地引用）。
- 2026-11-06：在隔离临时副本中验证 BOM、缺失链接、越界链接和错误 skill 名称均被拒绝，真实安装文件未被测试修改。
- 2026-11-06：独立只读审查维护授权边界、并行及隔离规则，结论可交付。
- 2026-11-06：公开仓库 HTTPS git clone、git pull --ff-only 和克隆副本校验通过；本地 git diff --check、首提交 git diff --cached --check 均通过。
- 未配置 CI；PowerShell/Windows 环境验证了 Git 安装与更新流程，Linux/macOS 原生环境未运行。
- 最低命令：python scripts/validate.py；git diff --check；提交前 git diff --cached --check。
- 本项目是 Markdown skill，不提供也不需要应用构建、Full/Lite 包、后台服务或安装器；无需执行桌面应用发行流程。

## 收尾维护

每个阶段更新本文件、必要的 README 与 CHANGELOG，再按 AGENTS.md 提交、推送及独立核验。提交只记某次已核验基线；不要自指“永远是当前 HEAD”。维护记录中的“已完成”仅指上述已核验基线；后续提交与推送结果以实时 Git 证据为准。没有新授权任务时等待用户需求。
