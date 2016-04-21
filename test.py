def print_matrix(list, size):
    width = size ** 2
    h_div = u'\u2554'.encode('utf8')
    c_div = u'\u2560'.encode('utf8')
    ci_div = u'\u255F'.encode('utf8')
    f_div = u'\u255A'.encode('utf8')
    for i in range(size):
        h_div += ('='.encode('utf8') * len(str(width**2)) + u'\u2564'.encode('utf8') ) * size
        h_div = h_div[:-3] + u'\u2566'.encode('utf8')
        c_div += ('='.encode('utf8') * len(str(width**2)) + u'\u256A'.encode('utf8') ) * size
        c_div = c_div[:-3] + u'\u256C'.encode('utf8')
        ci_div += ('-'.encode('utf8') * len(str(width**2)) + u'\u253C'.encode('utf8') ) * size
        ci_div = ci_div[:-3] + u'\u256B'.encode('utf8')
        f_div += ('='.encode('utf8') * len(str(width**2)) + u'\u2567'.encode('utf8') ) * size
        f_div = f_div[:-3] + u'\u2569'.encode('utf8')



    h_div = h_div[:-3] + u'\u2557'.encode('utf8')
    c_div = c_div[:-3] + u'\u2563'.encode('utf8')
    ci_div = ci_div[:-3] + u'\u2562'.encode('utf8')
    f_div = f_div[:-3] + u'\u255d'.encode('utf8')

    print h_div

    for i in range(width):
        body_line = str(u'\u2551'.encode('utf8'))
        ff = i*width; ft = i * width + width
        line = list[i * width:i * width + width]
        for j in range(width):
            if j % size == size - 1:
                body_line += "{0: >{w}}".format(str(line[j]), w=len(str(width**2))) + u'\u2551'.encode('utf8')
            else:
                body_line += "{0: >{w}}".format(str(line[j]), w=len(str(width**2)))  + u'\u2502'.encode('utf8')
        print body_line
        if i % size != size - 1:
            print ci_div

        if i % size == size -1 \
            and i < width - 1:
            print c_div
    print f_div
s = 3
grid = range(s**4)
print_matrix(grid, s)
