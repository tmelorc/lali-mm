#!/usr/bin/python
# -*- coding: utf-8 -*-
''' Created by Thiago de Melo '''

from PIL import Image, ImageDraw, ImageFont
import os, sys, textwrap

''' replace the file below to use as constant input image '''
imageFile = "lali-mm.jpg"

if len(sys.argv) == 4:
    imageFile = sys.argv[-1]
    if not os.path.exists(imageFile):
        print('** either the file "%s" is missing or is not an image' % imageFile)
        sys.exit()

if len(sys.argv) >= 3:
    msg = sys.argv[1:]
    top_msg = msg[0].decode("utf-8")
    bottom_msg = msg[1].decode("utf-8")
else:
    top_msg = 'top text'
    bottom_msg = 'bottom text'

top_box = textwrap.wrap(top_msg, width=25)
bottom_box = textwrap.wrap(bottom_msg, width=20)

im = Image.open(imageFile)
MAX_W, MAX_H = im.size

font_size = int(0.07 * MAX_W)

fillcolor = "white"
shadowcolor = "black"
font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/FreeSansBold.ttf", font_size)
ascent, descent = font.getmetrics()
# (width, baseline), (offset_x, offset_y) = font.font.getsize(text)

draw = ImageDraw.Draw(im)
current_h, pad = 0.1 * ascent, 0.7 * descent

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

current_h, pad = MAX_H - 1.1 * (ascent + descent), 0.7 * descent
for line in bottom_box[::-1]:
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
    current_h -= (h + pad)


num_mm = []
next_mm = 1
prefix = os.path.splitext(imageFile)[0]
for filename in os.listdir('.'):
        if filename.startswith(prefix + '-') and filename.endswith('.jpg'):
            num_mm.append(int(os.path.splitext(filename.split(prefix + '-')[1])[0]))
            next_mm = max(num_mm)+1

im.save('%s-%02d.jpg' % (prefix, next_mm))
print('creating meme from "%s" and saved on "%s-%02d.jpg"' % (imageFile, prefix, next_mm))
