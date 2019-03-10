from PIL import Image
import random

size = (6400,4800)
defaultColour = (0,0,255)
img = Image.new("RGB", size, defaultColour)

for x in range(size[0]):
    for y in range(size[1]):
        img.putpixel((x,y), (0,(y*255)//size[1],0))

numRandoms = 115

for i in range(0, numRandoms):
    radiusMax = 200
    xmin = 0
    ymin = 0

    xrandom = random.randint(xmin, size[0]-xmin)
    yrandom = random.randint(ymin, size[1]-ymin)
    rrandom = random.randint(1, radiusMax)

    for x in range(size[0]):
        for y in range(yrandom, size[1]):
            if (x-xrandom)*(x-xrandom)+(y-yrandom)*(y-yrandom) <rrandom*rrandom and 2*yrandom-y>0:
                downpixel = img.getpixel((x,2*yrandom-y))
                uppixel = img.getpixel((x,y))
                img.putpixel((x,y),downpixel)
                img.putpixel((x,2*yrandom-y),uppixel)

img.save("OverlappingCirles.png","PNG", dpi=(1600,1600))
img.show()