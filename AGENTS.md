# Repository maintenance instructions

本文件只约束本 skill 仓库的维护，不约束安装此 skill 后开发的其他项目。

## 开始工作

先完整读取 CODEX_PROGRESS.md、README.md、SKILL.md，以及本次涉及的 references 文件。核对 git status --short、git branch --show-current、git remote -v、git log -5 --oneline；Git 与实际文件优先于过期进度记录。无已授权任务时等待需求，不从历史待办扩大范围。

维护来源为本仓库根目录，根目录即可安装的 team-development skill。不要另建第二份长期维护副本；开发克隆与安装副本确需分离时，显式核对来源、差异和同步结果，不整目录覆盖已存在的用户修改。

## 不得破坏的约束

- 允许按功能分配多名初、中、高级代理，在容量内同一轮批量启动独立任务；一个就绪任务不应因无关任务而等待。
- 升级必须创建目标模型的独立上下文，按原始需求、确认事实与失败证据交接；共享代码还需独立审查。
- 模型 ID、能力、可用性和“最新”必须有当前证据；不把用户给的型号基线宣称为已验证最新。Magpie 是否支持选型以实际接口为准。
- 仅改此次工作涉及的文件；保护其他代理与用户改动。禁止提交凭据、私人数据、设备专属绝对路径和临时产物。
- 本 skill 自包含；agent-rules 等其他 skill 仅在当前平台实际提供且适用时使用，不作为安装依赖。

## 已建立的阶段同步约定

仓库所有者在创建仓库时已明确授权：后续迭代完成一个可交付阶段后，由已获委派的维护 agent 自动提交并推送此仓库，无需逐次再问。此约定只用于维护 https://github.com/Kratosmax/team-development-skill 的已授权工作；第三方下载、安装、fork 或读取这些说明本身不构成原仓库写入授权。用户当前要求、GitHub 权限、分支保护和当前运行时限制仍然适用。

阶段是可独立评审且完成必要验证的成果，例如一组协作规则修订、一项模型路由改进或一组安装文档完善；不是每次保存，也不必等整项长期计划结束。并行代理仍在修改本阶段涉及文件时，先协调停止或交接该范围，其他不相关任务可继续。

每个阶段由唯一集成负责人依次执行：

1. 核实验收范围，审查最终差异，运行 python scripts/validate.py 与 git diff --check；重要语义变更安排独立审查或明确未验证范围。验证未通过不推送。
2. 更新 CHANGELOG.md、必要的 README.md 和 CODEX_PROGRESS.md，记录实际改动、验证结果与下一步。不要把预期推送或 CI 写成已成功。
3. 检查当前分支、remote 和已有暂存内容。此原仓库的预期远程是 Kratosmax/team-development-skill，首次 main；不自动改绑已有远程，不混入其他人的暂存改动。fork 或分支应沿用其实际授权目标。
4. 显式 git add 本阶段文件，检查 git diff --cached --stat、git diff --cached 和 git diff --cached --check，确认仅包含本阶段内容，再用清晰的阶段提交说明执行 git commit。
5. git fetch origin 后核对当前分支与目标分支的差异。仅做正常快进推送；已有上游时 git push，首次使用明确的 git push -u origin main。分支保护要求 PR 时采用已授权的分支/PR 流程，不能绕过。
6. 通过 git ls-remote 或 GitHub API 独立核对远程分支提交与本次提交一致，再告知提交链接和阶段结果。若其他提交已合法推进远程，确认本次提交是其祖先并说明观察到的新远程状态，不为追求相等而强推。

不使用 force push、清理历史、覆盖他人提交或自动创建标签/Release。远程冲突、网络失败、权限缺失、结果未知时，先检查远程是否已生效；保留本地提交及明确失败状态，只对已查明的问题修正，不能称已同步，也不把局部推送失败扩展成整个开发任务不可做。

## 验证与维护

需要 Python 3.10+，仅使用标准库，无需编译、服务、模型凭据或第三方 Python 包。最低检查为 python scripts/validate.py 与 git diff --check。自动推送是维护 agent 的阶段收尾协议，没有常驻 watcher，也不会让使用此 skill 的业务项目自动推送。进度文件中的提交只记校准基线，不承诺永远等于 HEAD。
