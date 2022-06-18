main_list = ['Абрикос']#Хеш-функция(плохая, с множеством коллизий)добавляющая элементы в список по первой букве в слове.Example's word
words = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'#хотя это вовсе не хеш функция,ибо коллизий нет.For comfortable change alphabet,right to this string
                                          # и делается для массива,а не для хеша.Пример работы и кода
list_words = list(words)#Переформатируем в список алфавит
main_str = input('Введите ваше слово - ')
main_str1 = main_str.lower()#Для удобвства делаем слово с мал. буквы
list_main_str1 = list(main_str1)#Переформатируем в список
cut = list_main_str1[:1]#Делаем вырезку,чтобы была одна буква
str_cut = str(cut)#Переформатируем в строку
str_cut_r1 = str_cut.replace("[", '')#Из строк для проверки убираем все лишнее:скобки,кавычки
str_cut_r2 = str_cut_r1.replace(']', '')
str_cut_r3 = str_cut_r2.replace("'", '')
main_words = words.index(str_cut_r3)#Узнаем индекс первой буквы нашего слова
if str_cut_r3 in words:
    main_list.insert(main_words, main_str)
    print(main_list)#И в соответствии с алфавитом ставим слово в список на свое место

