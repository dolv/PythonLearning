import string


def find_most_frequent(text):
    f_dict = {}
    for char in string.punctuation:
        text = text.replace(char, ' ')
    for word in text.lower().split():
        if word in f_dict.keys():
            f_dict[word] += 1
        if word not in f_dict.keys():
            f_dict[word] = 1
    if f_dict:
        max_count = max(word for word in f_dict.values())
        for key, value in f_dict.items():
            if value != max_count:
                f_dict.pop(key)
    return sorted(f_dict.keys())

print find_most_frequent('Hello,Hello, my dear!')
print find_most_frequent('to understand recursion you need first to understand recursion...')
print find_most_frequent('Mom! Mom! Are you sleeping?!!!')
print find_most_frequent('')