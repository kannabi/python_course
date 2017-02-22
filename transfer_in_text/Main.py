text = ''

step = int(input()) - 1

fin = open("input.txt")
# print(step)
for i in fin:
    text += i

i = step
SPACE = ' '
aim = 0
END_OF_LINE = '\n'
NOT_FOUND = -1

print(len(text))

while i < len(text):
    aim = text.rfind(END_OF_LINE, i + 1, i + step)

    if aim != NOT_FOUND:
        i = aim
        aim = NOT_FOUND
        continue

    if text[i] != SPACE and text[i] != END_OF_LINE:
        aim = text.find(SPACE, i)
        if aim == -1:
            exit()
        text = text[0: aim] + '\n' + text[aim + 1: len(text)]
        i = aim
    else:
        text = text[0: i] + '\n' + text[i + 1: len(text)]
    i += step


print(text)
