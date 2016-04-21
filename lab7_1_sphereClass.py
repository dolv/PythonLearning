import math

class Sphere(object):
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.set_radius(radius)
        self.set_center(x, y, z)

    def get_volume(self):
        return float(4.0 / 3.0 * math.pi * self.radius ** 3)

    def get_square(self):
        return float(4.0 * math.pi * self.radius)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return tuple(self.center)

    def set_radius(self, r):
        self.radius = float(r)

    def set_center(self, x, y, z):
        self.center = [float(x), float(y), float(z)]

    def is_point_inside(self, x, y, z):
        point = [x - self.center[0], y - self.center[1], z - self.center[2]]
        return self.radius >= math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)



s0 = Sphere() # test sphere creation with radius and default center
print s0.is_point_inside(0, 0, 0)
print s0.is_point_inside(0.99, 0, 0)
print s0.is_point_inside(0, 0.99, 0)
print s0.is_point_inside(0, 0, 0.99)
s0.set_radius(1.1)
s0.set_center(0.5, 1, 0)
print s0.is_point_inside(0, 0.99, 0)
print s0.is_point_inside(0.99, 0, 0)
print s0.is_point_inside(0, 0, 0.99)
print
s2 = Sphere(2)
print s2.is_point_inside(1.99, 0, 0)
print s2.is_point_inside(0, 0, 2.99)
print
s3 = Sphere(1.99, 1, 2, -1)
print s3.is_point_inside(0, 0.99, 0)
print s3.is_point_inside(0.99, 0, 0)
print s3.is_point_inside(0, 0, 0.99)
print
s4 = Sphere(0,0,0,0)
print s4.is_point_inside(0, 0.99, 0)
print s4.is_point_inside(0.99, 0, 0)
print s4.is_point_inside(0, 0, 0.99)
print s4.is_point_inside(0, 0, 0)