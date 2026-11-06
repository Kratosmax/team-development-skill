# team-development

团队开发与多智能体协作 skill。当所处 agent 环境支持子代理或团队委派时，按任务需要组织设计、审美、多级编程、代码审核和用户视角质疑，依据当前实际可用的模型进行路由、降级与升级，协调共享文件并独立验收；环境不支持时简短告知并继续原任务。

这是一个以 Markdown 指令与参考文档为主体的 skill，附带可选的 Python 校验脚本。不需要编译或运行服务，克隆后即可被支持本地 skill 目录的 agent 客户端加载。

- 仓库：<https://github.com/Kratosmax/team-development-skill>（默认分支 `main`，仓库根目录即 skill 内容）
- 许可证：MIT（见 [LICENSE](LICENSE)）
- 变更记录：[CHANGELOG.md](CHANGELOG.md)

## 核心能力

- **按功能多名、多级并行。** Leader 按功能或工作包分配独立代理：同一级别可按功能同时存在多名代理，初级、中级、高级编程代理可并行负责不同功能（例如初级做展示组件、中级做数据查询、高级做并发与状态一致性），不把整个项目锁在单一档位。互不依赖的任务在同一轮批量启动，只对真正有依赖或共享写入冲突的局部步骤排序。
- **升级即全新独立上下文。** 任务从低档升级时，新建目标级别代理的独立上下文，不在原低级对话里改名、换模型或继续累积试错记录；交接用户原始需求、已确认约束、接口、当前基线与差异、可复现的失败证据，不默认继承旧对话的试错链与未证实结论。真实模型没变就不宣称已完成模型升级。
- **设计、审美、审核、用户质疑。** 设计智能体给出可实施方案；审美智能体必须查看真实界面截图或运行结果再评估视觉质量；代码审核智能体对照原始需求审核最终差异；抬杠智能体从真实用户场景提出反例、可用性障碍与替代建议。重要变更由未参与该项实现的代理独立审查，作者自检不计为独立审查。
- **能力不支持时短提示后继续。** 当前环境没有任何委派能力时，只提示一次“当前环境不支持团队协作，无法使用 team-development；已跳过，继续按普通方式处理原任务”，随后退出团队流程继续原任务：不要求用户安装或切换环境，也不用一个代理扮演多个角色冒充团队。

从能力检查、组队、模型路由、拆分与并行委派，到审查质疑、验收与汇报的完整流程见 [SKILL.md](SKILL.md)。

## 关于模型：偏好基线，不是保证

- [references/model-routing.md](references/model-routing.md) 中的模型（如 GPT-6.1 Sol、GLM-5.3、GLM-5.3-Flash、gpt-image-2.6-flare）是**偏好基线**，只表达各职责的优先顺序，不是“已安装”“官方最新”或“当前环境可用”的保证。每次使用以当前工具实际返回、可调用的 provider/model 为准；首选不可用时按文档规则降级到真实可用的替代并如实披露，不用文本模型冒充生图模型。
- 文中“当前 DSH 路由示例”里的 provider/model ID 是 **2026-11-06 在某一特定 DSH 环境实测的示例**，仅供该环境的映射参考；换环境或新会话应重新发现可用模型，不要盲用历史 ID。
- **生图**：Magpie 的图像生成工具使用 Magpie 设置中配置的图像模型；当前未核实它能按次指定型号，因此本 skill 不把 gpt-image 系列冒称为“可选生图型号”。偏好名 gpt-image-2.6-flare 属待核实偏好；无法确认配置与回执的型号时，会如实说明“使用 Magpie 当前配置的生图模型，指定 GPT image 型号尚未核实”，不虚假宣称。

## 安装

前置条件：

- 已安装 `git`；
- 一个支持从本地目录加载 skill 的 agent 客户端；
- 可选：Python 3.10+，仅用于运行仓库自带的可选自检脚本 `scripts/validate.py`。

