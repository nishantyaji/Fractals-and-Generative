from PIL import Image
import random
import numpy

class RandomBezier:
    def __init__(self, levels, 
                    gradient=0.001, 
                    img=None, 
                    img_size=(800, 800), 
                    dpi=(800, 800),
                    img_file_name='beziersample.bmp', 
                    default_bg_color=(0, 0, 0, 0), 
                    default_fg_color_fn = (lambda x: (255, 255, 0, 0))):
        if img == None:
            self.img = Image.new('RGBA', img_size, default_bg_color)
        else:
            self.img = img 
        self.levels = levels
        self.gradient = gradient
        self.dpi = dpi
        self.img_file_name = img_file_name
        self.default_bg_color = default_bg_color
        self.default_fg_color_fn = default_fg_color_fn

    @staticmethod
    def find_ratio_point(p1, p2, r):
        return p1[0]+(p2[0]-p1[0])*r, p1[1]+(p2[1]-p1[1])*r

    def random_points(self):
        return [(random.randint(0, self.img.size[0]), random.randint(0,self.img.size[1])) for _ in range(0, self.levels)]

    def bezier(self):
        points_orig = self.random_points()
        color = self.default_fg_color_fn(None)
        for grad in numpy.arange(0, 1, self.gradient):
            points_array = points_orig.copy()
            for levels in range(self.levels, 1, -1):
                points_new = [self.find_ratio_point(points_array[i], points_array[i+1], grad) for i in range(0, levels-1)]
                if len(points_new) == 1:
                    x,y = int(points_new[0][0]), int(points_new[0][1])
                    if x >= 0 and x <= self.img.size[0]-1 and y >= 0 and y <= self.img.size[1]-1:
                        self.img.putpixel((x, y), color)
                else:
                    points_array = points_new

    def save(self):
        self.img.save(self.img_file_name, 'PNG', dpi=self.dpi)

    def show(self):
        self.img.show()


class RandomBezierSmall(RandomBezier):
    def __init__(self, levels=4, diff=20):
        default_fg_color_fn = lambda x: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        super().__init__(levels=4, default_fg_color_fn=default_fg_color_fn )
        self.diff = diff

    @staticmethod
    def limit_within_boundaries(val, min_allowed, max_allowed):
        return max(min(val, max_allowed), min_allowed)

    def random_points(self):
        points = [(random.randint(0, self.img.size[0]), random.randint(0, self.img.size[1]))]    
        for _ in range(0, self.levels-1) :
            rand_x = random.randint(points[0][0]-self.diff, points[0][0]+self.diff)
            x = self.limit_within_boundaries(rand_x, 0, self.img.size[0])
            rand_y = random.randint(points[0][1]-self.diff, points[0][1]+self.diff)       
            y = self.limit_within_boundaries(rand_y, 0, self.img.size[1]-1)
            points.append((x, y))
        return points