from PIL import Image
im = Image.open("CatNyan.jpg")
width, height = im.size
print(im.size)
if im: 
    print("now it's on")
    print(im)
im = Image.close()
if im:
    print("it didn't work")
    print(im)