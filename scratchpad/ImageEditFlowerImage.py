from PIL import Image

image = Image.open('Flower.jpeg')

for x in range(image.size[0]):
    for y in range(image.size[1]):
        r,g,b = image.getpixel((x,y))
        image.putpixel((x,y),(b,g,r))
        #image.putpixel((x,y),(r*255//255,r*218//255,r*185//255))

image.show()
