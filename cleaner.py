dirty = open('dirty.txt', 'r', encoding='utf8')
clean = open('clean.txt', 'a', encoding='utf8')
lines = dirty.readlines()
for i in range(len(lines)):
    if '-' in lines[i]:
        clean.writelines(lines[i])
clean.close()
