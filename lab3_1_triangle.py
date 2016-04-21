import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

is_triangle = False
if (a < b + c) and \
        (a > b - c) and \
        (b < a + c) and \
        (b > a - c) and \
        (c < a + b) and \
        (c > a - b):
    is_triangle = True
if is_triangle:
    print "triangle"
else:
    print "not triangle"
