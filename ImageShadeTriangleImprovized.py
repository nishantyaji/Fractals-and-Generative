from PIL import Image
from math import sqrt as sqrt

def shadeTriangle(vertices, color, img):
    """ vertices are in the order lefet, top, right
    """
    left, top, right = vertices
    for x in range(left[0], round((left[0] + right[0])/2)):
        y_ = round(left[1] + (x-left[0]) * (top[1]-left[1]) / (top[0] - left[0]))
        for y in range(y_, left[1]):
            img.putpixel((x,y), color)

    for x in range(round((left[0] + right[0])/2), right[0]):
        y_ = round(top[1] + (x-top[0]) * (right[1]-top[1]) / (right[0] - top[0]))
        for y in range(y_, right[1]):
            img.putpixel((x,y), color)

def display():
    size = (640,480)
    defaultColour = (0,0,255)
    triangleColour = (0,255,0)
    leftVertex = (100, 350)
    side = 250
    triangleCordinates = [ leftVertex, (round(leftVertex[0]+side/2.0), round((leftVertex[1]-side*sqrt(3)/2.0))),
        (leftVertex[0]+side,leftVertex[1])]

    img = Image.new("RGB", (640,480), defaultColour)
    shadeTriangle(triangleCordinates, triangleColour, img)
    img.save("triangle.png","PNG")
    img.show()

if __name__ == '__main__':
    display()