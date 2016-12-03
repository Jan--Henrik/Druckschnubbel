from PIL import Image, ImageDraw, ImageFont

count = 0


def createCard(name="Anonymus"):
    img = Image.open("creator/data/prepaid_print.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 48)
    draw.text((120, 35), name, (0, 0, 0), font=font)
    img.save("app/uploads/scretch%01s.png" % (name.replace(" ", "")))
