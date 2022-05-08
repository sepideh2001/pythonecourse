lst = [ 'Iran', 'Zanjan', '098', '024']
def reverse(lst):
    lst2 = []
    for item in lst:
        lst2.insert(0, item)
    return lst2
print(reverse(lst))