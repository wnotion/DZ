import tkinter as tk
import sqlite3
import random

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


class Joke():
    def __init__(self, root):
        self.root = root
        self.root.title("Joke")
        
        self.text_joke = tk.Text(root, height=5, width=50)
        self.text_joke.pack()
        
        self.button_next = tk.Button(root, text="Next Joke", command=self.get_random_joke)
        self.button_next.pack()

        # Подключение к базе данных
        self.conn = sqlite3.connect('jokes.db')
        self.cursor = self.conn.cursor()

    def get_random_joke(self):
        # Удаление предыдущего анекдота
        self.text_joke.delete(0.0, tk.END)

        # Выполнение запроса на выборку случайного анекдота
        self.cursor.execute("SELECT joke FROM jokes ORDER BY RANDOM() LIMIT 1;")
        joke = self.cursor.fetchone()[0]

        # Вставка анекдота в виджет Text
        self.text_joke.insert(0.0, joke)

    def run(self):
        self.root.mainloop()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = Joke(root)
    app.run()
