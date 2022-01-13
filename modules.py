import csv, datetime
import plotly.graph_objs as go
import os

from termcolor import colored
from emoji import UNICODE_EMOJI_ENGLISH


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


def gen_clean_file(data, cleaned_file):
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


def gen_stat_file(data, final_stat_file):
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
                if not final_line[test_validity] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "/"] \
                        or final_line[:3] == "...":
                    skip = True
            except IndexError:
                skip = True

        if not skip:
            try:
                stat_file_data[i] = final_line + "\n"
            except IndexError:
                final_stat_file.write(str(final_line) + "\n")
        # else:
        # print("Rejected", str(i) + ":", final_line[:15] + "...")

        i += 1


def raw_char(file):
    l = 0
    for line in file:
        l += len(line)

    return str(l)


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
        if letter in [" ", "\n", ".", ",", "!", ":", ')', '('] or letter in UNICODE_EMOJI_ENGLISH and acc not in [
            'omitted>', '<Media']:
            add_word(acc)
            acc = ""
        else:
            acc += letter

    words = dict(sorted(words.items(), key=lambda item: item[1]))

    print('Top 10 common words:\n')

    for i in range(10):
        print(colored(
            list(words.items())[len(words) - i - 1][0] + " : " + str(list(words.items())[len(words) - i - 1][1]),
              'blue'))

    print('\n')


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

    out = "\nMessages per user:\n"
    for key in getKeyList(mpu):
        out += str(key) + " : " + str(mpu[key]) + "\n"

    return (out)


def write_csv():
    with open("res/data.csv", "w") as csv_file, open("res/stat.txt", "r") as stat_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Month', 'Day', 'Year', "Hour", "Minute", "User"])

        for line in stat_file.readlines():
            data = standarize_stat(0, 0, line)
            writer.writerow(data)


def graph_mpdow():
    try:
        stat_file = open("res/stat.txt", "r")
    except:
        return

    users = {}
    data = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for line in stat_file:
        stats = standarize_stat(0, 0, line)
        user = stats[5]
        dow = datetime.date(int(stats[0]), int(stats[1]), int(stats[2])).weekday()

        if user not in users:
            users[user] = {}
            for i in range(7):
                users[user][i] = 0

        if dow not in users[user]:
            users[user][dow] = 1
        else:
            users[user][dow] += 1

    base = [0] * 7

    for user in getKeyList(users):
        data.append(go.Bar(
            name=user,
            x=days,
            y=getValueList(users[user]),
            base=base,
            offsetgroup=0
        ))

        base = addLists(base, getValueList(users[user]))

    fig = go.Figure(
        data,
        layout=go.Layout(
            title="Messages per weekday",
            yaxis_title="Message count"
        )
    )

    html_file = open("res/htmls/mpdow.html", "r+")
    html_file.truncate()
    fig.write_html(html_file, auto_open=False)
    html_file.close()
    stat_file.close()


def addLists(x, y):
    if not len(x) == len(y):
        print("Addlists Error, terminating...")
        quit()
    else:
        c = []
        for i in range(len(x)):
            c.append(int(x[i]) + int(y[i]))

        return c


def graph_mph():
    try:
        stat_file = open("res/stat.txt", "r")
    except:
        return

    users = {}
    data = []

    for line in stat_file:
        stats = standarize_stat(0, 0, line)
        hour = int(stats[3])
        user = str(stats[5])

        while hour >= 24: hour -= 24
        hour = str(hour)

        if user not in users:
            users[user] = {}
            for i in range(24):
                users[user][str(i)] = 0

        if hour not in users[user]:
            users[user][hour] = 1
        else:
            users[user][hour] += 1

    base = [0] * 24

    for i in getKeyList(users):
        data.append(go.Bar(
            name=i,
            x=getKeyList(users[i]),
            y=getValueList(users[i]),
            base=base,
            offsetgroup=0
        ))

        base = addLists(base, getValueList(users[i]))

    fig = go.Figure(
        data,
        layout=go.Layout(
            title="Messages per hour of day",
            yaxis_title="Number of messges"
        )
    )

    html_file = open("res/htmls/mph.html", "r+")
    html_file.truncate()
    fig.write_html(html_file, auto_open=False)
    html_file.close()
    stat_file.close()


def graph_mpd():
    try:
        stat_file = open("res/stat.txt", "r")
    except:
        return

    users = {}
    data = []
    dates = []

    for line in stat_file:
        stats = standarize_stat(0, 0, line)
        date = str(standarize_stat(0, 0, line)[0]) + "-" + str(standarize_stat(0, 0, line)[1]) + "-" + str(
            standarize_stat(0, 0, line)[2])
        user = str(stats[5])

        if user not in users:
            users[user] = {}
            for date in dates:
                users[user][date] = 0

        if date not in dates:
            dates.append(date)
            for usr in getKeyList(users):
                users[usr][date] = 0
        else:
            users[user][date] += 1

    base = [0] * len(dates)

    for user in getKeyList(users):
        data.append(go.Bar(
            name=user,
            x=dates,
            y=getValueList(users[user]),
            base=base,
            offsetgroup=0
        ))

        base = addLists(base, getValueList(users[user]))

    fig = go.Figure(
        data,
        layout=go.Layout(
            title="Messages per date",
            yaxis_title="Message count"
        )
    )

    html_file = open("res/htmls/mpd.html", "r+")
    html_file.truncate()
    fig.write_html(html_file, auto_open=False)
    html_file.close()
    stat_file.close()

# print(str(raw_char(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/res/clean.txt", "r"))) + "\n" * 2)
# print(str(count_words(clean_file)) + "\n" * 2)
# print(str(common_word(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/res/clean.txt", "r"))) + "\n" * 2)
# print(messages_per_user(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/res/stat.txt", "r")))
