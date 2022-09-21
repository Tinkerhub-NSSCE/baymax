import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

directory = os.path.dirname(os.path.realpath(__file__))

def generate_greeting(avatar_url:str, name:str):
    global directory
    avatar = BytesIO(requests.get(avatar_url).content)
    bg_image_path = f'{directory}/cards/welcome_card.png'

    im = Image.open(avatar)
    im = im.resize((163,163))

    font_name = 'Gilroy-SemiBold.ttf'
    font = ImageFont.truetype(font=f'{directory}/fonts/{font_name}', size=25)
    color_white = (255,255,255)
    bigsize = (im.size[0]*3, im.size[0]*3)

    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.Resampling.LANCZOS)
    im.putalpha(mask)

    im = im.resize((163,163))

    background = Image.open(bg_image_path)
    draw = ImageDraw.Draw(background)

    if len(name) > 20:
        name = name.split(' ')
        if len(name) > 1:
            name = f"{name[0]} {name[1]}"
            if len(name) > 21:
                name = name.split(' ')
                name = f"{name[0]} {name[1][0].capitalize()}"
        else:
            name = str(name[0])

    draw.text((189, 105), name, fill=color_white, font=font)

    background.paste(im, (12,13), im)

    out = BytesIO()
    background.save(out, format='PNG')

    return out