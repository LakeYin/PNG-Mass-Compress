from converter import Converter
import os

files = os.listdir()
c = Converter()

if not os.path.exists("new"):
    os.makedirs("new")

for f in files:
    if f.lower().endswith(".mp4"):
        print("Converting " + f)
        c.convert(f, "new/" + f, {'format': 'mp4','video': {'codec': 'hevc'}})
        print("Converted " + f)
