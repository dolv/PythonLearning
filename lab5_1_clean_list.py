def clean_list(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] not in result:
            result.append(lst[i])
        elif str(lst[i]) != str(result[result.index(lst[i])]):
            result.append(lst[i])
    return result

print clean_list(['asd', 'dsa', 1, '1', 1.0])
