from modules import *
import os.path

path = str(input("Enter path to text file: "))

try:
    file = open(path, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()


def clean_up_file(cleaned_file):
    i = 1

    clean_file_data = cleaned_file.readlines()

    for _ in data:
        try:
            line = data[i]
        except IndexError:
            break

        new_line = line[line.find(":") + 1:]
        newer_line = new_line[(new_line.find(":") + 2):]

        try:
            clean_file_data[i] = newer_line
        except IndexError:
            cleaned_file.write(str(newer_line))

        i += 1


def gen_stat_file(final_stat_file):
    i = 0

    stat_file_data = final_stat_file.readlines()

    for _ in data:
        line = data[i]
        final_line = ""
        first = line.find(":")
        final_line += line[:first] + ":"
        new_line = line[first + 1:]
        final_line += new_line[:new_line.find(":")]

        skip = False
        for test_validity in range(5):
            try:
                if not final_line[test_validity] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "/"]:
                    skip = True
            except IndexError:
                skip = True

        if not skip:
            try:
                stat_file_data[i] = final_line + "\n"
            except IndexError:
                final_stat_file.write(str(final_line) + "\n")
        else:
            print("Rejected:", final_line[:15] + "...")

        i += 1


clean_path = os.path.dirname(os.path.abspath("clean.txt")) + "/clean.txt"
stat_path = os.path.dirname(os.path.abspath("stat.txt")) + "/stat.txt"

try:
    clean_file = open(clean_path, 'r+')
except FileNotFoundError:
    print("Creating  new clean file...")
    clean_file = open(clean_path, "x")
    clean_file.close()
    clean_file = open(clean_path, "r+")

try:
    stat_file = open(stat_path, 'r+')
except FileNotFoundError:
    print("Creating  new stat file...")
    stat_file = open(stat_path, "x")
    stat_file.close()
    stat_file = open(stat_path, "r+")

data = file.readlines()

clean_up_file(clean_file)
gen_stat_file(stat_file)

file.close()
clean_file.close()
stat_file.close()

# test
# хай бич король)
