def file_search(folder, filename):
    path = ''
    for _file in folder:
#        if str(_file)[0] == '[':
        if isinstance(_file, list):
            sub_folder = file_search(_file, filename)
            if sub_folder:
                path += folder[0] + '/' + sub_folder
        elif _file == filename:
            path += folder[0] + '/' + _file
    return [False, path][len(path) > 0]

print file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me')
