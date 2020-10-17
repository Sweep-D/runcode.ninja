#!/usr/bin/env python
import sys

# Open the path that has been passed into the file
file = open(sys.argv[1], 'r')

# read data in the file
data = file.read()

# output to console.
print(data)
