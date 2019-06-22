#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os, sys, textwrap

if len(sys.argv) == 4:
    imageFile = sys.argv[-1]
    if os.path.exists(imageFile):
        print('creating meme on "%s"' % imageFile)
    else:
        print('** either the file "%s" is missing or is not an image' % imageFile)
else:
    ''' replace the file below to use as constant input image '''
    imageFile = "lali-mm.jpg"
    print('creating meme on "%s"' % imageFile)


msg = sys.argv[1:]

top_msg = msg[0].decode("utf-8")
bottom_msg = msg[1].decode("utf-8")
top_box = textwrap.wrap(top_msg, width=25)
bottom_box = textwrap.wrap(bottom_msg, width=20)

fillcolor = "white"
shadowcolor = "black"
font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/FreeSansBold.ttf", 50)

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

current_h, pad = 0.80 * MAX_H, 10
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
prefix = os.path.splitext(imageFile)[0]
for filename in os.listdir('.'):
        if filename.startswith(prefix + '-') and filename.endswith('.jpg'):
            num_mm += 1

im.save('%s-%02d.jpg' % (prefix, num_mm))
print('%s-%02d.jpg created' % (prefix, num_mm))
