from PIL import Image

def shadeTriangle(vertices, color, img):
    """ vertices are in the order left, top, right
    """
    left, top, right = vertices

    if (top[0] == left[0]) or (right[0] == top[0]):
        return

    for x in range(left[0], round((left[0] + right[0])/2)):
        y_ = round(left[1] + (x-left[0]) * (top[1]-left[1]) / (top[0] - left[0]))
        if y_ < left[1]:
            step = 1
        else :
            step = -1
        for y in range(y_, left[1], step):
            img.putpixel((x,y), color)

    for x in range(round((left[0] + right[0])/2), right[0]):
        y_ = round(top[1] + (x-top[0]) * (right[1]-top[1]) / (right[0] - top[0]))
        if y_ < right[1]:
            step = 1
        else:
            step = -1
        for y in range(y_, right[1], step):
            img.putpixel((x,y), color)