from PIL import Image
from math import sqrt as sqrt

def areaTriangle(vertices):
    return abs(vertices[0][0]*(vertices[1][1] - vertices[2][1])
                + vertices[1][0]*(vertices[2][1] - vertices[0][1])
                + vertices[2][0]*(vertices[0][1] - vertices[1][1]))/2.0

def insideTriangle(vertices, point) -> bool :
    A = areaTriangle(vertices)
    A0 = areaTriangle([point, vertices[1], vertices[2]])
    A1 = areaTriangle([vertices[0], point, vertices[2]])
    A2 = areaTriangle([vertices[0], vertices[1], point])
    return( A == (A0 + A1 + A2))

def display():
    size = (640,480)
    defaultColour = (0,0,255)
    triangleColour = (0,255,0)
    leftVertex = (100, 350)
    side = 250
    triangleCordinates = [ leftVertex, (round(leftVertex[0]+side/2.0), round((leftVertex[1]-side*sqrt(3)/2.0))),
        (leftVertex[0]+side,leftVertex[1])]

    img = Image.new("RGB", (640,480), defaultColour)

    for x in range(size[0]):
        for y in range(size[1]):
            if(insideTriangle(triangleCordinates, (x,y))):
                img.putpixel((x,y), triangleColour)

    img.save("triangle.png","PNG")
    img.show()

if __name__ == '__main__':
    display()