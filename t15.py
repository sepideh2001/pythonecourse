a = [3, -3, 5, 2, -1, 2]
def sum_positive(a):
    sum = 0
    for i in a:
        if i > -1:
            sum = sum + i
    print(sum)
sum_positive(a)