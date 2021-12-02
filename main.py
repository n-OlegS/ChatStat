from modules import *
import os.path

path = str(input("Enter path to text file: "))

try:
    file = open(path, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()


def clean_up_file(raw_file, cleaned_file):
    i = 0

    data = raw_file.readlines()
    clean_file_data = cleaned_file.readlines()

    for _ in data:
        line = data[i]
        new_line = line[line.find(":") + 1:]
        newer_line = new_line[(new_line.find(":") + 2):]

        try:
            clean_file_data[i] = newer_line
        except IndexError:
            cleaned_file.write(str(newer_line))

        i += 1


clean_path = os.path.dirname(os.path.abspath("clean.txt")) + "/clean.txt"

try:
    clean_file = open(clean_path, 'r+')
except FileNotFoundError:
    print("Creating  new clean file...")
    clean_file = open(clean_path, "x")
    clean_file.close()
    clean_file = open(clean_path, "r+")

clean_up_file(file, clean_file)

file.close()
clean_file.close()

#test
#хай бич король)