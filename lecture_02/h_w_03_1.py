num = float(input("Введите 5 значное число: "))
result = int(num % 10 * 10000 + num // 10 % 10 * 1000 + num // 100 % 10 * 100 + num // 1000 % 10 * 10 + num // 10000 % 10 * 1)
print(result)