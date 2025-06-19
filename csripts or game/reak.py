import tkinter as tk
import time
import random

class ReactionGame:
    def __init__(self, master): #конструктор принимает главное окно tkinter
        self.master = master #сохраняет переданое окно в переменую self.master
        self.master.title("Игра на реакцию (Круги)")
        self.master.geometry("250x400")

        self.label = tk.Label(master, text="Нажми 'Старт' и жди круга", font=("Arial", 14))
        self.label.pack(pady=0)

        self.canvas = tk.Canvas(master, width=200, height=230) #область для рисования
        self.canvas.pack(pady=10)
        self.circle = self.canvas.create_oval(50, 50, 150, 150, fill="gray") #рисует круг/овал, вписанный в прямоугольник от (50, 50) до (150, 150)
        # Итоговые координаты круга: 
        # Левый верхний угол — (50, 50)
        # Правый нижний угол — (150, 150)
        # Центр круга — (100, 100), радиус — 50 пикселей
        self.canvas.tag_bind(self.circle, "<Button-1>", self.react) #назначает обработчик нажатия на круг при клике ЛКМ вызвать метод react

        self.start_button = tk.Button(master, text="Старт", command=self.start_game, font=("Arial", 12)) #кнопка запуска
        self.start_button.pack(pady=30)

        self.result_label = tk.Label(master, text="", font=("Arial", 12)) #пустая метка для вывода результата
        self.result_label.pack(pady=2)

        self.ready_to_click = False #разрешено ли кликать по кругу (сначала нельзя)
        self.start_time = 0  #переменная для хранения времени когда круг стал зелёным
 
    def start_game(self): #запускает новую игру
        self.result_label.config(text="") #очищает текст результата
        self.canvas.itemconfig(self.circle, fill="red")  #делает круг крастным
        self.ready_to_click = False #запрещает клик по кругу
        wait_time = random.randint(2000, 5000) #выбирает случайную задержку от 2 до 5 секунд
        self.label.config(text="Готовься нужн будет\n нажать на зелёный круг")
        self.master.after(wait_time, self.show_circle)  #вызывает метод show_circle через wait_time миллисекунд

    def show_circle(self):
        self.canvas.itemconfig(self.circle, fill="green")  #делает круг зелёным как сигнал к действию
        self.label.config(text="Кликай по кругу!")
        self.start_time = time.time() #запоминает текущее время старта
        self.ready_to_click = True #разрешает клик по кругу

    def react(self, event):
        if self.ready_to_click: #проверяет можно ли кликать
            reaction_time = time.time() - self.start_time #вычисляет время реакции
            self.label.config(text="Нажми 'Старт' и жди круга") #возвращает исходный текст
            self.result_label.config(text=f"Время реакции: {reaction_time:.3f} секунд") #показывает результат
            self.canvas.itemconfig(self.circle, fill="gray") #делает круг серым
            self.ready_to_click = False #запрещает дальнейшие клики
        else:
            self.result_label.config(text="Слишком рано! Жди зелёный круг!")


root = tk.Tk()  #создаёт главное окно
game = ReactionGame(root)  #создаёт объект игры и передаёт ему окно
root.mainloop()  #запускает главный цикл программы