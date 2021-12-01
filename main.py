import os.path

path = str(input("Enter path to text file: "))
c = 0

try:
    file = open(path, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()

def clean_up_file(raw_file, cleaned_file):
    for line in raw_file.readlines():
        new_line = line[:line.find(":")]
        newer_line = new_line[:new_line.find(":")]

        cleaned_file


try:
    clean_path = os.path.dirname(os.path.abspath("clean.txt"))
    clean_file = open(clean_path, 'r')
except FileNotFoundError:
    clean_file = open("clean.txt", "x")




def count_lines():
    line_count = 0

    for line in file.readlines():
        line_count += 1

    return(line_count)

