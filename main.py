from modules import *
from termcolor import colored
import os

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
    print(colored("Creating  new clean file...", 'yellow'))
    clean_file = open(clean_path, "x")
    clean_file.close()
    clean_file = open(clean_path, "r+")

try:
    stat_file = open(stat_path, 'r+')
except FileNotFoundError:
    print(colored("Creating  new stat file...", 'yellow'))
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

#UI start
graph_mpdow()
graph_mph()
graph_mpd()

char = "Total characters typed: " + str(raw_char(open("res/clean.txt", "r")))
lines = "Total lines: " + str(count_lines(open(path, "r")))
mpu = "Total words: " + str(count_words(open("res/clean.txt", "r")))

print(colored(char, 'green'))
print(colored(lines, 'green'))
print(colored(mpu, 'green'))
print(messages_per_user(open("res/stat.txt", "r")))
print("See messages per weekday: file://" + os.path.abspath("res/htmls/mpdow.html"))
print("See messages per date: file://" + os.path.abspath("res/htmls/mpd.html"))
print("See messages per hour of day: file://" + os.path.abspath("res/htmls/mph.html"))
#UI end


os.remove(clean_path)
os.remove(stat_path)
os.remove('res/data.csv')