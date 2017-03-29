with open("input.txt", 'r') as content_file:
    content = content_file.read().split(" ")

length = len(content)
for i in range(length):
    content.extend(content.pop(i).split('\n'))

fout = open("output.txt", "w")

for it in content:
    it = it.strip("\n")
    if it[0:8] == "https://" or it[0:4] == "www.":
        print(it)
