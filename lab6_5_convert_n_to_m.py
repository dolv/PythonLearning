def convert_n_to_m(x, n, m):
    posible_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(x) in [str, int, long] and \
            n >= 1 and m <= 36 and m >= 1 and \
            all(chars in posible_chars[:n] for chars in str(x).upper()):
        decimal_value = 0
        x = str(x).upper()
        for order in range(len(x)):
            decimal_value += posible_chars.index(x[-(order+1):][0]) * pow(n, order)
        m_val = ''
        if m == 1:
            m_val = '0' * decimal_value
        else:
            while decimal_value >= m:
                m_val = posible_chars[decimal_value % m] + m_val
                decimal_value = int(decimal_value / m)
            m_val = posible_chars[decimal_value % m] + m_val
        return m_val
    else:
        return False

print convert_n_to_m([123], 4, 3)
print convert_n_to_m("0123", 5, 6)
print convert_n_to_m("123", 3, 5)
print convert_n_to_m(123, 4, 1)
print convert_n_to_m(-123.0, 11, 16)
print convert_n_to_m("A1Z", 36, 16)
print convert_n_to_m([1], 2, 2)
print convert_n_to_m(True, 1, 2)
print convert_n_to_m({1: 0}, 2, 2)
print convert_n_to_m(-777, 10, 2)
print convert_n_to_m(123123123123123123123.0, 11, 16)
print convert_n_to_m(100, 2, 1)
print convert_n_to_m(0, 10, 2)
print convert_n_to_m(000, 10, 2)
print convert_n_to_m(777, 10, 2)
print convert_n_to_m(777L, 10, 2)
print convert_n_to_m('ZZZZ', 36, 13)
print convert_n_to_m('000ZZZZ', 36, 13)
print convert_n_to_m('ZZZZ', 35, 13)
print convert_n_to_m('qweasd', 33, 36)
print convert_n_to_m('123123123123123123123', 11, 16)
print convert_n_to_m(123123123123123123123, 11, 16)
print convert_n_to_m(123123123123123123123, 10, 10)
print convert_n_to_m('bnh34521', 31, 14)