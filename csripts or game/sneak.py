import tkinter as tk #для создания графического интерфейса
import random #для генерации случайных значений (координат еды)

WIDTH = 600 #разрешение ширина
HEIGHT = 400  #разрешение высота
DELAY = 150 #задержка между обновлениями экрана в миллисекундах
SIZE = 20 #размер одного квадратика змейки и еды

class SnakeGame:
    def __init__(self, root): #конструктор класса вызывается при создании объекта
        self.root = root #сохраняем переданное главное окно tkinter
        self.root.title("Змейка на tkinter") #устанавливаем заголовок окна

        self.frame = tk.Frame(root) #создаём отдельный контейнер как папку чтобы удобно группировать элементы (например стартовое меню или игровое поле)
        self.frame.pack() #показываем эту коробку в окне всё что внутри неё станет видно


        self.start_screen() #вызываем функцию для показа стартового экрана с кнопкой "Старт" и заголовком

    def start_screen(self):
        self.clear_frame() #очищаем всё внутри фрейма, чтобы подготовить место для стартового экрана
        start_label = tk.Label(self.frame, text="Змейка", font=("Arial", 30)) #надпись с созданием игры
        start_label.pack(pady=20) #показываем надпись с отступами сверху и снизу

        start_button = tk.Button(self.frame, text="Старт", font=("Arial", 20), command=self.start_game) #cоздаём кнопку cтарт при нажатии на которую запускается игра (вызывается метод start_game)
        start_button.pack(pady=20) #размещает надпись с отступами сверху и снизу

    def start_game(self):
        self.clear_frame() #очищаем текущий экран (удаляем меню) чтобы показать игровое поле
        self.canvas = tk.Canvas(self.frame, width=WIDTH, height=HEIGHT, bg="black") #создаём поле для игры черное окно где будет отображаться змейка и еда
        self.canvas.pack() #показываем игровое поле 

        self.score = 0 #начальный счет игрока равен нулю
        self.snake = [(WIDTH//2, HEIGHT//2)] #змейка начинается с одной клетки в центре экрана
        self.direction = 'Right' #начальное движение змейки это право
        self.food = None #позиция еды пока не задана
        self.create_food() #создаем еду в случайном месте не пересекающемся со змейкой

        self.score_text = self.canvas.create_text(50, 10, fill="white", font=("Arial", 16), text=f"Счёт: {self.score}") #отображаем текущей счет в левом верхнем углу

        self.root.bind("<Key>", self.change_direction) #cвязываем нажатия клавиш с функцией изменения направления змейки
        self.running = True #флаг что игра запущена и должна продолжаться
        self.game_loop()  #запускаем главный цикл игры — она будет обновляться через заданный интервал времени (delay - 150)

    def clear_frame(self):
        for widget in self.frame.winfo_children():#получаем список всех элементов (кнопок, надписей и др.) внутри фрейма
            widget.destroy() #удаляем каждый элемент что бы очистить фрейм полностью 

    def create_food(self):
        possible_positions = [] #эта список всех свободных клеток для игры
        for x in range(0, WIDTH, SIZE): #проходим по всем координатам по ширене с шагом size
            for y in range(0, HEIGHT, SIZE):#аналогично ток тут по высоте
                if (x, y) not in self.snake: #если эта клетка не занята змейкой
                    possible_positions.append((x, y)) #добавим эту клетку в коондидаты на появление еды
        self.food = random.choice(possible_positions) #из всех коондидатов выбераем рандомно где будет еда
    #меняем направление змейки но не даём ей повернуть в обратную сторону (чтобы не врезаться в себя)
    #эта просто бинды кнопки управление
    def change_direction(self, event):
        key = event.keysym #получаем нажатую стрелку
        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head_x, head_y = self.snake[0] #получаем текущие координати головы змейки
        #тут изменяем координаты головы в зависимости от движения
        if self.direction == "Left":
            head_x -= SIZE #сдвигаем влево на один блок
        elif self.direction == "Right":
            head_x += SIZE #вправо
        elif self.direction == "Up":
            head_y -= SIZE #вверх
        elif self.direction == "Down":
            head_y += SIZE #вниз

        # Обработка выхода за границы — перенос на противоположную сторону
        if head_x < 0:  #если голова ушла за левый край окна
            head_x = WIDTH - SIZE  #то перемещаем её на правый край (ширина окна минус размер блока)
        elif head_x >= WIDTH:  #если голова ушла за правый край окна
            head_x = 0  #то перемещаем её на левый край (координата 0)

        if head_y < 0:  #если голова ушла за верхний край окна
            head_y = HEIGHT - SIZE  #то перемещаем её в самый низ (высота окна минус размер блока)
        elif head_y >= HEIGHT:  #если голова ушла за нижний край окна
            head_y = 0  #то перемещаем её в самый верх (координата 0)


        new_head = (head_x, head_y) #создаём новую позицию головы змейки в виде кортежа с обновлёнными координатами

       
        if new_head in self.snake: #чекаем не столкнулась ли голова змейки с ее телом
            self.game_over() #если столкнулась вызываем конец игры
            return False #возращаем фолс что бы остоновить движение змейки и остоновить игровой цикл

        self.snake.insert(0, new_head) #добавляем новую голову змейки в начало списка — змейка движется вперёд

        if new_head == self.food: #если голова съела еду(координаты совпали)
            self.score += 1 #увеличиваем счет
            self.create_food() #создаем новую еду
            self.canvas.itemconfig(self.score_text, text=f"Счёт: {self.score}") #обновляем текст со счетом
        else:
            self.snake.pop() #если еда не съедена удаляем последний блок тела змейки что бы она не росла 

        return True #возвращаем тру значит змея жива и все успешно 

    def game_loop(self): #эт основной цикл который повторяется через основной интервал времени
        if self.running: #проверяем что игра еще не кончилась 
            alive = self.move_snake() #двигаем змейку и получаем результат жива или не
            if alive: #если жива то 
                self.draw() #отрисовываем текущее состояние игры на экране
                self.root.after(DELAY, self.game_loop) #запускаем следующий цикл игры через задержку delay

    def draw(self): #функция для отрисовки всех элементов игры
        self.canvas.delete("all") #очищаем холст от всех пред объектов (обновляем экран)

        x, y = self.food # получаем координаты еды
        self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="red", outline="") #рисуем еду в виде крастного квадрата

        for i, (x, y) in enumerate(self.snake): #проверяем все сегменты змейки(с координатами и индексом)
            color = "green" if i == 0 else "lightgreen" #первый сегмент голова будет зеленым, остальное светло зеленые 
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color, outline="") #рисуем каждый сегмент змейки как квадрат нужного цвета

        self.canvas.create_text(50, 10, fill="white", font=("Arial", 16), text=f"Счёт: {self.score}") #отображаем текущий счет

    def game_over(self): #конец
        self.running = False #остонавливаем игру больше не вызываем game_loop
        self.clear_frame() #очищаем фрейм (удаляем все с экрана)

        game_over_label = tk.Label(self.frame, text="Игра окончена!", font=("Arial", 30), fg="red") #печальная надпись
        game_over_label.pack(pady=20) 

        score_label = tk.Label(self.frame, text=f"Твой счёт: {self.score}", font=("Arial", 20))
        score_label.pack(pady=10) #показываем счет игрока 

        restart_button = tk.Button(self.frame, text="Играть снова", font=("Arial", 20), command=self.start_game) #кнопка для перезапуска игры запускает start_game
        restart_button.pack(pady=20) 


root = tk.Tk() #создаем главное окно приложения
game = SnakeGame(root) #создаем экземпляр игры передаем в него окно 
root.mainloop() #запускаем главный цыкл tkinter окно будет реагировать на действия пользователя 
