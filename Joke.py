import tkinter as tk
import random
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('jokes.db')
c = conn.cursor()

c.execute('''CREATE TABLE Jokes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              joke TEXT)''')

jokes = [("1", "Из комбинации лени и логики получаются программисты."),
         ("2", "Не так велика вселенная, как ее исходный код…"),
         ("3", "Некоторые программисты настолько ленивы, что сразу пишут рабочий код."),
         ("4", "Программист сделал своей девушке приложение…"),
         ("5", "Разработчики, обвиненные в написании нечитабельного кода, отказались давать комментарии.")]
c.executemany("INSERT INTO Jokes (id, joke) VALUES (?, ?)", jokes)

conn.commit()
conn.close()