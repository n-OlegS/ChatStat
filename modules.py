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
    data = file.readlines()
    i = 0

    if inp_line != -1:
        line = inp_line
    else:
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

    return [minute, hour, day, month, year, user]

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

stat_file = open("/ChatStat/res/stat.txt", "r")
clean_file = open("/ChatStat/res/clean.txt", "r")

#print(str(raw_char(clean_file)) + "\n" * 2)
#print(str(count_words(clean_file)) + "\n" * 2)
#print(str(common_word(clean_file)) + "\n" * 2)
#print(messages_per_user(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/stat.txt", "r")))

clean_file.close()
stat_file.close()