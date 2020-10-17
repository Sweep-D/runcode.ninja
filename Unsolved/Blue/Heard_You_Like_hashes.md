# Directive

Yo, your boss heard you like hashes so they asked you to create a novel way to get a single hash for a directory full of subdirectories and files using hashes of each file. Essentially, they want you to look through all of the directories and subdirectories and collect all the files. Once they are all collected, sort by just the filename (0-9A-Za-z) and not the entire path, iterate over each file in a sorted fashion (0-9A-Za-z), and get the sha1 hash of each file. Combine all the hashes to create a mega hash and hash that hash. The output is a single sha1 hash. If any of the content in the directory changes, the final hash will also change. This gives you the means to quickly check the overall forensic integrity of a directory (or even an entire file system). The input will be a path to a file system to hash.

## Get a single Hash

1. Input will be a path to a file system to the hash. 
2. Parse all directories
3. Get files all in all directories
4. sort by filename (0-9A-Za-z)
5. Iterate over all files and generate sha1 hash of each file.
6. Combine all of those hashes into one mega hash
7. Hash the mega hash (sha1)
