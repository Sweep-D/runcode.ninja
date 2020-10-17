#!/usr/bin/env python3
from os import walk as w
from sys import argv
from hashlib import sha1
files = {}
for line in w(str(argv[1])):
    for f in line[2:][0]:
        if '.txt' in f:
            files[f] = {'path': str(line[0]) + '/'}
            with open(str(files[f]['path'] + f), 'r') as open_file:
                files[f]['sha1'] = sha1(open_file.read().encode()).hexdigest()

hashes = "".join(str(files[h]['sha1']) for h in sorted(files.keys()))
print(sha1(hashes.encode()).hexdigest())
