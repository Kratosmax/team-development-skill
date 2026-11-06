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
- 提交基线：仓库初始化阶段，尚无首个提交；以接手时 git log 与 remote 校准。
- 本地：已加入维护规则、MIT 许可、标准库验证脚本；安装文档和变更记录正在整理。
- 线上：尚未完成创建、首次推送与独立核验，不能依据此文件声称已同步。

## 当前待办

1. 完成本地文档与必要验证。
2. 创建目标仓库、提交并推送，核对 GitHub 分支提交。
3. 回填真实验证与线上核验记录；完成后等待新的用户需求。

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

- 2026-11-06：当前阶段验证待执行，不沿用建仓前的历史检查作为本轮通过。
- 最低命令：python scripts/validate.py；git diff --check；提交前 git diff --cached --check。
- 本项目是 Markdown skill，不提供也不需要应用构建、Full/Lite 包、后台服务或安装器；无需执行桌面应用发行流程。

## 收尾维护

每个阶段更新本文件、必要的 README 与 CHANGELOG，再按 AGENTS.md 提交、推送及独立核验。提交只记某次已核验基线；不要自指“永远是当前 HEAD”。首次发布完成后删除过期初始待办；没有新授权任务时等待用户需求。
