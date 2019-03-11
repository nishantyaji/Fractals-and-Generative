import math
from PIL import Image, ImageDraw
import random
import functools
import operator

class CircleSub:
    def __init__(self, x, y, img):
        self.center = (x,y)
        self.radius = 1
        self.grow_flag = True
        self.circle_color = (0, 255, 0)
        self.img = img

    def within_boundary(self):
        return ((self.center[0]-self.radius) >= 0) and ((self.center[1]-self.radius) >= 0) and \
            ((self.center[0]+self.radius) < self.img.size[0]) and \
                ((self.center[1]+self.radius) < self.img.size[1])

    def grow(self):
        if self.grow_flag:
            if self.within_boundary():
                self.radius += 1
            else:
                self.grow_flag = False
        return self.grow_flag

    def draw(self):
        draw = ImageDraw.Draw(self.img)
        draw.ellipse((self.center[0]-self.radius, self.center[1]-self.radius, 
        self.center[0]+self.radius, self.center[1]+self.radius), outline = self.circle_color)

    @staticmethod
    def distance(p1, p2):
        return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

    def intersects_another(self, other):
        dist = self.distance(self.center, other.center)
        res = (dist <= (self.radius+other.radius))
        if res == True:
            self.grow_flag = False
        return res

    def point_inside(self, point):
        dist = self.distance(self.center, point)
        return dist <= self.radius


class CirclePacker:
    def __init__(self, image_size):
        self.default_bg_color = (0, 0, 0, 0)
        self.img = Image.new("RGBA", image_size, self.default_bg_color)
        self.list_of_circles = []
        self.loops_till_no_add = 100
        self.img_file_name = 'circle_packing.bmp'

    def generate_random_circle(self):
        return CircleSub(random.randint(0, self.img.size[0]-1), random.randint(0, self.img.size[1]-1), self.img)

    def init(self):
        first = self.generate_random_circle()
        while True:
            grow1 = first.grow()
            if grow1 == False:
                break
        self.list_of_circles.append(first)

    def iterate(self):
        howmany_didnot_grow_count = 0
        while howmany_didnot_grow_count < self.loops_till_no_add:
            c = self.generate_random_circle()
            in_flags = [(c2.point_inside(c.center)) for c2 in self.list_of_circles if c2 != c]
            is_in_a_circle = functools.reduce(operator.or_, in_flags, False)
            if is_in_a_circle == False:
                howmany_didnot_grow_count = 0
                while c.grow_flag:
                    intersect_flags = [(c2.intersects_another(c)) for c2 in self.list_of_circles if c2 != c]
                    is_intersecting = functools.reduce(operator.or_, intersect_flags, False)
                    if is_intersecting:
                        self.list_of_circles.append(c)
                        break
                    else:
                        c.grow()
            else:
                howmany_didnot_grow_count += 1
    
    def display(self):
        for c in self.list_of_circles:
            c.draw()
        self.img.show()
    
    def save(self):
        self.img.save(self.img_file_name, dpi=(800, 800))

if __name__ == '__main__':
    cp = CirclePacker((800, 800))
    cp.init()
    cp.iterate()
    cp.display()
    cp.save()