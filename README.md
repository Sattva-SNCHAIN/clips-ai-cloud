# Clips AI Cloud

**Clips AI Cloud** 是一个基于 Python 的视频剪辑自动化工具，支持演讲、播客、电视剧等视频的智能剪辑。
它使用 **Transcriber** 进行语音转录、**ClipFinder** 找到剪辑点，并可以根据字幕或关键词自动选择片段。

> **注意**：目前 **Resize 功能已注释**，后续需要可以启用。

---

## 目录结构

```text
clips-ai-cloud/
├─ env/                    # 已安装虚拟环境
│  ├─ transcriber_env/     # Transcriber 环境
│  ├─ clipfinder_env/      # ClipFinder 环境
│  └─ resize_env/          # Resize 环境（可选）
├─ scripts/                # Python 脚本
│  ├─ speech_clip.py       # 演讲剪辑脚本
│  └─ drama_clip.py        # 电视剧剪辑脚本
├─ input_videos/           # 本地上传视频
├─ output_clips/           # 剪辑输出目录
└─ README.md
```

---

## 功能特点

* 自动转录视频音频生成字幕
* 自动识别剪辑点
* 根据字幕关键词选择电视剧片段
* 支持演讲或电视剧视频剪辑
* 输出剪辑信息到文本文件，方便后续视频拼接
* Resize 功能可选，支持 16:9 → 9:16

---

## 安装与环境

**建议使用独立虚拟环境**，避免依赖冲突：

1. **Transcriber 环境**

```bash
python -m venv env/transcriber_env
source env/transcriber_env/bin/activate
pip install clipsai
pip install whisperx@git+https://github.com/m-bain/whisperx.git
deactivate
```

2. **ClipFinder 环境**

```bash
python -m venv env/clipfinder_env
source env/clipfinder_env/bin/activate
pip install clipsai
deactivate
```

3. **Resize 环境（可选）**

```bash
python -m venv env/resize_env
source env/resize_env/bin/activate
pip install clipsai
# 安装 ffmpeg, libmagic 等依赖
deactivate
```

> 确保三个环境都已创建完成，Resize 环境暂时可以不启用。

---

## 上传视频

将本地视频上传到仓库目录下的 `input_videos/` 文件夹。
支持格式：`.mp4`、`.mkv`、`.mov`。

---

## 使用脚本

### 演讲剪辑

```bash
# 激活 Transcriber 环境
source env/transcriber_env/bin/activate
cd scripts
python speech_clip.py
```

* 会自动调用 Transcriber + ClipFinder
* 输出剪辑点到控制台和 `output_clips/`

---

### 电视剧剪辑（基于字幕关键词）

```bash
# 激活 Transcriber 环境
source env/transcriber_env/bin/activate
cd scripts
python drama_clip.py
```

* 根据 `KEYWORDS` 关键词列表自动选择剪辑片段
* 输出剪辑时间和台词到 `output_clips/selected_clips.txt`
* 可后续用 FFmpeg 或 MoviePy 拼接成新视频

**示例 KEYWORDS**：

```python
KEYWORDS = ["爱情", "冲突", "惊讶", "秘密"]
```

可以根据剧情或角色定制。

---

## Resize 功能（后续启用）

* Resize 环境依赖 Pyannote HuggingFace Token
* 用于裁剪视频画面、调整纵横比
* 示例：

```python
from clipsai import resize

crops = resize(
    video_file_path="/abs/path/to/video.mp4",
    pyannote_auth_token="YOUR_PYANNOTE_TOKEN",
    aspect_ratio=(9, 16)
)
```

---

## 注意事项

* 空目录 **不会在 GitHub 页面显示**，建议至少放一个 `.gitkeep` 文件
* GitHub 仓库内创建的目录，推荐上传视频和输出剪辑也在仓库管理范围
* Resize 功能暂时注释，可以后续开启

---

## 后续优化

* 自动拼接电视剧片段生成新视频
* Resize 功能恢复，实现竖屏或自适应裁剪
* 支持批量上传和批量剪辑


你希望我帮你生成吗？
