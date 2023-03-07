import os
import sys
import glob

if len(sys.argv) > 1:
    directories = sys.argv[1:]
else:
    directories = input("Enter directory paths separated by spaces: ").split(" ")

#Unicode RTLO Characters
blacklist = set(['\u200E', '\u200F', '\u202A', '\u202B', '\u202C', '\u202D', '\u202E', '\u2066', '\u2067', '\u2068', '\u2069', ])

for directory in directories:
    for filepath in glob.glob(f'{directory}/**/*', recursive=True):
        if any(char in blacklist for char in filepath):
            print(f"File '{filepath}' contains Unicode characters")
