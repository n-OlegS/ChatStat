# немного говно кода
a = str(input("Enter path to text file: "))

def count_words():
    chat = open('chat1.txt', 'r')

    count = 0
    for line in chat:
        count = count + 1
    print('Number of lines in the file:', count)

    chat.close()


count_words()

# счетчик пробелов в строке
# i = 0
# line = chat.readline()
# i = line.count(' ')
# print(i + 1)