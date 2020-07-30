import os
import cut_plist
from PIL import Image

plist_path = os.path.normpath(input("plist: ").strip("\""))

default_texture_path = os.path.splitext(plist_path)[0] + ".png"
default_save_dir = os.path.split(plist_path)[0]

texture_path = os.path.normpath(input("texture (" + default_texture_path + "): ").strip("\""))
save_dir = os.path.normpath(input("save (" + default_save_dir + "): ").strip("\""))

if not texture_path:
    texture_path = default_texture_path
if not save_dir:
    save_dir = default_save_dir

plist = cut_plist.read_plist(plist_path)
frames = plist["frames"]
tip = "sprite frames: "
for key in frames:
    tip += key + ", "
print(tip)
keys = input("enter cut sprite key (split with ',',enter empty  output all sprites): ")
keys = list(filter(None, keys.split(",")))
output = {}
if len(keys) == 0:
    output = frames
else:
    for key in keys:
        key = key.strip()
        if key in frames:
            output[key] = frames[key]
        else:
            print("not found frame: " + key)
texture = Image.open(texture_path)
cut_plist.cut_plist(output, texture, save_dir)
print("cut sprites finish")
