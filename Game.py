import random#Модули
x = random.choice(range(1 ,20))#Вызов модуля
print("Введите число:")
while True:
    z = int(input())#Сама игра в ввиде условный операторов
    if z < x:
        print("Заданое число меньше")
    if z > x:
        print("Заданое число больше")
    if z == x:
        print("Вы угадали!")
        break
    if z < 1:
        print("Число не в диапазоне!")
    if z > 20:
        print("Число не в диапазоне!")
        
