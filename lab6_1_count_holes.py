import string


def count_holes(n):
    count = 0
    holes = {'9': 1, '8': 2, '6': 1, '4': 1, '0': 1}
    n = ['#', n][len(str(n)) > 0]
    n = [str(n), str(n)[1:]][str(n)[0] in ['-']]
    n = [n, '#'][n == '']
    if all(c in string.digits for c in n):
        for char in str(int(n)):
            if char in holes.keys():
                count += holes[char]
        return count
    else:
        return 'ERROR'

print count_holes('-')