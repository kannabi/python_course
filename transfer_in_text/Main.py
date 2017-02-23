text = ''

fin = open("input.txt")
fout = open("output.txt", "w")
step = int(fin.readline()) + 1
for i in fin:
    text += i

i = 0
SPACE = ' '
END_OF_LINE = '\n'
NOT_FOUND = -1
aim = 0

while True:
    aim = text.rfind(END_OF_LINE, i + 1, i + step)

    if aim != NOT_FOUND:
        i = aim
        aim = NOT_FOUND
        continue

    i += step
    try:
        if text[i] == SPACE:
            text = text[0: i] + '\n' + text[i + 1: len(text)]
        elif text[i] == END_OF_LINE: # or not text[i].isalpha():
            continue
        else:
            aim = text.rfind(SPACE, i - step, i)
            if aim == NOT_FOUND:
                # raise IndexError
                continue
            text = text[0: aim] + '\n' + text[aim + 1: len(text)]
            i = aim
    except IndexError:
        break

fout.write(text)

fout.close()
