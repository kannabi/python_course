import sys
# import no_standard_sort


def foo(a, b):
    l = a
    r = b
    med = arr[int((l + r) / 2)]

    while l <= r:
        while arr[l] < med:
            l += 1
        while arr[r] > med:
            r -= 1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    if a < r:
        foo(a, r)
    if b > l:
        foo(l, b)


# fin = open("input.txt")

arr = [int(x) for x in sys.stdin.readline().split()]

if len(arr) != 0:
    foo(0, len(arr) - 1)

# print(' '.join(arr))
res = str(arr[0])
it = 1
while it < len(arr):
    res += ' ' + str(arr[it])
    it += 1

print(res)
