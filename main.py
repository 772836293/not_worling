from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
#from datetime import date # мусор
from nums_from_string import get_nums

root = Tk() # ??
root.geometry()


class Person:
    def __init__(self, FIO, Gender, age):
        self.__FIO = FIO
        self.__Gender = Gender
        self.__age = age

    #def str(self):
        #return (f'{self._FIO}',f'{self.Gender}',f'{self._age}')

    def get_FIO(self):
        return self.__FIO

    def get_Gender(self):
        return self.__Gender

    def set_FIO(self, FIO):
        self.__FIO = FIO

    def set_Gender(self, Gender):
        self.__Gender = Gender

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age


root.title("test")
'''
root.FIO_label = ttk.Label(text="ФИО")
root.FIO_label.grid(row=0, column=0)
root.FIO_entry = ttk.Entry()
root.FIO_entry.grid(row=0, column=1)

root.Gender_label = ttk.Label(text="Гендер")
root.Gender_label.grid(row=1, column=0)
root.Gender_entry = ttk.Entry()
root.Gender_entry.grid(row=1, column=1)

root.age_label = ttk.Label(text="Возраст")
root.age_label.grid(row=0, column=2)
root.age_entry = ttk.Entry()
root.age_entry.grid(row=0, column=4)

'''

root.tree = ttk.Treeview(columns=('FIO', 'Gender', 'age'))

root.tree.column("#0", width=0,  stretch=NO)

root.tree.heading("#0",text="",anchor=CENTER)
root.tree.heading('#1', text="ФИО")
root.tree.heading('#2', text="Гендер")
root.tree.heading('#3', text="Возраст")
root.tree.grid(row=0,column = 0,  columnspan = 3)




#ysb = ttk.Scrollbar('' ,orient = tk.VERTICAL, command = root.tree.yview)
#root.tree.configure(yscroll = ysb.set)
#ysb.grid(row = 4, column = 1, sticky=tk.N + tk.S)


list = []
i = -1
first = 0

'''
def insert_data():
    # humans = [Person(f"fio_{i}", f"gender_{i}", f"age_{i}")]
    #list.append(Person(root.FIO_entry.get(), root.Gender_entry.get(), root.age_entry.get()))
    root.tree.insert('', 'end', values=(root.FIO_entry.get(), root.Gender_entry.get(), root.age_entry.get()))
    global i
    i = i + 1

    # print(i)
    # print(first)
'''

def window_to_add():
    new_window = Toplevel()
    new_window.geometry("800x600")

    FIO_label = ttk.Label(new_window, text="ФИО")
    FIO_label.grid(row=0, column=0)
    FIO_entry = ttk.Entry(new_window)
    FIO_entry.grid(row=0, column=1)

    Gender_label = ttk.Label(new_window,text="Гендер")
    Gender_label.grid(row=1, column=0)
    Gender_entry = ttk.Entry(new_window)
    Gender_entry.grid(row=1, column=1)

    age_label = ttk.Label(new_window,text="Возраст")
    age_label.grid(row=0, column=2)
    age_entry = ttk.Entry(new_window)
    age_entry.grid(row=0, column=3)

    def add_data():
        list.append(Person(FIO_entry.get(), Gender_entry.get(), age_entry.get()))
        root.tree.insert('', 'end', values=(FIO_entry.get(), Gender_entry.get(), age_entry.get()))
        global i
        i = i + 1


    button_add = Button(new_window, text="Добавить",command=add_data)
    button_add.grid(row=5, column = 2)
    button_cancel = Button(new_window, text="Отмена",command = new_window.destroy)
    button_cancel.grid(row=5, column = 3)

def delete_data():
    selected_item = root.tree.selection()
    if not selected_item:
        print('Не выбрана строка')
    else:
        z = root.tree.index(selected_item)
        print('Индекс полчил')
        root.tree.delete(selected_item)
        if z != 0:
            z - 1
        print(z)
        #k = get_nums(selected_item[0])
        #s = k[0] - 1
        print(list)
        # num_len = len(list)
        # if num_len == s:
        #    list.pop(num_len)
        list.pop(z)
        print(list)

    '''
    global first,second
    second = 0
    adm = -1
    if adm>second:
        first = i
        adm = -100
        if i>first:
            first = i
    '''


    # list.pop()
    # print(selected_item)
    # print(type(get_nums(selected_item[0])))
    # print(type(selected_item[0]))


def edit_data():
    selected_item = root.tree.selection()
    if not selected_item:
        print('Не выбрана строка')
    else:
        z = root.tree.index(selected_item)
        print('Индекс полчил')
        #k = get_nums(selected_item[0])
        #s = k[0] - 1

        new_window = Toplevel()
        new_window.geometry("800x600")

        FIO_label = ttk.Label(new_window, text="ФИО")
        FIO_label.grid(row=0, column=0)
        FIO_entry = ttk.Entry(new_window)
        FIO_entry.grid(row=0, column=1)

        Gender_label = ttk.Label(new_window, text="Гендер")
        Gender_label.grid(row=1, column=0)
        Gender_entry = ttk.Entry(new_window)
        Gender_entry.grid(row=1, column=1)

        age_label = ttk.Label(new_window, text="Возраст")
        age_label.grid(row=0, column=2)
        age_entry = ttk.Entry(new_window)
        age_entry.grid(row=0, column=3)

        selected = root.tree.focus()
        values = root.tree.item(selected, 'values')

        FIO_entry.insert(0, values[0])
        Gender_entry.insert(0, values[1])
        age_entry.insert(0, values[2])

        def select_record():
            FIO_entry.delete(0,END)
            Gender_entry.delete(0,END)
            age_entry.delete(0,END)

            selected = root.tree.focus()

            values = root.tree.item(selected, 'values')

            FIO_entry.insert(0,values[0])
            Gender_entry.insert(0,values[1])
            age_entry.insert(0,values[2])

        def update_record():
            selected = root.tree.focus()
            root.tree.item(selected,values=(
            FIO_entry.get(), Gender_entry.get(), age_entry.get()))

            FIO_entry.delete(0,END)
            Gender_entry.delete(0,END)
            age_entry.delete(0,END)

            list.insert(z, Person(FIO_entry.get(), Gender_entry.get(), age_entry.get()))

        button1 = Button(new_window, text="Выбрать запись", command = select_record)
        button2 = Button(new_window, text="edit", command = update_record)
        button1.grid(row = 4,column = 3)
        button2.grid( row = 5, column = 4)

        #root.tree.item(selected, values=(
        #    root.FIO_entry.get(),root.Gender_entry.get(), root.age_entry.get()))


        #x = list[z]
        #print(type(x))
        #print(list[z].__)
        #root.tree.item(selected_item,
        #          values=(root.FIO_entry.get(), root.Gender_entry.get(), root.age_entry.get()))


root.inset_data = ttk.Button(text="insert", command = window_to_add)
root.inset_data.grid(row=2,column = 0)

root.delete_data = ttk.Button(text="delete", command=delete_data)
root.delete_data.grid(row=2,column = 1)

root.edit_data = ttk.Button(text="edit", command=edit_data)
root.edit_data.grid(row=2,column = 2)

"""insert_data()
print(humans)
insert_data()
print(list)"""

root.mainloop()