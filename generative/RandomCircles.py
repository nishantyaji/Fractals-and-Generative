import sys
sys.path.insert(0, '../')

from PIL import Image
import random
import lib.Circle as circle

def getSize():
    return (640, 800)

def getRandomCircle():
    return ((random.randrange(1, getSize()[0], 1), random.randrange(1, getSize()[1], 1)),
        random.randrange(1, min(getSize())//2,1))

def randomIterations():
    return 100

def getRandomColor():
    return ( random.randrange(0, 255, 1),random.randrange(0, 255, 1),random.randrange(0, 255, 1) )

def display():
    size = (640,480)
    defaultColour = (0,0,0)
    img = Image.new("RGB", size, defaultColour)

    for i in range(0, randomIterations(), 1):
        center, radius = getRandomCircle()
        color = getRandomColor()
        circle.drawCircleBoundary(center, radius, img, color, size)

    img.show()

if __name__ == '__main__':
    display()