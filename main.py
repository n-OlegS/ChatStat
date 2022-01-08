from modules import *
import os.path

path = str(input("Enter path to text file: "))
clean_path = os.path.dirname(os.path.abspath("res/clean.txt")) + "/clean.txt"
stat_path = os.path.dirname(os.path.abspath("res/stat.txt")) + "/stat.txt"

try:
    file = open(path, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()

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


gen_clean_file(data, clean_file)
gen_stat_file(data, stat_file)
write_csv()

file.close()
clean_file.close()
stat_file.close()
