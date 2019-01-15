from PIL import Image
from math import sqrt
import numpy as np
import lib.Triangle as triangle


def doSierpinski(vertices, img, colors):
        left, top, right = vertices

        if (abs(left[0] - right[0]) < 3) & (abs(left[1] - right[1]) < 3):
            return

        leftmid = (left[0] + top[0])//2, (left[1] + top[1])//2 
        rightmid = (right[0] + top[0])//2, (right[1] + top[1])//2
        botmid = (left[0]+right[0])//2, (left[1]+right[1])//2

        triangle.shadeTriangle([left, leftmid, botmid], colors[1], img)
        triangle.shadeTriangle([botmid, rightmid, right], colors[1], img)
        triangle.shadeTriangle([leftmid, top, rightmid], colors[1], img)
        triangle.shadeTriangle([leftmid, botmid, rightmid], colors[0], img)

        doSierpinski([left, leftmid, botmid], img, colors)        
        doSierpinski([botmid, rightmid, right], img, colors)
        doSierpinski([leftmid, top, rightmid], img, colors)

def display():
    size = (640,480)
    defaultColour = (0,0,255)
    triangleColour = (0,255,0)
    leftVertex = (100, 350)
    side = 250
    triangleCordinates = [leftVertex, 
    (round(leftVertex[0]+side/2.0), round((leftVertex[1]-side*sqrt(3)/2.0))),
    (side+leftVertex[0],leftVertex[1]),]

    img = Image.new("RGB", (640,480), defaultColour)

    doSierpinski(triangleCordinates, img, (defaultColour, triangleColour))

    img.save("Sierpinski.png","PNG")
    img.show()

if __name__ == '__main__':
    display()