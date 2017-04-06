with open("input.txt") as fin:
    n = fin.readline()
    for k in range(int(n)):
        data = tuple(filter(lambda x: x.isalpha(), list(fin.readline().lower())))
        answer = "yes"
        for i in range(len(data)):
            if data[i] != data[-(i + 1)]:
                if data[i] == 'е' and data[-(i + 1)] == 'ё':
                    continue
                if data[i] == 'ё' and data[-(i + 1)] == 'е':
                    continue
                answer = "no"
        print(answer)
