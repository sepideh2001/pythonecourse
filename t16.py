lst = [3,5,4,-1,0]
def count_evens(lst):
    evens_num = 0
    for i in lst:
        if i % 2 ==0:
            events_num = evens_num + 1
    print(events_num)
count_evens(lst)