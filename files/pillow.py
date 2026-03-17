from PIL import Image

img = Image.open('ushguli.webp')

print(img.size)

img.show()