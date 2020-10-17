#!/usr/bin/env python3
import sys
import pathlib
import os
import hashlib


fileHashTable = [[], []]
fileName = []
fileHash = []
megaHash = ""


def shaHashFile(shaHash):  # Generate hash for a file.
    file = shaHash
    file_hash = hashlib.sha1()
    BLOCK_SIZE = 65536

    with open(file, 'rb') as hashingFile:
        readFile = hashingFile.read(BLOCK_SIZE)
        while len(readFile) > 0:
            file_hash.update(readFile)
            readFile = hashingFile.read(BLOCK_SIZE)
    return file_hash.hexdigest()


# Pathlib is used instead of glob because it has glob function and also allows for showing hidden files.
for filename in pathlib.Path(sys.argv[1]).rglob("**/*"):
    if filename.is_file():
        fileHashTable[0].append(str(filename))
        fileHashTable[1].append(str(shaHashFile(filename)))

for fname, fhash in zip(fileHashTable[0], fileHashTable[1]):
    fileName.append(os.path.basename(fname))  # get just the filename and submit append into array.
    fileHash.append(fhash)  # append the filehash to the filehash array.

# Sort the two arrays in relation to each other. Using zip.
fileName, fileHash = zip(*sorted(zip(fileName, fileHash)))

# Assume that zip worked properly, combine sorted filehash array into one hash.
for filehash in fileHash:
    megaHash += filehash

finalHash = hashlib.sha1(megaHash.encode()).hexdigest()  # one last sha1hash on the generated megahash.
print(finalHash)
