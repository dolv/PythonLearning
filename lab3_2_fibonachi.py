
import sys

a = int(sys.argv[1])

n = 0
n_plus_1 = 1
n_fibonachi = n
for i in range(a):
    n = n_plus_1
    n_plus_1 = n_fibonachi
    n_fibonachi = n + n_plus_1
print(str(n_fibonachi))
