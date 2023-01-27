# Простой калькулятор.
a = int(input("Введите первое число: "))
b = input("Введите действие: ")
c = int(input("Введите вторе число: "))
if b == '/':
    if c == 0:
        print("Деление на ноль не допустимо!")

    d = a / c
    print("Равно")
    print(d)
elif b == '*':
    d = a * c
    print("Равно")
    print(d)
elif b == '+':
    d = a + c
    print("Равно")
    print(d)
elif b == '-':
    d = a - c
    print("Равно")
    print(d)






