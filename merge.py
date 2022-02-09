from modules import *
from termcolor import colored
import os.path

orig_path = str(input('Enter path of file to be merged into: '))
try:
    orig_file = open(orig_path, 'r')
except FileNotFoundError:
    print(colored('File not found...', 'red'))
    quit()

merge_path = str(input('Enter path of file to be merged: '))
try:
    merge_file = open(merge_path, 'r')
    merge_count_file = open(merge_path, 'r')
except FileNotFoundError:
    print(colored('File not found...', 'red'))
    quit()

c = 1
lines = count_lines(orig_file)
orig_file.seek(0)
last_line = ""

print(lines)

for line in orig_file.readlines():
    if c == lines:
        last_line = line
    c += 1

found = False

orig_file.close()
orig_file = open(orig_path, 'a')

for line in merge_file.readlines():

    if line == last_line:
        found = True
        continue

    if found:
        orig_file.write(line)
