from modules import *

path = str(input("Enter path to text file: "))
c = 0

try:
    file = open(path, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()

lines = file.readlines()

for i in lines:
    c += 1

print(c)
