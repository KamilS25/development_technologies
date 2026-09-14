a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

try:
	result = a / b
except Exception:
	print("Деление на ноль запрещено")

print("Деление чисел:", result)