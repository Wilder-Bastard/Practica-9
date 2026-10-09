from PIL import Image
img = Image.open("C:/adamovahuinya/1. study/proga/Kuzma.jpg")
new_size = (img.width // 3, img.height // 3)
klein = img.resize(new_size)
klein.save("klein.jpg")
mirror_g = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_g.save("mirror_g.jpg")
mirror_w = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_w.save("mirror_w.jpg")
