num = []
count =0
tot = 0 
big = None 
small = None 

while True: 
    numbers = float(input('enter a positive number, negetive to stop: '))
    tot += numbers
    count += 1
    if big is None or numbers > big: 
        big = numbers 
    if small is None or numbers < small: 
        small = numbers 
    if numbers < 0: 
        break 
avg = tot / count

print('sum is:', tot)
print('average is:', avg)
print('maximum is:', big)
print('minimum is:', small)