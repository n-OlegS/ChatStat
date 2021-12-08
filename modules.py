from emoji import UNICODE_EMOJI_ENGLISH


def raw_char(file):
    return (len(file))


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


def standarize_stat(file, line_num):
    data = file.readlines()
    i = 0
    line = ""

    for line_check in data:
        if i == line_num - 1:
            line = line_check
        i += 1

    i = 0
    while line[i] not in [".", "/"]:
        i += 1

    day = 0
    month = 0
    year = 0

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