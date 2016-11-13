from PIL import Image,ImageDraw,ImageFont

def createCard(name = "Anonymus"):
    print("meow")
    img = Image.open("../creator/data/prepaid_print.png")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 96)

    draw.text((400, 70), name, (0, 0, 0), font=font)
    img.save("uploads/scretch.png")