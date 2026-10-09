from PIL import Image
img = Image.open("C:/adamovahuinya/1. study/proga/Kuzma.jpg")
img.show()
print(f"Размер: {img.size}")
print(f"Формат: {img.format}")
print(f"Модель: {img.mode}")
