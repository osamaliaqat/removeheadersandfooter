def remove_head_foot():
    header = 10
    footer = 15
    buffer = []

    with open('4ebbbebb46fab13cadcac3a1b0041b4c.txt', 'r') as f:
        for _ in range(header):
            f.readline()

        for _ in range(footer):
            buffer.append(f.readline())

        for line in f:
            buffer.append(line)
            line = buffer.pop(0)

            # do stuff to line
            print(line)


remove_head_foot()