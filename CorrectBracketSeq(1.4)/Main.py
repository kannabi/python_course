def is_opening(v):
    return v == '(' or v == '{' or v == '['


def is_pair(a, b):
    return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')


def is_correct_sequence(seq):
    stack = []

    if len(seq) == 0:
        return True

    if not is_opening(seq[0]):
        return False

    for iter in seq:
        if is_opening(iter):
            stack.append(iter)
        elif len(stack) > 0 and is_pair(stack[len(stack) - 1], iter):
            stack.pop()
        else:
            return False

    return False if len(stack) else True


n = int(input())

i = 0
seq_array = []

while i < n:
    i += 1
    seq_array.append(list(input()))

for it in seq_array:
    print('yes') if is_correct_sequence(it) else print('no')
