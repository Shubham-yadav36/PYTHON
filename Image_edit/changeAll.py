from PIL import Image
import os

for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open('img1.jpg')
        file_name, exten = os.path.splitext(item)
        img1.save(f'{file_name}.png')