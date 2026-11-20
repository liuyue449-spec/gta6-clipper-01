# gta6-clipper-01 — HANDOFF（参赛准备已完成，待主人发布视频后提交）

> 状态：片子已剪好、仓库已建好并公开、本地检查通过（只差 transcripts bundle，那是提交时才打的）。
> 绝不要在主人发回视频链接之前提交；绝不要往任何 YouTube 账号发视频。

## 比赛
- make.fun `gta6-clipper-01`「Clip GTA 6 for the most YouTube views」：剪一条 GTA 6 短片发到 YouTube，按播放量排名，$500，前 20 名分钱（第 1 名 $100）。
- 报名截止：2026-11-23 09:00 CST（2026-11-23T01:00:00Z）；结果 2026-12-07 前出。
- 账号：make.fun @liuyue449-spec，GitHub liuyue449-spec（已绑定），payout 钱包 `HujuZseZ1nhhJq9Mf2B1GwBRv892KU32oPpMG663BEe1`。

## 成片
- 路径：`~/workspace/makefun/gta6-clipper-01/clip/gta6-clipper-final.mp4`（也在仓库里，见下）
- 规格：35.5 秒，1080x1920 竖屏，30fps，H.264 + AAC，11.4 MB，YouTube Shorts 格式。
- 素材：Rockstar 官方 GTA 6 预告片 2（YouTube，`VQRLujxTm3c`，yt-dlp 取回）。本机只能拿到 360p（YouTube 对高清格式做了机器人验证；Rockstar 官网只有贴纸动画、Piped/cobalt 也连不上），所以 16:9 画面用“模糊填充底 + 居中原画”的 Shorts 常规做法呈现，没有硬裁成竖屏糊掉。
- 剪辑思路（钩子在前 3 秒）：0–1.5s Vice City 航拍 + 大字 `GTA 6`；1.5–3.5s 车顶跳舞镜头 + `VICE CITY IS BACK`；接着快切预告片高光——高速路飞机、`MAY 26, 2026`、警车追逐、Lucia & Jason 重逢、夜店、摩托+飞机、夜卡车/拥抱、霓虹俱乐部、VI 标题卡；最后 8 秒黑底粉字尾卡推介 make.fun，屏幕文字 + 口播都有。
- 口播（Kokoro-82M，男声 `am_adam`，6.7 秒）：“Make clips like this with AI — and get paid for it. Check out make dot fun. Link in the description.”
- 质检：逐段抽帧看过；修过一个问题——预告片前 ~6 秒是黑场（只有 R* 角标），钩子段已从 5.0s 移到 6.2s；音频均值 -14.4 dB、峰值 0.0 dB（原片电平，未削波）。
- 复现剪辑：`build/build_clip.py`（ffmpeg，一键重跑；源文件在 `footage/`，未进仓库）。

## 仓库
- https://github.com/liuyue449-spec/gta6-clipper-01（公开）
- 提交：`a151818c0dd1e709ad8bcd67f351bd65ed4f9441`（main 分支，已推送）
- 含：`LICENSE`（MIT，带 SPDX 行）、`README.md`（三枚 make.fun 实时徽章已填好 owner/repo）、`.makefun/owner.json`（payout 钱包）、`main.ts`、`VIDEO.json`（还是占位符，见下）、`AGENT.md`、`build/build_clip.py`、成片 `clip/gta6-clipper-final.mp4`。
- About 已设：homepage `https://make.fun/bounty/gta6-clipper-01`，topics `makefun, ai-agents, bounties, growth`。
- 仓库建于 2026-11-20T03:37:54Z，在比赛开赛（01:00Z）之后，满足 repo_created_after_open。

## main.ts 输出约定
- `main.ts`（Node 22，只用标准库）只做一件事：把仓库根目录的 `VIDEO.json` 原样复制到 `/output/VIDEO.json`。本地跑法：`mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`，已验证通过，`out/VIDEO.json` 与仓库里的逐字节一致。
- `/output` 里不要自己写别的：房子（house）会在程序跑完后自己把 `/output/video.counts.json`（它从 YouTube Data API 读到的播放量）写进去，覆盖同名文件。
- `VIDEO.json` 格式：`{"url": "https://www.youtube.com/shorts/<id>"}`，`/watch?v=<id>` 或 `youtu.be/<id>` 也认。

## 本地检查结果
- kit check（`node cli/makefun.mjs check --kit . --repo ~/workspace/makefun/gta6-clipper-01`）：4 项通过——snapshot（9 个文件，11,447,094 字节，在容量上限内）、license_osi（MIT）、entrypoint（main.ts → node22）；唯一失败是 `transcripts_present`，因为 bundle 要到提交时才打，这是正常的；其余 15 项 transcript 检查因无 bundle 而跳过；5 项“提交时检查”（repo_public、repo_owner、repo_created_after_open、commit_in_repo、duplicate_snapshot）现实中都已满足。
- kit 位置：`~/workspace/makefun/gta6-clipper-01/kit/gta6-clipper-01-kit/`。

## 还差的一步（主人做）
1. 主人用自己的公开 YouTube 频道，把 `clip/gta6-clipper-final.mp4` 作为公开 Short 发布（不要设私享/不公开；要在 2026-11-23 09:00 CST 之前发布；保持公开直到结果出炉）。
2. 视频简介里逐字写上这一行（同时满足“$500 bounty”和 make.fun 链接两项检查）：
   `Made by my AI agent for a $500 bounty on make.fun, where you can earn money making clips with AI: https://make.fun/bounty/gta6-clipper-01`
   再加上任意一个 play code（任选其一即可；也可以改放频道简介里）：
   - `makefun-macaw-hobby-eel`
   - `makefun-armchair-lemonade-gold`
   - `makefun-beach-flask-sandal`
   - `makefun-crow-pagoda-jade`
   （play code 不是秘密，kit check 也印出来了。）
3. 把视频链接（分享按钮复制的那种，`https://www.youtube.com/shorts/<id>`）发回安安。

## 提交会话要做的事（拿到链接后，新会话）
1. 把 `VIDEO.json` 里的占位符换成真实地址，提交并推送（新 commit）。
2. 本地跑一遍 `main.ts`（上面有命令）。
3. 从顶层 agent 打 bundle：`node cli/makefun.mjs bundle --repo <仓库> --system-prompt <文件> --effort <level> --out transcripts.tar.gz`——必须包含本会话（含本子任务会话）的全部记录，`--muse-usage` 附上用量；再跑一次 kit check，确认 transcripts_present 通过。
4. 提交（不要用别的 keypair；payout 钱包是上面那个）：
   `node cli/makefun.mjs submit --competition gta6-clipper-01 --repo-url https://github.com/liuyue449-spec/gta6-clipper-01 --commit <新sha> --title <名字> --bundle transcripts.tar.gz --keypair <keypair文件>`
5. 提交后在汇报里报回执和总用时。注意：同一视频只能一个账号报；Force_Last 规则下最新一次提交会覆盖之前的。

## 其它注意
- 片子画面是 360p 源上变换来的；如果以后某台机器能拿到 1080p 预告片，用 `build/build_clip.py` 换源重跑即可（分段时间点不变）。
- 不要买量、不要刷播放量，会被取消资格。
- 推荐码（README 里已用）：`y9xqfw0n`。
