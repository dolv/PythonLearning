def super_fibonacci(x, y):
    if x>y:
        n = []
        for i in range(y):
            n.append(1)
        for i in range(x-y):
            n.append(sum(n[i:]))
        return n[x-1]
    else:
        return 1
print super_fibonacci(9, 3)