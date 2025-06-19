import tkinter as tk #Импорт библиотеки для создания графического интерфейса
import random #Импорт библиотеки для генерации случайных чисел
import time #Импорт библиотеки для работы со временем
from threading import Thread #Импорт класса для запуска кода в отдельном потоке

def lighten_color(color, amount=0.5): #Функция, чтобы сделать цвет посветлее
    rgb = root.winfo_rgb(color) #Получает цвет в виде чисел (красный, зелёный, синий)
    r = rgb[0] // 256 #это смесь трёх цветов: красного (R), зелёного (G) и синего (B
    g = rgb[1] // 256 #Каждый из них может быть от 0 (нет цвета) до 255 (максимальная яркость
    b = rgb[2] // 256 #Например, (255, 0, 0) — ярко-красный, а (0, 0, 0) — чёрный

    #Смещаем цвет к белому по формуле
    r = int(r + (255 - r) * amount) # r = 100 + (255 - 100)*0.5 = 100 + 155*0.5 = 100 + 77.5 = 177
    g = int(g + (255 - g) * amount) # g = 150 + (255 - 150)*0.5 = 150 + 105*0.5 = 150 + 52.5 = 202
    b = int(b + (255 - b) * amount) # b = 200 + (255 - 200)*0.5 = 200 + 55*0.5 = 200 + 27.5 = 227

    return f"#{r:02x}{g:02x}{b:02x}"# Преобразует числа r, g, b в строку цвета в формате HEX (например, "#aabbcc")

