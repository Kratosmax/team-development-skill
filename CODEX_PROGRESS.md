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

## 当前快照（2026-11-06）

- 本阶段：将 team-development 整理为可分享的 GitHub 仓库；维护来源就是根目录 skill，无需编译或桌面安装包。
- 仓库目标：https://github.com/Kratosmax/team-development-skill ，公开，默认 main。
- 已核验发布基线：485f7245f19f43439cbb8e7d0898447694f5b8ba（首次发布）。这是校准基线，后续进度文档提交会继续推进 HEAD。
- 本地：9 个交付文件已完成，安装说明、变更记录、MIT 许可、维护与接续规则和校验脚本均已纳入 Git。
- 线上：2026-11-06 已通过 gh repo view 确认 PUBLIC/main；首次推送后 git ls-remote 与本地发布基线一致，GitHub contents API 的 SKILL.md blob SHA 与本地 git hash-object 一致。公开 HTTPS 克隆与快进更新已成功，克隆中的校验通过。后续接手仍须重新核对实时状态。

## 当前待办

本阶段建仓、首推、安装验证已完成。当前仅需按阶段收尾协议同步本次核验记录，随后等待新的用户需求；没有其他已授权未完成的功能任务。

## 关键入口

- [SKILL.md](SKILL.md)：运行时能力探测、角色、多级并行、隔离升级、验收。
- [模型路由](references/model-routing.md)：偏好基线、实际接口与新版核验；模型版本不是软件包版本。
- [AGENTS.md](AGENTS.md)：阶段完成后的自动提交推送约定及其仓库范围。
- [验证脚本](scripts/validate.py)：Python 3.10+ 标准库，无第三方依赖。
- [变更记录](CHANGELOG.md)：记录每个已交付阶段。

## 兼容与边界

必须保留多级多名并行、升级新上下文、实际模型证据、唯一写入负责人及独立验收。生图服务按可用接口选择，不假装能按次切换模型。第三方无需安装作者其他私有或个人 skill。

维护 agent 已获阶段完成且验证通过后自动提交推送此仓库的授权，具体范围见 AGENTS.md；不扩大到业务项目、fork 用户、标签、Release 或全局配置。账号凭据和机器路径不进入仓库。

## 验证记录

- 2026-11-06：python scripts/validate.py 通过（元数据、UTF-8、必需文件、设备路径与本地引用）。
- 2026-11-06：在隔离临时副本中验证 BOM、缺失链接、越界链接和错误 skill 名称均被拒绝，真实安装文件未被测试修改。
- 2026-11-06：独立只读审查维护授权边界、并行及隔离规则，结论可交付。
- 2026-11-06：公开仓库 HTTPS git clone、git pull --ff-only 和克隆副本校验通过；本地 git diff --check、首提交 git diff --cached --check 均通过。
- 未配置 CI；PowerShell/Windows 环境验证了 Git 安装与更新流程，Linux/macOS 原生环境未运行。
- 最低命令：python scripts/validate.py；git diff --check；提交前 git diff --cached --check。
- 本项目是 Markdown skill，不提供也不需要应用构建、Full/Lite 包、后台服务或安装器；无需执行桌面应用发行流程。

## 收尾维护

每个阶段更新本文件、必要的 README 与 CHANGELOG，再按 AGENTS.md 提交、推送及独立核验。提交只记某次已核验基线；不要自指“永远是当前 HEAD”。维护记录中的“已完成”仅指上述已核验基线；后续提交与推送结果以实时 Git 证据为准。没有新授权任务时等待用户需求。
