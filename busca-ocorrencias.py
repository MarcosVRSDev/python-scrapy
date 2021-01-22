import string
import re
import json
import os

Path = "./arquivos/"
filelist = os.listdir(Path)

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

d = dict()

for i in filelist:
    with open(Path + i, "r") as text:
        for line in text:
            line = re.sub(cleanr, '', line)

            line = line.strip()

            line = line.lower()

            line = line.translate(line.maketrans("", "", string.punctuation))

            words = line.split(" ")

            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1

for key in (dict(sorted(d.items(), key=lambda item: item[1]))).__reversed__():
    if(key == "" ):
        d.pop(key)
    elif(key.isnumeric()):
        d.pop(key)

sorted_dict = dict(sorted(d.items(),
                          key=lambda item: item[1],
                          reverse=True))

with open("data.json", "w") as outfile:
    json.dump(sorted_dict, outfile, indent=4)
