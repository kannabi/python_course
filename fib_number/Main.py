n = int(input())
v0 = 0
v1 = 1
i = 1

while i < n:
    v2 = v1 + v0
    v0 = v1
    v1 = v2
    i += 1
if n != 0:
    print(v1)
else:
    print(0)
