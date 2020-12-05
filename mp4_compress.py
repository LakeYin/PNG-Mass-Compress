import ffmpeg
import os

files = os.listdir()

if not os.path.exists("new"):
    os.makedirs("new")

for f in files:
    if f.lower().endswith(".mp4"):
        print("Converting " + f)
        stream = ffmpeg.input(f)
        stream = ffmpeg.output(stream, "new/" + f, vcodec="hevc")
        ffmpeg.run(stream)
        print("Converted " + f)
