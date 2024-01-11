import os
from fnmatch import fnmatch

path_dir = "public"
save_match = []

for path, subdirs, files in os.walk(path_dir):
    for name in files:
        # print(os.path.join(path, name))

        print('Filename: {:<25} Match: {}'.format(
            name, fnmatch(name, '*.html')))

        if fnmatch(name, '*.html'):
            save_match.append(os.path.join(path, name))


print("-----------------")
print(save_match)
print("-----------------")


pathDir = "public"

for file in os.listdir(pathDir):

    dir_validate = (os.path.join(pathDir, file))
    isdir = os.path.isdir(dir_validate)
    print('Filename: {:<10} Match: {:<5} Folder: {}'.format(
        file, fnmatch(file, '*.css'), isdir))


print("-----------------")