class SimonSaysGame:
    def __init__(self, root):  # Функция, которая запускается при создании игры и настраивает всё сначала
        self.root = root # Сохраняет главное окно программы для дальнейшей работы с ним
        self.root.title("Simon Says") # название окна программы
        self.root.geometry("400x450") # разрешение
        self.root.resizable(False, False) # Запрещает менять размер окна по ширине и высоте

        self.colors = ["green", "red", "purple", "blue"] # Список основных цветов кнопок игры
        self.light_colors = [lighten_color(c, 0.5) for c in self.colors] #создаёт новый список, где каждый цвет из self.colors становится светлее на 50% с помощью функции lighten_color
        self.buttons = []  # Список кнопок игры
        self.sequence = []  # Последовательность цветов, которую нужно запомнить
        self.player_input = []  # Ввод игрока для повторения последовательности
        self.level = 0 # Текущий уровень игры
        self.is_playing_sequence = False  # Показывает, что сейчас НЕ идёт показ цвета, и игрок может нажимать кнопки

        self.create_widgets() # Создаёт все кнопки и элементы интерфейса игры

    def create_widgets(self):
        frame = tk.Frame(self.root) # Создаёт рамку для кнопок
        frame.pack(pady=20) #Размещает эту рамку с отступом сверху и снизу

        for i, color in enumerate(self.colors):  # Проходим по списку цветов с индексами (i — номер кнопки, color — её цвет)
            btn = tk.Button(frame, bg=color, activebackground=self.light_colors[i], width=10, height=5, # Создаёт кнопку внутри рамки,Основной цвет кнопки(светлый оттенок), Размер кнопки (ширина и высота)
                            command=lambda i=i: self.player_click(i), relief="raised") # При нажатии на кнопку вызывается функция, которая передаёт её номер (i),# Кнопка выглядит как приподнятая
            btn.grid(row=i//2, column=i%2, padx=10, pady=10) #каждые две кнопки идут в новую строку (0, 1 → первая строка; 2, 3 → вторая),первая кнопка в строке слева (столбец 0), вторая справа (столбец 1),отступы по горизонтали и вертикали между кнопками
            self.buttons.append(btn) # Добавляет кнопку в список всех кнопок игры

        self.start_button = tk.Button(self.root, text="Начать игру", font=("Arial", 14), command=self.start_game) # Создаёт кнопку "Начать игру", которая запускает игру при нажатии
        self.start_button.pack(pady=20) # Размещает кнопку "Начать игру" с отступом сверху и снизу

        self.status_label = tk.Label(self.root, text="Нажмите 'Начать игру' чтобы начать", font=("Arial", 12)) # Создаёт текстовую надпись с инструкцией для игрока
        self.status_label.pack() # Размещает текстовую надпись под кнопкой "Начать игру"

    def start_game(self):  # Запускает новую игру
        self.sequence = []  # Очищает старую последовательность цветов
        self.player_input = [] # Очищает ввод игрока
        self.level = 0  # Сбрасывает уровень на 0
        self.status_label.config(text="Игра началась! Следи за последовательностью...") # Обновляет текст на экране
        self.next_round() # Начинает первый раунд

    def next_round(self): # Начинает новый уровень игры
        self.level += 1 # Увеличивает номер уровня на 1
        self.player_input = [] # Очищает ввод игрока для нового уровня
        self.sequence.append(random.randint(0, 3)) # Добавляет случайный цвет к последовательности
        self.status_label.config(text=f"Уровень {self.level}. Запоминай!") # Показывает текущий уровень и инструкцию
        self.is_playing_sequence = True # Запрещает игроку нажимать кнопки пока игра показывает последовательность
        Thread(target=self.play_sequence).start() # Запускает показ последовательности в отдельном потоке (чтобы не "заморозить" интерфейс)

    def play_sequence(self): # Показывает игроку последовательность кнопок
        for index in self.sequence: # Для каждого цвета в последовательности
            self.highlight_button(index)  # Подсвечивает кнопку светлым цветом
            time.sleep(0.6)  # Ждёт 0.6 секунды
            self.unhighlight_button(index) # Возвращает кнопку к обычному цвету
            time.sleep(0.2)  # Ждёт 0.2 секунды перед следующей кнопкой
        self.is_playing_sequence = False   # Разрешает игроку нажимать кнопки
        self.status_label.config(text="Твой ход! Повтори последовательность.") # Сообщает, что ход игрока

    def highlight_button(self, index): 
        self.buttons[index].config(bg=self.light_colors[index])  # Подсвечивает кнопку светлым цветом
        self.buttons[index].update()  # Обновляет кнопку, чтобы сразу показать изменение

    def unhighlight_button(self, index):
        self.buttons[index].config(bg=self.colors[index]) # Возвращает кнопку к обычному цвету
        self.buttons[index].update()  # Обновляет кнопку на экране сразу

    def player_click(self, index):
        if self.is_playing_sequence:  # Если сейчас игра показывает последовательность, игнорируем нажатия игрока
            return # Просто выходим, не обрабатывая клик

        self.highlight_button(index) # Подсвечивает кнопку при нажатии
        self.root.after(300, lambda: self.unhighlight_button(index)) # Через 300 мс убирает подсветку кнопки

        self.player_input.append(index) # Добавляет номер нажатой кнопки в список ответов игрока
        current_step = len(self.player_input) - 1 # Определяет индекс последнего нажатия (текущий шаг)

        if self.player_input[current_step] != self.sequence[current_step]: # Если игрок ошибся в текущем шаге
            self.status_label.config(text=f"Неверно! Игра окончена. Ты достиг уровня {self.level}.") # Показываем что он ошибся
            self.sequence = []  # Очищаем последовательность (конец игры)
            return # Прекращаем обработку, игра останавливается

        if len(self.player_input) == len(self.sequence): # Если игрок повторил всю последовательность правильно
            self.status_label.config(text="Правильно! Подготовься к следующему уровню...") # Сообщаем успех
            self.root.after(1500, self.next_round)  # Через 1.5 секунды запускаем следующий уровень



root = tk.Tk() # Создаёт главное окно программы
game = SimonSaysGame(root) # Создаёт игру и связывает с окном
root.mainloop() # Запускает цикл обработки событий (чтобы окно работало)