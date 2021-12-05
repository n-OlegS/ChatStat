


a = {}
max_count = 0
max_value = ''

for i in range(len(a)):
    key = list(a)[i]

    if a[key] > max_count:
        max_value = list(a)[i]
        max_count = a[key]