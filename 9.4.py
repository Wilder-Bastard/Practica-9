from PIL import ImageDraw, ImageFont
from PIL import Image
font = ImageFont.truetype("arial.ttf", size=40)
img = Image.open("C:/adamovahuinya/1. study/proga/Kuzma.jpg")
draw = ImageDraw.Draw(img)
x = img.width -200
y = img.height - 50
draw.text((x,y), "Я водяной",fill="white", font=font)
img.save("Kuzma_wodyanoy.jpg")