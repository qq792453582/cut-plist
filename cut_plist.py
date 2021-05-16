import plistlib
import os
import numpy as np
from PIL import Image


def read_plist(plist_path):
    with open(plist_path, "rb") as fp:
        return plistlib.load(fp)


def to_list(x):
    return x.replace("{", "").replace("}", "").split(",")


def cut_plist(output, texture, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for key in output:
        data = output[key]
        rect = to_list(data["textureRect"])
        rotated = data["textureRotated"]
        x = int(rect[0])
        y = int(rect[1])
        width = int(rect[2])
        height = int(rect[3])
        if rotated:
            width, height = height, width
        box = (x, y, x + width, y + height)

        newSize = np.array([width, height])
        offset = np.array(to_list(data["spriteOffset"])).astype("float")*(-1,1)
        srcSize = np.array(to_list(data["spriteSourceSize"])).astype("float")
        offset = ((newSize-srcSize)/2+offset).astype("int")

        sprite = texture.crop(box).crop((*offset,*(offset+srcSize)))


        if rotated:
            sprite = sprite.transpose(Image.ROTATE_90)
        save_path = os.path.splitext(os.path.join(save_dir, key))[0] + ".png"
        sprite.save(save_path)
