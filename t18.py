lst = [5, 3, 1]
def next_number(lst):
    max = 0
    num = 0
    for i in lst:
        if i > max:
            max = i
    for i in range(1, max + 1):
        if i not in lst:
            return i
    return max + 1
print(next_number(lst))