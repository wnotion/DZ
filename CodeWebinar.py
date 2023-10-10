import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def search_records(self, name):
        name = ('%'+ name + '%')
        self.db.c.execute("""SELECT * FROM abc""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end',values=row) for row in self.db.c.fetchall()]
    
    def open_search_dialog(self):
        Search()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute("""DELETE FROM abc 
            WHERE id=?""", (self.tree.set(selection_item, '#1')))
            self.db.conn.commit()
            self.view_records()

    def update_record(self, name, tel, email):
        self.db.c.execute("""UPDATE abc SET name=?, tel = ?, email=?
        WHERE ID=?""", (name,tel, email,
                        self.tree.set(self.tree.selection()[0],'#1')))
        self.db.conn.commit()
        self.view_records()

    def open_update_dialog(self):
        Update()

    def records(self, name, tel, email):
        self.db.insert_data(name, tel, email)
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd = 2)
        toolbar.pack(side= tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='./Для Проекта Картинки/add.png')
        # создание кнопки добавления
        # command - функция по нажатию
        # bg - фон
        # bd - граница
        # compound - ориентация текста (tk.CENTER , tk.LEFT , tk.RIGHT , tk.TOP или tk.BOTTOM.)
        # image - иконка кнопки
        btn_open_dialog = tk.Button(toolbar, bg='#d7d8e0', bd=0, image=self.add_img, command=self.open_dialog)
        # упаковка и выравнивание по левому краю
        btn_open_dialog.pack(side=tk.LEFT)
        # Добавляем Treeview
        # columns - столбцы
        # height - высота таблицы
        # show='headings' скрываем нулевую (пустую) колонку таблицы
        self.tree = ttk.Treeview( columns=('ID', 'name', 'tel', 'email'), height=45, show='headings')

        # добавляем параметры колонкам
        # width - ширина
        # anchor - выравнивание текста в ячейке
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("name", width=300, anchor=tk.CENTER)
        self.tree.column("tel", width=150, anchor=tk.CENTER)
        self.tree.column("email", width=150, anchor=tk.CENTER)

        # подписи колонок
        self.tree.heading("ID", text='ID')
        self.tree.heading("name", text='ФИО')
        self.tree.heading("tel", text='Телефон')
        self.tree.heading("email", text='E-mail')


        # упаковка
        self.tree.pack(side=tk.LEFT)
        #создание кнопки изменения данных
        self.update_img = tk.PhotoImage(file='./Для Проекта Картинки/update.png')
        btn_edit_dialog = tk.Button(toolbar, bg='#d7d8e0',
                                    bd=0, image=self.update_img,
                                    command = self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)
        
        #создание кнопки удаление записи
        self.delete_img = tk.PhotoImage(file='./Для Проекта Картинки/delete.png')
        btn_delete = tk.Button(toolbar, bg='#d7d8e0', bd=0,
                               image=self.delete_img,
                               command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)
        #создание кнопки поиска
        self.search_img = tk.PhotoImage(file='./Для Проекта Картинки/search.png')
        btn_search =tk.Button(toolbar, bg='#d7d8e0',bd=0,
                              image=self.search_img,
                              command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)
        #кнопка обновления
        self.refresh_img = tk.PhotoImage(file='./Для Проекта Картинки/refresh.png')
        btn_refresh = tk.Button(toolbar, bg='#d7d8e0', bd=0,
                                image= self.refresh_img,
                                command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)



    def open_dialog(self):    
            Child()
    # вывод данных в виджет таблицы
    def view_records(self):
        # выбираем информацию из БД
        self.db.c.execute('''SELECT * FROM abc''')
        # удаляем все из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]
        # добавляем в виджет таблицы всю информацию из БД
        [self.tree.insert('', 'end', values=row)
         for row in self.db.c.fetchall()]


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
        

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x220')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        label_name = tk.Label(self, text='ФИО:')
        label_name.place(x=50, y=50)
        label_select = tk.Label(self, text='Телефон')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='E-mail')
        label_sum.place(x=50, y=110)
        # добавляем строку ввода для наименования
        self.entry_name = ttk.Entry(self)
        # меняем координаты объекта
        self.entry_name.place(x=200, y=50)
        # добавляем строку ввода для email
        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=80)
        # добавляем строку ввода для телефона
        self.entry_tel = ttk.Entry(self)
        self.entry_tel.place(x=200, y=110)
        # кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)


        # кнопка добавления
        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        # срабатывание по ЛКМ
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                       self.entry_email.get(),
                                                                       self.entry_tel.get()))
#класс обновление записи
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=206, y=170)
        btn_edit.bind('<Button-1>',lambda event: self.view.update_record(self.entry_name.get(),
                                                    self.entry_email.get(),
                                                    self.entry_tel.get()))
        #закрываем окно редактирования
        #add='+ позволяет на одну кнопку вешать более одного события
        btn_edit.bind('<Button-1>', lambda event: self.destroy(), add='+')
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM abc WHERE
                          id=?''',
        (self.view.tree.set(self.view.tree.selection()[0], '#1')))
        #получаем доступ к первой записи из выборки
        row = self.db.c.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_email.insert(0, row[2])
        self.entry_tel.insert(0, row[3])

#класс поиска записи
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app
    
    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105 , y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50) 
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')
    


class DB():
    def __init__(self):
        self.conn = sqlite3.connect('abc.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS abc (
        id INTEGER PRIMARY KEY, 
        name TEXT,
        tel TEXT,
        email TEXT);""")
        self.conn.commit()

    def insert_data(self, name, tel, email):
        self.c.execute("""INSERT INTO abc(name, tel, email)
        VALUES(?, ?, ?)""", (name, tel , email))
                  



if __name__== '__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root)
    root.title('Телефонная книга')
    root.geometry('665x450')
    root.resizable(False, False)
    root.mainloop()