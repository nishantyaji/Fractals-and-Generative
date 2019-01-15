from PIL import Image

size = (640,480)
defaultColour = (0,0,255)
img = Image.new("RGB", (640,480), defaultColour)

for x in range(size[0]):
    for y in range(size[1]):
        img.putpixel((x,y), (0,(y*255)//size[1],0))

img.save("greengradient.png","PNG")

img.show()