本 skill 独立可用，**不依赖** `agent-rules`、`desktop-tool-ui-release` 或其他任何 skill 才能安装或使用；它们只是协作中可按需配合的可选项（例如环境与权限问题可参考 agent-rules），不是前置条件。

安装到用户级公共目录 `~/.agents/skills/team-development`。**目标目录已存在时不要覆盖**：请先自行备份原目录，或另选其他路径。

PowerShell（Windows）：

```powershell
$dest = "$HOME\.agents\skills\team-development"
if (Test-Path $dest) {
    Write-Output "目标已存在：$dest —— 请先自行备份该目录，或另选其他路径安装。"
} else {
    git clone https://github.com/Kratosmax/team-development-skill.git $dest
}
```

bash（Linux / macOS）：

```bash
dest="$HOME/.agents/skills/team-development"
if [ -e "$dest" ]; then
    echo "目标已存在：$dest —— 请先自行备份该目录，或另选其他路径安装。"
else
    git clone https://github.com/Kratosmax/team-development-skill.git "$dest"
fi
```

> **通用客户端**：不同 agent 客户端的 skill 目录约定不同。如果你的客户端不使用 `~/.agents/skills`，请以其文档支持的 skill 目录为准，把仓库克隆（或复制仓库全部内容）到该目录下名为 `team-development` 的子目录——仓库根目录就是 skill 内容，不要再套一层目录。

## 更新

在安装目录执行快进更新：

```powershell
cd "$HOME\.agents\skills\team-development"
git pull --ff-only
```

```bash
cd "$HOME/.agents/skills/team-development" && git pull --ff-only
```

`--ff-only` 只接受快进更新；如果你在安装目录做过本地提交导致无法快进，命令会失败并提示，此时请先自行处理本地改动（备份、暂存或另选路径重装），不要改写上游分支。

## 使用

安装后，skill 会出现在支持客户端的 skill 列表中（必要时重启会话或按客户端的方式刷新）。调用示例：

> 使用 team-development 并行完成这三个互不依赖的模块实现，并安排代码审核。
>
> 使用 team-development 为这次界面改版组织设计、审美评审和用户视角质疑。
>
> 使用 team-development 处理；如果当前环境不支持团队协作，就直接按普通方式继续。

具体触发方式取决于客户端：有的按任务描述自动匹配，有的需要像上面一样显式点名。skill 加载后，agent 按 [SKILL.md](SKILL.md) 的流程执行。

## 本地自检（可选）

本 skill 是纯 Markdown，无需编译或运行服务。仓库提供可选的自检脚本，在安装目录运行：

```bash
python scripts/validate.py
```

需要 Python 3.10+；不运行该脚本不影响 skill 的安装与使用。

## 仓库结构与 AI 接续

```text
team-development-skill/        # 仓库根目录 = skill 内容
├── SKILL.md                   # skill 主体指令
├── references/
│   └── model-routing.md       # 模型偏好基线与运行时路由
├── scripts/
│   └── validate.py            # 可选本地自检脚本（Python 3.10+）
├── AGENTS.md                  # AI 接续入口：面向维护代理的仓库说明
├── CODEX_PROGRESS.md          # AI 接续入口：阶段进度与交接记录
├── README.md                  # 本文件
├── CHANGELOG.md               # 变更记录
└── LICENSE                    # MIT
```

`AGENTS.md` 与 `CODEX_PROGRESS.md` 供 AI 维护代理在新的会话或工具中接续开发和交接进度时快速恢复上下文。

## 维护与边界

- 阶段完成的自动推送由**已获授权的维护 agent** 执行，且仅作用于本 skill 仓库（Kratosmax/team-development-skill）。
- 本 skill **不安装常驻 watcher 或后台服务**，也不会自动推送使用者的业务项目。
- 第三方安装本 skill 不会获得、也不会被授予向原作者仓库推送的权限；你的克隆只使用你自己的凭据与远端。
- 本仓库当前未配置 CI；文档中的命令由维护者在本地环境验证。
