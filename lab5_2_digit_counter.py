def counter(a, b):
    result = ''
    a = str(a)
    b = str(b)
    for char in b:
        if a.find(char) != -1 and result.find(char) == -1:
            result += char
    return len(result)

print counter(98123560, 79266)