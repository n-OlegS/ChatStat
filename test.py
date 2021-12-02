from emoji import  *

def count_words(path):
    a = open(path, 'r')
    text = a.read()
    return text.count(' ') + 1
    a.close()

print(count_words('/Users/ula/PycharmProjects/Projectneolegs/ChatStat/clean.txt'))