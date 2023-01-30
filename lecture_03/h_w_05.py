lst = [1, 2, 3, 4, 5, 6]
a = len(lst)
if a % 2 == 0:
    x = a // 2
    first = [lst[:x]]
    last = [lst[x:]]
    fl = first + last
    print(fl)
else:
    x = a // 2 + 1
    first = [lst[:x]]
    last = [lst[x:]]
    fl = first + last
    print(fl)
