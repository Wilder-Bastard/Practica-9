from PIL import Image, ImageFilter
import os
os.makedirs("filtered", exist_ok=True)
for i in range(1,6):
    filename= f"{i}.jpg"

    img=Image.open(filename)
    filtered = img.filter(ImageFilter.CONTOUR)
    filtered.save(f"filtered/{i}.jpg")
