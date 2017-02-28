fin = open("input.txt")

p = float(fin.readline())

arr = [float(x) for x in fin.read().split()]

# arr = list(input())

for i in arr:
    if i == ' ':
        arr.remove(i)

res = 0

for i in arr:
    res += (abs(float(i)))**p

if p == 0:
    print(0)
else:
    print(res**(1/p))
