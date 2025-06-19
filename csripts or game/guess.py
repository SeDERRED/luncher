import tkinter as tk
import random

class NumberGuessGame:
    def __init__(self, master): # Это "конструктор" класса — выполняется автоматически при создании объекта. "master" — это главное окно tkinter, которое передаётся в игру
        self.master = master #cохраняем переданное окно в переменную self.master чтобы обращаться к нему внутри класса
        self.master.title("Угадай число") #устанавливаем название окна верхней части окна
        self.master.geometry("300x250") #прост разрешение

        self.secret_number = random.randint(1, 100) #загадываем число от 1 до 100 и сейвим в переменую селв.секрет.нумбер
        self.attempts = 0 #счетчик попыток сейчас он 0

        self.label = tk.Label(master, text="Я загадал число от 1 до 100.\nПопробуй угадать!", font=("Arial", 12)) #создаем надпись 
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12)) #создаем поле ввода
        self.entry.pack(pady=5)

        self.check_button = tk.Button(master, text="Проверить", command=self.check_guess, font=("Arial", 12)) #создаем кнопку проверить,после нажатия вызовется метод check_guess
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12)) #создаем пустую надпись,позже сюда будет выодиться результат меньше больше и тд
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(master, text="Заново", command=self.restart_game, font=("Arial", 10)) #создаем кнопку заново,вызываем метод restart_game
        self.restart_button.pack(pady=5)

    def check_guess(self): #метод который вызывается если нажали кнопку проверить
        try:
            guess = int(self.entry.get()) #пытаемся получить число из поля ввода и преобразовать его в целое число
        except ValueError:
            self.result_label.config(text="Введите число!")
            return #останавливаем функцию если ошибка

        self.attempts += 1 #увеличиваем счетчик попыток на 1


        if guess<self.secret_number:
            self.result_label.config(text='больше')
           

        elif guess> self.secret_number:
            self.result_label.config(text="меньше")
        else:
            self.result_label.config(text=f"Угадал за {self.attempts} попыток!") #показываем за сколько попыток

    def restart_game(self): #метод вызывается если жмут заново 
        self.secret_number = random.randint(1, 100) #новое число
        self.attempts = 0 #сбрасываем попытки до 0
        self.entry.delete(0, tk.END) #очищаем поле ввода от предыдущего числа (начинаем с пустого)
        self.result_label.config(text="") #очищаем текст с результатом (меньше/больше/угадал)
        self.label.config(text="Я загадал число от 1 до 100.\nПопробуй угадать!")


root = tk.Tk() #создаём главное окно приложения
game = NumberGuessGame(root) #создаём объект игры передаём в него главное окно
root.mainloop() #запускаем главный цикл tkinter oкно будет работать пока пользователь его не закроет
