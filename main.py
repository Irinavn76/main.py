# Сложение
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Введите первое число:", num1)
    print("Введите второе число:", num2)
    result = num1 + num2
except:
    print("Ошибка:Введенно неверное значение")
else:
    print(f"Результат сложения: {result}")


# Вычитание
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Введите первое число:", num1)
    print("Введите второе число:", num2)
    result = num1 - num2
except:
    print("Ошибка:Введенно неверное значение")
else:
    print(f"Результат вычитания {result}")


# Умножение
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 * num2
    print("Введите первое число:", num1)
    print("Введите второе число:", num2)
except:
    print("Ошибка:Введенно неверное значение")
else:
    print(f"Результат умножения: {result}")


# Деление
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
    print("Введите первое число:", num1)
    print("Введите второе число:", num2)
except:
    print("Ошибка:Введено неверное значение")
else:
    print(f"Результат деления: {result}")
