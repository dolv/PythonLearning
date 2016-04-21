import math

def find_fraction(summ):
    a = int(summ / 2)
    b = summ - a
    if summ > 5:
        listPrime = [2]
        for i in range(3, int(math.sqrt(summ))):
            yes = True
            for prime in listPrime:
                if i % prime == 0:
                    yes = False
                    break
            if yes:
                listPrime.append(i)
    else:
        listPrime = range(1, a)
    while a > 0:
        if a < b:
            has_Common_divider = False
            for i in listPrime:
                if a % i == 0 and b % i == 0 :
                    has_Common_divider = True
                    break
            if not has_Common_divider:
                return (a, b)
        a -= 1
        b = summ - a
    return False

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)