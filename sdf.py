import random#Для наглядности вызываем модуль рандом
def quickly_sort(list):
    final_list = []#Сюда выводим итоговый список - результат роботы
    while len(list) != 0:#Вызываем рекурсию,которая работает до момента опустошения параметра list
        min_element = min(list)#При помощи функции min определяем минимальное число в списке
        index_of_element = list.index(min_element)#Потом определяем индекс этого минимального числа
        final_list.append(min_element)#Добавляем само минимальное число в итоговый список
        del list[index_of_element]#И в конце рекурентного случая - удаляем текущий минимальный элемент из параметра list
        if len(list) == 0:#В самом конце рекурсии,когда она дошла до базового случая - выводим результат на экран
            print(final_list)
a = list(range(0, 1001))#Пример списка из 1000 чисел
random.shuffle(a)#Функция shuffle перемешивает список
print(a)#Вывод списка до работы алгоритма
quickly_sort(a)#После работы алгоритма































































#Реализовать самостоятельно все алгоритмы из книги "Грокаем алгоритмы"даже если они уже были пройденный!Повторения-мать учения