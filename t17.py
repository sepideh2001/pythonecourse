lst = [10, 11, 12, 13, 14, 15]
num = 12
def print_big_enough(lst, num):
    sliced_lst = []
    for i in lst:
        if i >= num:
            sliced_lst += [i]
    print(sliced_lst)
print_big_enough(lst, num)