# Obsidian 个人知识库 Skill

`obsidian-agent-vault` · v1.1.0

这个 Skill 在电脑上建好视频里的九个一级目录、首页看板、Agent 规则、导航、两份记录模板和一份常用口令。之后在任何能读写本地文件的 Agent 里，都可以用同一个库继续整理资料、记录决定和回填复盘。库根目录的 `AGENTS.md` 是规则入口，`CLAUDE.md` 指向同一份规则。

## 第一次使用

1. 下载 [Skill ZIP](https://github.com/cxcxy/obsidian-agent-vault/releases/download/v1.1.0/obsidian-agent-vault-v1.1.0.zip) 并解压。保留完整的 `obsidian-agent-vault/` 文件夹。
2. **Codex** 把整个文件夹放进用户的 `~/.agents/skills/`，在新会话中选 `$obsidian-agent-vault`。 [Codex 本地 Skill 路径](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)
3. **WorkBuddy** 把整个解压文件夹放进用户的 `~/.workbuddy/skills/`，新任务里输入 `/` 搜索 `obsidian-agent-vault`。也可以按客户端的「技能 → 添加技能 → 上传技能」导入本地技能包。 [WorkBuddy 导入技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
4. **其他 Agent** 支持 Skill 的，把整个文件夹放进它读取技能的目录。不支持的，让它在解压后的 `obsidian-agent-vault/` 里运行 `python3 scripts/init_vault.py --vault "目标目录"`（Windows 用 `py -3`），结果相同。
5. 给 Agent 发一句「用 obsidian-agent-vault 帮我搭一个 Obsidian 个人知识库，放在我的文稿目录」。想放到其他位置就给出路径。
6. 在 Obsidian 的仓库管理里选「打开本地仓库」，选择 Agent 返回的目录，然后打开 `首页看板.base`。 [管理仓库](https://obsidian.md/help/manage-vaults) · [Bases](https://obsidian.md/help/bases)

初始化可以重复运行，已有笔记和配置会保留。当目标目录本来就有 Obsidian 设置时，可以从「文件与链接」手动选择收件箱和附件目录。网页剪藏可从官方 Web Clipper 导入库内 `90-系统底座/视图/Web-Clipper-收件箱.json`。 [导入 Web Clipper 模板](https://obsidian.md/help/web-clipper/templates)

## 搭好以后可以这样说

下面几句常用的话，库里的 `90-系统底座/常用口令.md` 都有，复制就能用。

> 把我们刚才确认的决定、原因和待验证的事项，写进这个知识库。给我新笔记的路径。

> 先看看收件箱，列出每篇资料建议放哪、为什么、是否有重复。等我确认清单后再移动。

> 找出「待复查」里的决定和各自原文。把我刚提供的实际结果，补回对应那一条。

> 只读检查整个库，看看有没有失效链接、互相冲突的版本，导航是否太长需要瘦身。不要改文件，列一份清单给我。

整理收件箱时先确认预览，再让 Agent 只执行清单里确认的动作。每周有空翻一次「待复查」，有了新结果就写回原来的记录。

## 长期维护

- **每天十秒**。网页用 Web Clipper 存进收件箱；想法在 Obsidian 按 `Cmd + N`（Windows 是 `Ctrl + N`），写完就关，先不分类。
- **每周两分钟**。攒到五到十篇，用常用口令里的那句话让 Agent 给归档预览清单，看完回「确认执行」。收件箱积压太多时，可以让它把一个月前的笔记整批移进已归档。
- **按事件**。项目做完，把能复用的经验提炼成卡片放进专业沉淀，原项目移进已归档；决定有了结果，就补回原来那条记录。
- **每月一次**。让 Agent 做只读体检，只出清单，不改文件。

两条底线：批量整理只交给一个主力 Agent，不要同时开两个 Agent 改文件；大整理前留恢复点。库是 Git 仓库就先提交一次（自带的 `.gitignore` 已忽略系统文件和窗口布局缓存）；不用 Git 就先复制整个库文件夹。密码、证件号、银行卡号这类内容不要放进库。

## 从 v1.0.0 升级

换上新的 Skill 文件夹后，对已有的库再跑一次初始化，会补上 `常用口令.md` 和 `.gitignore`，不会覆盖你的笔记。库里原来的 `AGENTS.md` 也会保留，所以新规则不会自动写进去。可以让 Agent 对照新版 Skill 里的 `assets/vault/AGENTS.md`，把新增的四条规则合并进你的规则文件。

## 本机验收

Codex 和 WorkBuddy 均已实际调用 Skill 建库，并各自把测试会话里的决定写成了库内 Markdown。Obsidian 中已打开生成的首页看板，验证待复查筛选、新建笔记位置和决策模板。WorkBuddy 的验证使用解压后的本地目录，Web Clipper 模板完成格式检查。

v1.1.0 新增的常用口令、规则和 `.gitignore` 已经验证过：在干净目录建库、重复运行、为 v1.0.0 的旧库补缺失文件、遇到同名冲突时停止，`.gitignore` 也能正常生效。新规则还没有让 Agent 跑一轮真实的维护任务来检验。
