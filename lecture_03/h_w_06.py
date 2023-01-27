num = []
if len(num) > 0:
    num_last = num.pop()
    num.insert(0, num_last)
    print(num)
else:
    print(num)
