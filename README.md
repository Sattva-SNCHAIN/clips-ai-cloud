# Clips AI One-Click Deployment (GitHub Codespaces)

Clips AI 是一个开源库，可自动把长视频切割成多个片段，并支持从 16:9 转换成 9:16 的竖屏格式。

本仓库提供：

✔ 一键创建 GitHub Codespace  
✔ ClipsAI/WhisperX 分离独立环境（避免冲突）  
✔ ffmpeg + libmagic 自动安装  
✔ 示例代码完全可运行  

---

## 🚀 一键启动方式

1. 打开仓库
2. 点击：

```
Code → Create codespace on main
```

Codespace 将自动安装所有依赖，并创建两个独立虚拟环境：

- `/workspaces/env-clipsai`
- `/workspaces/env-whisperx`

---

## 📦 包含的环境

| 环境名称 | 用途 | 内容 |
|---------|------|-------|
| env-clipsai | Clips AI 主程序 | `clipsai` |
| env-whisperx | 语音识别 | `whisperx`（从 Git 安装） |

系统依赖自动安装：

- ffmpeg  
- libmagic  

---

## ▶️ 运行示例

激活 ClipsAI 环境：

```bash
source /workspaces/env-clipsai/bin/activate
python run_clips.py
```

如果你只想调试 WhisperX：

```bash
source /workspaces/env-whisperx/bin/activate
```

---

## 📝 替换你的视频与 token

编辑 `run_clips.py`：

```python
VIDEO_PATH = "/workspaces/clips-ai-cloud/your_video.mp4"
HF_TOKEN = "your token"
```

即可运行。

---

## 📁 项目结构

```
.
├── .devcontainer/
│   ├── devcontainer.json
│   └── setup.sh
├── run_clips.py
├── README.md
```

---

## 🍻 完成！

完成后你即可：

- 自动剪辑视频（ClipFinder）  
- 自动转录（WhisperX）  
- 自动竖屏智能裁切（resize + pyannote）  
- 全程无需配置本地环境  
- 只需 GitHub Codespace 即可运行  
