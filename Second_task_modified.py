# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.  (ДЗ 2.1)

a = float(input("введите вещественное число: "))
print(sum(map(int, str(a).replace('.', '').replace('-', ''))))