import csv, datetime
import plotly.offline as py
import plotly.graph_objs as go

from emoji import UNICODE_EMOJI_ENGLISH


def raw_char(file):
    l = 0
    for line in file:
        l += len(line)

    return l


def count_lines(file):
    line_count = 0

    for _ in file.readlines():
        line_count += 1

    return (line_count)


def count_words(file):
    a = file
    text = a.read()
    return text.count(' ') + 1
    a.close()


def common_word(file):
    global words
    words = {}

    text = file.read()

    def add_word(word):
        if word not in ["-", " ", ""]:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    acc = ""

    for letter in text:
        if letter in [" ", "\n", ".", ",", "!", ":", ')', '('] or letter in UNICODE_EMOJI_ENGLISH:
            add_word(acc)
            acc = ""
        else:
            acc += letter

    max_count = 0
    max_value = ''

    for i in range(len(words)):
        key = list(words)[i]

        if words[key] > max_count:
            max_value = list(words)[i]
            max_count = words[key]
    return 'Word: ' + max_value + '\nCount: ' + str(max_count)


def search_word(file, s_word):
    text = file.read()
    return "Word: " + s_word + "\nAmount: " + str(text.count(s_word))


def standarize_stat(file, line_num, inp_line):
    i = 0

    if inp_line != -1:
        line = inp_line
    else:
        data = file.readlines()
        line = ""

        for line_check in data:
            if i == line_num - 1:
                line = line_check
            i += 1

    i = 0
    while line[i] not in [".", "/"]:
        i += 1

    user = line[line.find(" - ") + 3:line.find("\n")]

    if line[line.find(" - ") - 2:line.find(" - ")] == "PM":
        hour = int(line[line.find(" "):line.find(":")]) + 12
        minute = int(line[line.find(":") + 1:line.find(" PM")])

    elif line[line.find(" - ") - 2:line.find(" - ")] == "AM":
        hour = int(line[line.find(" "):line.find(":")])
        minute = int(line[line.find(":") + 1:line.find(" AM")])
    else:
        minute = line[line.find(" - ") - 2:line.find(" - ")]
        hour = line[line.find(" - ") - 5:line.find(" - ") - 3]

    if hour == 24:
        hour = 0

    if line[i] == ".":
        day = line[:i]
        line = line[i + 1:]
        i = line.find(".")
        month = line[:i]
        year = line[i + 1:line.find(",")]
    else:
        month = line[:i]
        line = line[i + 1:]
        i = line.find("/")
        day = line[:i]
        year = line[i + 1:line.find(",")]

    return [year, month, day, hour, minute, user]


def messages_per_user(file):
    mpu = {}
    i = 0
    for line in file.readlines():
        try:
            cur_sender = standarize_stat(file, i, line)[5]
        except IndexError:
            print("error")
            continue
        if cur_sender in mpu:
            mpu[cur_sender] += 1
        else:
            mpu[cur_sender] = 1

        i += 1

    return mpu


def write_csv():
    with open("res/data.csv", "w") as csv_file, open("res/stat.txt", "r") as stat_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Month', 'Day', 'Year', "Hour", "Minute", "User"])

        for line in stat_file.readlines():
            data = standarize_stat(0, 0, line)
            writer.writerow(data)


def graph_mpdow():
    mon, tue, wed, thur, fri, sat, sun = 0, 0, 0, 0, 0, 0, 0
    try:
        with open("res/stat.txt", "r") as stat_file:
            for line in stat_file:
                l = standarize_stat(0, 0, line)
                dow = datetime.date(int(l[0]), int(l[1]), int(l[2])).weekday()

                if dow == 0:
                    mon += 1
                elif dow == 1:
                    tue += 1
                elif dow == 2:
                    wed += 1
                elif dow == 3:
                    thur += 1
                elif dow == 4:
                    fri += 1
                elif dow == 5:
                    sat += 1
                else:
                    sun += 1

        trace = go.Bar(x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                       y=[mon, tue, wed, thur, fri, sat, sun])
        py.plot([trace])
    except:
        none = None

def getKeyList(d):
    keys = []
    for key in d.keys():
        keys.append(key)
    return keys

def getValueList(d):
    values = []
    for value in d.values():
        values.append(value)
    return values

def mph():
    try:
        with open("res/stat.txt", "r") as stat_file:
            hours = {}
            for i in range(24):
                hours[str(i)] = 0

            for line in stat_file:
                new_line = str(int(standarize_stat(0, 0, line)[3]))
                hours[new_line] += 1

            print(hours)
            trace = go.Bar(x=getKeyList(hours),
                           y=getValueList(hours))
            py.plot([trace])
    except:
        i = 0

graph_mpdow()
#mph()
# print(str(raw_char(clean_file)) + "\n" * 2)
# print(str(count_words(clean_file)) + "\n" * 2)
# print(str(common_word(clean_file)) + "\n" * 2)
# print(messages_per_user(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/stat.txt", "r")))
