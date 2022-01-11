from modules import *
import os.path, time

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

#UI start
graph_mpdow()
graph_mph()
graph_mpd()

print("Total characters typed:", str(raw_char(open("res/clean.txt", "r"))))
print("Total lines:", count_lines(open(path, "r")))
print("Total words:", count_words(open("res/clean.txt", "r")))
print(messages_per_user(open("res/stat.txt", "r")))
print("See messages per weekday: file://" + os.path.abspath("res/htmls/mpdow.html"))
print("See messages per date: file://" + os.path.abspath("res/htmls/mpd.html"))
print("See messages per hour of day: file://" + os.path.abspath("res/htmls/mph.html"))
#UI end
