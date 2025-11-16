from clipsai import ClipFinder, Transcriber, resize

# 修改成你的文件路径
VIDEO_PATH = "/workspaces/clips-ai-deploy/sample.mp4"
HF_TOKEN = "your_pyannote_token_here"

# Step 1: Transcribe
transcriber = Transcriber()
transcription = transcriber.transcribe(audio_file_path=VIDEO_PATH)

# Step 2: Find Clips
clipfinder = ClipFinder()
clips = clipfinder.find_clips(transcription=transcription)

print("===== FOUND CLIPS =====")
for c in clips:
    print(c.start_time, "→", c.end_time)

# Step 3: Resize (optional)
crops = resize(
    video_file_path=VIDEO_PATH,
    pyannote_auth_token=HF_TOKEN,
    aspect_ratio=(9, 16)
)

print("===== CROPS =====")
print(crops.segments)
