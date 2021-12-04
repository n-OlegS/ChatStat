from emoji import UNICODE_EMOJI_ENGLISH

def raw_char(input_file):
    return (len(input_file))

def count_lines(file):
    line_count = 0

    for _ in file.readlines():
        line_count += 1

    return(line_count)

def common_word(file):
    words = {}

    text = file.read()

    def add_word(word):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    acc = ""

    for letter in text:
        if letter in [" ", "\n", ".", ",", "!", ":"] or letter in UNICODE_EMOJI_ENGLISH:
            add_word(acc)
            acc = ""
        else:
            acc += letter

    return words

#print(common_word(open("/Users/oleg/PycharmProjects/chatstat/ChatStat/clean.txt", "r")))