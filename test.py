
def count_words():
    line = input()
    i = 0
    for space in line:
        if space == " ":
            i += 1
        else:
            continue
    ans = i + 1
    return(ans)


count_words()
