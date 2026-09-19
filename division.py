a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


if b != 0:
	result = a / b
else:
	print("Деление на ноль запрещено")

print("Деление чисел:", result)