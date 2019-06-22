#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os, sys

fillcolor = "white"
shadowcolor = "black"
font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/FreeSansBold.ttf", 50)

msg = sys.argv[1:]

top_msg = msg[0].decode("utf-8")
bottom_msg = msg[1].decode("utf-8")
top_box = textwrap.wrap(top_msg, width=25)
bottom_box = textwrap.wrap(bottom_msg, width=20)


imageFile = "mm-lali.jpg"
im = Image.open(imageFile)
MAX_W, MAX_H = im.size

draw = ImageDraw.Draw(im)
current_h, pad = 0.05 * MAX_H, 10

for line in top_box:
    w, h = draw.textsize(line, font=font)
    x, y = (MAX_W - w) / 2, current_h
    # thin border
    draw.text((x-1, y), line, font=font, fill=shadowcolor)
    draw.text((x+1, y), line, font=font, fill=shadowcolor)
    draw.text((x, y-1), line, font=font, fill=shadowcolor)
    draw.text((x, y+1), line, font=font, fill=shadowcolor)
    # thicker border
    draw.text((x-1, y-1), line, font=font, fill=shadowcolor)
    draw.text((x+1, y-1), line, font=font, fill=shadowcolor)
    draw.text((x-1, y+1), line, font=font, fill=shadowcolor)
    draw.text((x+1, y+1), line, font=font, fill=shadowcolor)
    draw.text((x, y), line, font=font, fill=fillcolor)
    current_h += h + pad

current_h, pad = 0.85 * MAX_H, 10
for line in bottom_box:
    w, h = draw.textsize(line, font=font)
    x, y = (MAX_W - w) / 2, current_h
    # thin border
    draw.text((x-1, y), line, font=font, fill=shadowcolor)
    draw.text((x+1, y), line, font=font, fill=shadowcolor)
    draw.text((x, y-1), line, font=font, fill=shadowcolor)
    draw.text((x, y+1), line, font=font, fill=shadowcolor)
    # thicker border
    draw.text((x-1, y-1), line, font=font, fill=shadowcolor)
    draw.text((x+1, y-1), line, font=font, fill=shadowcolor)
    draw.text((x-1, y+1), line, font=font, fill=shadowcolor)
    draw.text((x+1, y+1), line, font=font, fill=shadowcolor)
    draw.text((x, y), line, font=font, fill=fillcolor)
    current_h += h + pad

num_mm = 1
for filename in os.listdir('.'):
        if filename.startswith("lali-mm") and filename.endswith('.jpg'):
            num_mm += 1

im.save('lali-mm-%02d.jpg' % num_mm)
print('lali-mm-%02d.jpg criado' % num_mm)
