from random import *  # импортируем все из random
from turtle import *  # импортируем все из turtle
from freegames import vector  # импортируем vector из freegames

INITIAL_BALL_SPEED = 5  # задаем начальную скорость шаров
INITIAL_KIVI_SPEED = 3  # задаем начальную скорость камней

ball_speed = INITIAL_BALL_SPEED  # текущая скорость шаров
kivi_speed = INITIAL_KIVI_SPEED  # текущая скорость камней
speed_increase_amount = 0.2  # шаг увеличения скорости
speed_increase_interval_ms = 6000  # интервал увеличения скорости в миллисекундах
maxspeed_baal = 8  # максимальная скорость шаров
maxspeed_kivi = 7  # максимальная скорость камней

game_state = 'playing'  # состояние игры

bird = vector(0, 0)  # позиция птицы
balls = []  # список шаров
kivis = []  # список камней

bgcolor("lightblue")  # устанавливаем цвет фона

def tap(x, y):  # функция прыжка птицы по клику
    if game_state == 'playing':  # проверяем идет ли игра
        up = vector(0, 40)  # вектор движения вверх
        bird.move(up)  # двигаем птицу вверх

def inside(point):  # проверяем находится ли точка в поле
    return -200 < point.x < 200 and -200 < point.y < 200  # возвращаем True если в пределах

def draw():  # функция отрисовки экрана
    clear()  # очищаем экран

    if game_state == 'playing':  # если игра идет
        goto(bird.x, bird.y)  # перемещаемся к позиции птицы
        write('🦉', align='center', font=('Arial', 16, 'normal'))  # рисуем птицу

        for ball in balls:  # для каждого шара
            goto(ball.x, ball.y)  # перемещаемся к шару
            dot(20, 'black')  # рисуем черный шар

        for kivi in kivis:  # для каждого камня
            goto(kivi.x, kivi.y)  # перемещаемся к камню
            dot(30, 'grey')  # рисуем серый камень

    elif game_state == 'game_over':  # если игра закончена
        goto(0, 20)  # перемещаемся к центру сверху
        write("Вы проиграли!", align="center", font=("Arial", 24, "bold"))  # пишем сообщение
        goto(0, -20)  # перемещаемся ниже
        write("Нажмите 'R' для перезапуска", align="center", font=("Arial", 16, "normal"))  # пишем инструкцию

        goto(bird.x, bird.y)  # перемещаемся к позиции птицы
        write('🪶', align='center', font=('Arial', 16, 'normal'))  # рисуем мертвую птицу

    update()  # обновляем экран

def increase_speed():  # функция увеличения скорости
    global ball_speed, kivi_speed  # используем глобальные переменные

    if game_state != 'playing':  # если игра не идет
        return  # выходим из функции

    ball_speed += speed_increase_amount  # увеличиваем скорость шаров
    if ball_speed > maxspeed_baal:  # если скорость больше максимума
        ball_speed = maxspeed_baal  # ограничиваем максимальной

    kivi_speed += speed_increase_amount  # увеличиваем скорость камней
    if kivi_speed > maxspeed_kivi:  # если скорость больше максимума
        kivi_speed = maxspeed_kivi  # ограничиваем максимальной

    if game_state == 'playing':  # если игра идет
        ontimer(increase_speed, speed_increase_interval_ms)  # вызываем функцию снова через интервал

def move():  # основная функция движения объектов
    global game_state  # используем глобальную переменную состояния

    if game_state != 'playing':  # если игра не идет
        return  # выходим из функции

    bird.y -= 5  # птица падает вниз

    for ball in balls:  # для каждого шара
        ball.x -= ball_speed  # двигаем шар влево на скорость

    for kivi in kivis:  # для каждого камня
        kivi.x -= kivi_speed  # двигаем камень влево на скорость

    if randrange(10) == 0:  # с шансом один из десяти
        y = randrange(-199, 199)  # случайная высота
        ball = vector(199, y)  # создаем шар справа
        balls.append(ball)  # добавляем шар в список

        y = randrange(-199, 199)  # случайная высота
        kivi = vector(199, y)  # создаем камень справа
        kivis.append(kivi)  # добавляем камень в список

    while len(balls) > 0 and not inside(balls[0]):  # пока первый шар за пределами
        balls.pop(0)  # удаляем первый шар

    while len(kivis) > 0 and not inside(kivis[0]):  # пока первый камень за пределами
        kivis.pop(0)  # удаляем первый камень

    if not inside(bird):  # если птица вышла за границы
        game_state = 'game_over'  # меняем состояние игры
        draw()  # отрисовываем экран
        return  # выходим из функции

    for ball in balls:  # проверяем столкновение с шарами
        if abs(ball - bird) < 13:  # если расстояние меньше 13
            game_state = 'game_over'  # игра окончена
            draw()  # отрисовываем экран
            return  # выходим из функции

    for kivi in kivis:  # проверяем столкновение с камнями
        if abs(kivi - bird) < 20:  # если расстояние меньше 20
            game_state = 'game_over'  # игра окончена
            draw()  # отрисовываем экран
            return  # выходим из функции

    draw()  # отрисовываем текущий кадр

    if game_state == 'playing':  # если игра идет
        ontimer(move, 30)  # вызываем функцию снова через 30 миллисекунд

def restart_game():  # функция перезапуска игры
    global game_state, bird, balls, kivis, ball_speed, kivi_speed  # используем глобальные переменные

    if game_state == 'game_over':  # если игра окончена
        game_state = 'playing'  # меняем состояние на играем
        bird.x = 0  # ставим птицу в центр по х
        bird.y = 0  # ставим птицу в центр по у
        balls.clear()  # очищаем список шаров
        kivis.clear()  # очищаем список камней
        ball_speed = INITIAL_BALL_SPEED  # сбрасываем скорость шаров
        kivi_speed = INITIAL_KIVI_SPEED  # сбрасываем скорость камней
        move()  # запускаем игровой цикл заново
        increase_speed()  # запускаем таймер увеличения скорости заново

setup(420, 420, 370, 0)  # создаем окно размером 420 на 420 с позиционированием
hideturtle()  # скрываем курсор черепахи
up()  # поднимаем перо чтобы не рисовать линии
tracer(False)  # отключаем анимацию для быстрого обновления
listen()  # включаем обработку нажатий клавиш
onkey(restart_game, 'r')  # перезапуск игры по нажатию r
onkey(restart_game, 'R')  # перезапуск игры по нажатию R
increase_speed()  # запускаем процесс увеличения скорости
onscreenclick(tap)  # прыжок птицы по клику мыши
move()  # запускаем игровой цикл движения
done()  # запускаем главный цикл turtle
