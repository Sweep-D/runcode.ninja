#!/usr/bin/env python3
import pathlib
import sys
import os
import hashlib
import glob

fileString = []
sha1String = []
megaHash = ""

# Pathlib is used instead of glob because it has glob function and also allows for showing hidden files.
# Loop through the path that has been passed
'''
for filename in glob.iglob("**/*.txt", recursive=True):
    files = os.path.basename(filename)
    fileString.append(files)
fileString.sort()
'''
for filename in pathlib.Path(sys.argv[1]).rglob("**/*"):
    files = os.path.basename(str(filename))
    if filename.is_file():
        fileString.append(files)
fileString.sort()  # sort the string array list.

# Loop through the string array list and hash each item into another list.
for filename in fileString:
    encodeFile = hashlib.sha1(filename.encode())  # Need to encode the line first before it will accept it.
    encrypt = encodeFile.hexdigest()
    sha1String.append(encrypt)

# Combine all hashes into one hash.
for filehash in sha1String:
    megaHash += filehash

encodeFile = hashlib.sha1(megaHash.encode())
encrypt = encodeFile.hexdigest()
print(encrypt)
