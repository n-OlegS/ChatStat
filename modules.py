def raw_char(input_file):
    return (len(input_file))

def count_lines(file):
    line_count = 0

    for _ in file.readlines():
        line_count += 1

    return(line_count)
