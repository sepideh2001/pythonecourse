def matrix(line, column):
    result = []
    for i in range(line):
        partial_result = []
        for i in range(column):
            partial_result.append(1)
        result.append(partial_result)
    return result
m = matrix(6, 9)
for i in m:
    print(i)
m[2][4] = 0
for i in m:
    print(i)
            

