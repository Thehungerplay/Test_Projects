from tkinter import *
dictionary = {'Swaroop': 'Dictionaries street,12', 'Jon': 'Bebera street,19', 'Lin': 'SuperBebra street,4',
              'Robin': 'Funny street,111', 'Erik': 'Young street,228'}
def read_dict():
    print('Cписок жителей улицы("Человек","Адрес") - ', dictionary.items())
def delete_dict():
    dictionary.clear()
    print('Книга очищена', dictionary)
def delete_needing_element_in_dict():
    try:
        del_string = input('Введите человека,которого нужно удалить из вашей книги - ')
        del dictionary[del_string]
        print('Ваша изменённая книга', dictionary)
    except Exception:
        print('Этого человека нет в книге')
        del_string = input('Введите человека,которого нужно удалить из вашей книги - ')
        del dictionary[del_string]
        print('Изменнёная книга', dictionary)
def seek_element_in_dict():
    str1 = input('Введите имя человека - ')
    print(dictionary.get(str1, ['Такого человека нет']))
def fromkeys_dict():
    person = input('Введите ФИО человека - ')
    information_of_person = input('Введите его контактный данные - ')
    dictionary.__setitem__(person, information_of_person)
    print('Ваш человек добавлен в книгу', dictionary)
def changed_dict():
    try:
        old_key = input('Введите человека для исключения из книги - ')
        new_key = input('Введите нового человека - ')
        dictionary[new_key] = dictionary.pop(old_key)
        print('Изменённая книга', dictionary)
    except Exception:
        print('Такого человека нет в книге')
        old_key = input('Введите человека для исключения из книги - ')
        new_key = input('Введите нового человека - ')
        dictionary[new_key] = dictionary.pop(old_key)
        print('Изменённая книга', dictionary)
def save_dict():
    print('Ваша книга сохраненна в файл - adress book(Человек : Адресс)')
    with open('adress book', 'w') as r:
        str_dictionary = str(dictionary)
        r.write(str_dictionary)
        r.close()
tk = Tk()
tk.title('Книга')
tk.geometry('900x900')
tk.resizable(height=False, width=False)
lab = Label(tk, text='Блок возможностей', font='Gadugi')
lab.place(x=0, y=0)
btn = Button(tk, text='Read', command=read_dict)
btn.place(x=100, y=100)
btn1 = Button(tk, text='Delete everything', command=delete_dict)
btn1.place(x=200, y=200)
btn2 = Button(tk, text='Delete', command=delete_needing_element_in_dict)
btn2.place(x=300, y=300)
btn3 = Button(tk, text='Seek', command=seek_element_in_dict)
btn3.place(x=400, y=400)
btn4 = Button(tk,  text='Fromkeys', command=fromkeys_dict)
btn4.place(x=500, y=500)
btn5 = Button(tk, text='Change', command=changed_dict)
btn5.place(x=600, y=600)
btn6 = Button(tk, text='Save', command=save_dict)
btn6.place(x=700, y=700)
tk.mainloop()