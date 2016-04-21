import sys
import math

x = float(sys.argv[1])
u = float(sys.argv[2])
sig = float(sys.argv[3])

f = 1 /(sig *  math.sqrt(2 * math.pi)) *math.exp(-1 * math.pow(x-u,2)/(2*math.pow(sig,2)))
print f