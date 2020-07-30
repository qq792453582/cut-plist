import os
import cut_plist
from PIL import Image

inputPath = os.path.normpath(input("dir: ").strip("\""))
outputPath = os.path.normpath(input("output dir: ").strip("\""))

for root, dirs, files in os.walk(inputPath):
    for file in files:
        [name, extension] = os.path.splitext(file)
        if extension == ".plist":
            plist_path = os.path.join(root, file)
            texture_path = os.path.join(root, name + ".png")
            save_dir = os.path.join(root.replace(inputPath, outputPath), name)
            plist = cut_plist.read_plist(plist_path)
            texture = Image.open(texture_path)
            cut_plist.cut_plist(plist["frames"], texture, save_dir)
            print("cut: " + plist_path + " finish")
