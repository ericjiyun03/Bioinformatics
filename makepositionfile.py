with open("Human_AG_all_hg19.txt", "r") as f:
    f.readline()
    newlines = []
    for line in f.readlines():
        items = line.strip().split()
        newlines.append("%s:%s-%s\n"%(items[0], int(items[1]), int(items[1])))

with open("position_HG19.txt", "w") as f:
    f.writelines(newlines)



