import tkinter as tk  #модуль для создания окон кнопок и интерфейса
from tkinter import messagebox, PhotoImage  #всплывающие окна и картинки в окне
from PIL import Image, ImageTk  #библиотека для работы с изображениями
import webbrowser  #открывает сайты в браузере
import subprocess  #запускает другие программы или команды
import sys  #доступ к функциям питона например выход из программы
import os  #работа с файлами и папками

BG_COLOR = "#1b2838"#цвет фона окна темно синий как у стим
FRAME_BG_COLOR = "#2a3f54" #цвет внутренних блоков немного светлее чем фон
TEXT_COLOR = "#c7d5e0" #цвет текста светло серо голубой хорошо видно
ACCENT_COLOR = "#66c0f4" #яркий голубой цвет для акцентов важных элементов
EXIT_BUTTON_BG_COLOR = "#c94c4c" #красный цвет для кнопки выхода
BUTTON_BG_COLOR = "#4a6e8a" #цвет обычных кнопок темно синий
BUTTON_FG_COLOR = TEXT_COLOR #цвет текста на кнопках такой же как обычный текст
SUPPORT_BUTTON_BG_COLOR = "#556b2f" #цвет кнопки поддержки зеленый чтобы отличалась
ABOUT_BUTTON_BG_COLOR = "#4f5b62" #цвет кнопки о программе серо синий
BUTTON_ACTIVE_BG_COLOR = "#5e8bb0" #цвет кнопки когда на неё наводят мышкой или нажимают
FONT_FAMILY_MAIN = "Segoe UI" #основной шрифт
FONT_SIZE_NORMAL = 10 #обычный размер текста
FONT_SIZE_MEDIUM = 12 #средний размер текста
FONT_SIZE_LARGE = 16 #крупный текст для заголовков
FONT_BOLD = "bold" #жирный

GAMES = [ 
    {
        "name": "Trips-traps-trull", #название игры показывается в интерфейсе
        "path": "..\\oleg2007\\csripts or game\\reak.py", #путь к файлу
        "description": """🎮 Тест на реакцию!
Мини-игра для проверки скорости реакции. Нажми кнопку после сигнала.

🏆 Особенности: уровни, статистика, минимализм.
Тренирует реакцию, внимание. Полезно для ума!""",
        "cover_path": "..\\oleg2007\\image\\AIM.jpg" #путь к картинке
    },
    {
        "name": "Guess number",
        "path": "..\\oleg2007\\csripts or game\\guess.py", 
        "description": """🔢 Угадай число!
Компьютер загадал число от 1 до 100. Попробуй угадать его за наименьшее количество попыток!""",
        "cover_path": "..\\oleg2007\\image\\chis.jpg"
    },
{
        "name": "Snake",
        "path": "..\\oleg2007\\csripts or game\\sneak.py", 
        "description": """🐍 Классическая игра 'Змейка'.
Управляй змейкой, собирай еду и расти. Не врезайся в себя или стены!""",
        "cover_path": "..\\oleg2007\\image\\snake.jpg"
    },
{
        "name": "Simon",
        "path": "..\\oleg2007\\csripts or game\\simon.py",
        "description": """🧠 Simon: игра на память.
Повторяй последовательность цветов.

Развивает память и внимание.""",
        "cover_path": "..\\oleg2007\\image\\simon.jpg"
    },
    {
        "name": "Flappy Bird",
        "path": "..\\oleg2007\\csripts or game\\gamesam.py", 
        "description": """🐦 Flappy Bird!
Управляй птичкой, пролетая между трубами. Набери как можно больше очков!
Просто кликай, чтобы птичка взлетала.""",
        "cover_path": "..\\oleg2007\\image\\flapy.jpg" 
    },
]


class GameLauncherApp: #создаём класс лаунчера игр
    def __init__(self, root):#конструктор запускается когда создаётся объект этого класса
        self.root = root #сохраняем переданное окно (tk.Tk()) в переменную self.root
        self.root.title("Steam")
        self.root.geometry("800x550") 
        self.root.configure(bg=BG_COLOR) #устанавливаем цвет фона окна (берётся из ранее заданной переменной BG_COLOR)

        self.button_style = { #создаём словарь для кнопок чтобы все выглядели одинаково
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL), #шрифт и его размер
            "bg": BUTTON_BG_COLOR, #фон кнопки обычный
            "fg": BUTTON_FG_COLOR, #цвет текста на кнопке
            "activebackground": BUTTON_ACTIVE_BG_COLOR, #цвет фона при наведении/нажатии
            "activeforeground": TEXT_COLOR, #цвет текста при наведении/нажатии
            "relief": "flat", #стиль кнопки без выпуклостей плоская
            "borderwidth": 0, #толщина границы 0 то есть без рамки
            "width": 22, #ширина кнопки
            "anchor": "w", #текст внутри кнопки прижат к левому краю (w = west = лево)
            "padx": 10, 
            "compound": tk.LEFT, #если рядом с текстом будет изображение то оно слева
        }
        self.launch_button_style = self.button_style.copy()  # копируем стиль кнопки 
        self.launch_button_style.update({
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM, FONT_BOLD),  #шрифт средний размер и жирный
            "bg": ACCENT_COLOR,#цвет фона ставим ярко-синий для акцента 
            "fg": "#FFFFFF", #цвет текста делаем белым
            "activebackground": "#55b0e4", #цвет фона кнопки при нажатии светлее 
            "width": 20, #ширина кнопки уменьшается  
            "anchor": "center", #выравниваем текст по центру кнопки  
        
        })
        self.exit_button_style = self.button_style.copy() #копируем базовый стиль для кнопки выхода
        self.exit_button_style.update({
            "bg": EXIT_BUTTON_BG_COLOR, #красный кнопка выхода
            "activebackground": "#4b1f1f", #цвет фона при наведении/нажатии темно-красный
            "fg": "#FFFFFF", #цвет текста белый
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD), #шрифт кнопки семейство размер жирность
            "anchor": "center", 
        })
        self.support_button_style = self.button_style.copy() #копируем базовый стиль для кнопки поддержки
        self.support_button_style.update({
            "bg": SUPPORT_BUTTON_BG_COLOR,  #задаём цвет фона для кнопки поддержки
            "activebackground": "#38441F",  #цвет фона при наведении/нажатии - тёмно-зелёный
            "fg": "#FFFFFF",
            "anchor": "center",
        })
        self.about_button_style = self.button_style.copy() #копируем базовый стиль для кнопки "О программе"
        self.about_button_style.update({
            "bg": ABOUT_BUTTON_BG_COLOR, #задаём цвет фона кнопки о программе
            "activebackground": "#3e4a52", #цвет фона при наведении/нажатии - тёмно-синий
            "fg": "#FFFFFF",
            "font": (FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD),  #шрифт кнопки семейство размер жирность
            "anchor": "center",
        })



       
        main_frame = tk.Frame(root, bg=BG_COLOR) #создаём главный фрейм с фоном BG_COLOR внутри root
        main_frame.pack(fill="both", expand=True, padx=10, pady=10) #размещаем фрейм с отступами, растягиваем по ширине и высоте

       
        self.games_list_frame = tk.Frame(main_frame, width=250, bg=FRAME_BG_COLOR, relief="solid", borderwidth=1)  #фрейм для списка игр с шириной 250, рамкой и фоном
        self.games_list_frame.pack(side="left", fill="y", padx=(0, 10)) #прикрепляем слева, растягиваем по вертикали, с отступом справа 10
        
        #создаём и размещаем метку Игры с отступами и выравниванием влево
        tk.Label(
            self.games_list_frame,
            text="Игры:",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM, FONT_BOLD),
            bg=FRAME_BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=10, padx=10, anchor="w") 

        
        self.game_buttons_frame = tk.Frame(self.games_list_frame, bg=FRAME_BG_COLOR) #контейнер для кнопок игр с тем же фоном
        self.game_buttons_frame.pack(fill="x", expand=False)  #размещаем, чтобы растягивался по ширине но не по высоте

       #кнопка выхода с командой закрытия окна и стилем из exit_button_style
        exit_button = tk.Button(
            self.games_list_frame,
            text="Выход",
            command=self.root.destroy,
            **self.exit_button_style
        )
        exit_button.pack(side="bottom", pady=(1,10), padx=10, fill="x") #размещаем кнопку снизу с отступами и растягиваем по ширине

        
        support_button = tk.Button( #создаём кнопку
            self.games_list_frame, #панель в которой будет размещена кнопка
            text="Поддержка",
            command=self.open_support_chat,  #функция вызываемая при нажатии открыть чат поддержки
            **self.support_button_style #применяем заранее заданный стиль для кнопки поддержки
        )
        support_button.pack(side="bottom", pady=(1,1), padx=10, fill="x") #размещаем кнопку внизу с отступами сверху и снизу по 1 слева и справа по 10 растягиваем по ширине

        about_button = tk.Button( 
            self.games_list_frame, 
            text="О программе",
            command=self.show_about_info, # функция вызываемая при нажатии
            **self.about_button_style #применяем заранее заданный стиль для кнопки
        )
        about_button.pack(side="bottom", pady=(10,1), padx=10, fill="x") # размещаем кнопку внизу, с отступом сверху 10, снизу 1, слева и справа по 10, растягиваем по ширине

        
        self.details_frame = tk.Frame(main_frame, bg=FRAME_BG_COLOR, relief="solid", borderwidth=1) #создаём фрейм для информации с фоновым цветом и рамкой
        self.details_frame.pack(side="right", fill="both", expand=True) #размещаем фрейм справа он заполняет всё доступное пространство и расширяется вместе с окном

        #заполнение списка игр 
        #P.S ЛОГИ ДЕЛАЛИСЬ НЕ ДЛЯ ПОЛЬЗОВАТЕЛЯ, А ДЛЯ РАЗРАБОТЧИКА ПОТОМУ ЧТО ВОЗНИКАЛИ ОШИБКИ С PILLOW
        for game_info in GAMES:  #для каждой игры из списка игр
            icon_image = None  #иконки пока нет
            icon_path_from_config = game_info.get("icon_path") #берем путь к иконке из настроек игры 
            print(f"\n[ИГРА: {game_info['name']}] Обработка icon_path: '{icon_path_from_config}'")

            if icon_path_from_config: #если путь к иконке есть
                
                normalized_path_from_config = os.path.normpath(icon_path_from_config) #нормализуем путь убираем лишние слеши
                print(f"  Нормализованный icon_path из конфига: '{normalized_path_from_config}'") 

                if os.path.isabs(normalized_path_from_config): #если путь абсолютный полный
                    actual_path_to_check = normalized_path_from_config #используем как есть
                else:
                    current_script_dir = os.path.dirname(os.path.abspath(__file__)) # папка где лежит скрипт
                    actual_path_to_check = os.path.join(current_script_dir, normalized_path_from_config) # добавляем к папке скрипта
                    actual_path_to_check = os.path.normpath(actual_path_to_check)  # еще раз нормализуем

                print(f"  Финальный проверяемый АБСОЛЮТНЫЙ путь к иконке: '{actual_path_to_check}'") 
 
                if os.path.exists(actual_path_to_check): #если файл по этому пути существует
                    print(f"  Файл иконки НАЙДЕН по пути: '{actual_path_to_check}'")
                    try:
                        pil_image = Image.open(actual_path_to_check) #открываем картинку с помощью pillow
                        print(f"  Pillow Image.open УСПЕШНО. Объект: {pil_image}")
                        print(f"    Размер: {pil_image.size}, Формат: {pil_image.format}, Режим: {pil_image.mode}")
                        icon_image = ImageTk.PhotoImage(pil_image)  #готовим картинку для отображения в tkinter
                        print(f"  ImageTk.PhotoImage УСПЕШНО. Объект: {icon_image}") #если ошибка при открытии картинки
                    except Exception as e:
                        print(f"  [ОШИБКА ЗАГРУЗКИ ИКОНКИ] Путь: {actual_path_to_check}. Ошибка: {e}")
                        icon_image = None #иконку не загрузили
                else:
                    print(f"  [ФАЙЛ ИКОНКИ НЕ НАЙДЕН] по пути: '{actual_path_to_check}'")
                    icon_image = None #иконки нет
            else:
                print(f"  icon_path не указан в конфигурации для игры '{game_info['name']}'.")

            print(f"  Перед созданием кнопки, icon_image: {icon_image}")
            btn = tk.Button(
                self.game_buttons_frame, #кнопка будет внутри фрейма с кнопками игр
                text=game_info["name"], #текст на кнопке — название игры
                image=icon_image, #ставим иконку на кнопку
                **self.button_style, #применяем стиль кнопки
                command=lambda gi=game_info: self.show_game_details(gi) #по нажатию показываем детали игры
            )
            if icon_image: #если иконка есть
                btn.image = icon_image #сохраняем ссылку чтобы картинка не пропала
            btn.pack(pady=3, padx=10, fill="x") #размещаем кнопку с отступами и растягиваем по ширине

        self.cover_label = tk.Label(
            self.details_frame, text="Обложка игры", #надпись для плейсхолдера обложки
            font=(FONT_FAMILY_MAIN, FONT_SIZE_MEDIUM),
            bg="#334B61", fg=TEXT_COLOR,  #темный фон для заглушки обложки
            relief="solid", borderwidth=1 #рамка вокруг метки
        )
        self.cover_label.pack(pady=20, padx=20) #отступы вокруг

        self.game_title_label = tk.Label(
            self.details_frame, text="Название игры",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_LARGE, FONT_BOLD),
            bg=FRAME_BG_COLOR, fg=ACCENT_COLOR #цвет фона и акцентный цвет текста
        )
        self.game_title_label.pack(pady=(0,10))

        self.game_description_text = tk.Label(
            self.details_frame, text="Описание игры...",
            font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL),
            bg=FRAME_BG_COLOR, fg=TEXT_COLOR, 
            wraplength=450, justify="left" #перенос текста и выравнивание по левому краю
        )
        self.game_description_text.pack(pady=10, fill="x", padx=20)

        self.launch_button = tk.Button(self.details_frame, text="ЗАПУСТИТЬ", state="disabled", **self.launch_button_style) #кнопка запуска игры неактивна пока
        self.launch_button.pack(pady=20)

        if GAMES:
            self.show_game_details(GAMES[0]) #если игры есть показываем детали первой игры
        else:
            self.game_title_label.config(text="Нет игр для отображения")

    def show_game_details(self, game_info):
        self.current_game_path = game_info["path"] #сохраняем путь игры
        self.current_game_name = game_info["name"] #сохраняем имя игры

        self.game_title_label.config(text=game_info["name"]) #обновляем заголовок игры
        self.game_description_text.config(text=game_info.get("description", "Описание отсутствует."))  #описание или заглушка

        cover_path_from_config = game_info.get("cover_path") #путь к обложке из конфигурации
        loaded_cover_image = None

        if cover_path_from_config:
            #определяем абсолютный путь к обложке
            if os.path.isabs(cover_path_from_config):
                actual_cover_path = os.path.normpath(cover_path_from_config) #нормализуем абсолютный путь
            else:
                #если путь относительныйь он будет относительно директории скрипта
                current_script_dir = os.path.dirname(os.path.abspath(__file__))
                actual_cover_path = os.path.join(current_script_dir, cover_path_from_config)
                actual_cover_path = os.path.normpath(actual_cover_path) #нормализуем

            self.log_message(f"  [ОБЛОЖКА] Попытка загрузки из: '{actual_cover_path}'")

            if os.path.exists(actual_cover_path):
                try:
                    pil_image = Image.open(actual_cover_path) #открываем изображение
                    desired_width = 280 #новая ширина
                    aspect_ratio = pil_image.height / pil_image.width #соотношение сторон
                    desired_height = int(desired_width * aspect_ratio) #высота пропорциональна
                    pil_image = pil_image.resize((desired_width, desired_height), Image.Resampling.LANCZOS)  #меняем размер
                    self.log_message(f"    Размер обложки после resize: {pil_image.size}")
                    
                    loaded_cover_image = ImageTk.PhotoImage(pil_image) #конвертируем для tkinter
                    self.log_message(f"    Обложка успешно загружена: {pil_image}")
                except Exception as e:
                    self.log_message(f"  [ОШИБКА ЗАГРУЗКИ ОБЛОЖКИ] Путь: {actual_cover_path}. Ошибка: {e}")
                    loaded_cover_image = None
            else:
                self.log_message(f"  [ФАЙЛ ОБЛОЖКИ НЕ НАЙДЕН] по пути: {actual_cover_path}")
        else:
            self.log_message(f"  cover_path не указан в конфигурации для игры '{game_info['name']}'.")

        if loaded_cover_image:
            self.cover_label.config(image=loaded_cover_image, text="") #если есть картинка убираем текст
            self.cover_label.image = loaded_cover_image #сохраняем ссылку чтобы картинка не пропала
        else:
            #если картинки нет показываем текст заглушку
            self.cover_label.config(image="", text=f"Обложка для\n{game_info['name']}")
            self.cover_label.image = None #сбрасываем ссылку
            
        self.launch_button.config(state="normal", command=self.launch_current_game) #активируем кнопку запуска игры

    def launch_current_game(self):  #запускает игру которая выбрана на панели деталей
        if not hasattr(self, 'current_game_path') or not self.current_game_path:
            messagebox.showerror("Ошибка", "Игра не выбрана или путь не указан.")
            return

        game_name_to_launch = self.current_game_name #имя игры для запуска
        game_path_from_config = self.current_game_path #путь из конфигурации
        
        #определяем абсолютный путь к файлу игры
        if not os.path.isabs(game_path_from_config):
            current_script_dir = os.path.dirname(os.path.abspath(__file__)) #папка скрипта
            absolute_game_path = os.path.normpath(os.path.join(current_script_dir, game_path_from_config))
        else:
            absolute_game_path = os.path.normpath(game_path_from_config)  #если уже абсолютный

        self.log_message(f"Попытка запуска: {game_name_to_launch} (Конфиг: '{game_path_from_config}', Абсолютный: '{absolute_game_path}')")
        try:
            if not os.path.exists(absolute_game_path):
                messagebox.showerror("Ошибка Запуска", f"Файл для игры '{game_name_to_launch}' не найден по пути:\n{absolute_game_path}")
                self.log_message(f"Ошибка: Файл не найден - {absolute_game_path}")
                return
            
            if absolute_game_path.lower().endswith(".py"):  #определяем как запускать игру
                game_script_directory = os.path.dirname(absolute_game_path) #папка скрипта игры
                subprocess.Popen([sys.executable, absolute_game_path], cwd=game_script_directory) #запускаем через python
            else:
                subprocess.Popen(absolute_game_path) #запускаем как обычный исполняемый файл
            self.log_message(f"Игра '{game_name_to_launch}' успешно запущена.")
        except OSError as e:
            messagebox.showerror("Ошибка Запуска", f"Не удалось запустить игру '{game_name_to_launch}'.\nОшибка: {e}")
            self.log_message(f"OSError при запуске {game_name_to_launch}: {e}")
        except Exception as e:
            messagebox.showerror("Неизвестная Ошибка", f"Произошла неизвестная ошибка при запуске '{game_name_to_launch}'.\nОшибка: {e}")
            self.log_message(f"Exception при запуске {game_name_to_launch}: {e}")

    def log_message(self, message):
        print(f"[Лаунчер] {message}")#выводим сообщение в консоль с префиксом лаунчер

    def open_support_chat(self):#открывает ссылку на чат поддержки в браузере
        support_url = "https://t.me/turkell"#адрес чата поддержки
        self.log_message(f"Открытие чата поддержки: {support_url}")#логируем открытие ссылки
        webbrowser.open_new_tab(support_url)#открывает указанную ссылку в новой вкладке браузера по умолчанию

    def show_about_info(self):#определяем метод для показа информации о программе
        about_window = tk.Toplevel(self.root)#создаем новое окно верхнего уровня связанное с главным окном
        about_window.title("О программе")#устанавливаем заголовок для нового окна
        about_window.configure(bg=FRAME_BG_COLOR)#устанавливаем цвет фона нового окна
        about_window.resizable(False, False)#запрещаем изменение размеров нового окна по ширине и высоте

        #задаем размеры окна перед центрированием
        window_width = 450#задаем ширину окна о программе в пикселях
        window_height = 800#задаем высоту окна о программе в пикселях

        #центрирование окна о программе относительно главного окна
        self.root.update_idletasks()#обновляем состояние главного окна чтобы получить актуальные размеры и положение
        root_x = self.root.winfo_x()#получаем координату x левого верхнего угла главного окна
        root_y = self.root.winfo_y()#получаем координату y левого верхнего угла главного окна
        root_width = self.root.winfo_width()#получаем ширину главного окна в пикселях
        root_height = self.root.winfo_height()#получаем высоту главного окна в пикселях

        x = root_x + (root_width // 2) - (window_width // 2)#вычисляем координату x для окна о программе чтобы оно было по центру главного окна по горизонтали координата x будет равна x координате главного окна плюс половина ширины главного окна минус половина ширины окна о программе
        y = root_y + (root_height // 2) - (window_height // 2)#вычисляем координату y для окна о программе чтобы оно было по центру главного окна по вертикали координата y будет равна y координате главного окна плюс половина высоты главного окна минус половина высоты окна о программе
        about_window.geometry(f'{window_width}x{window_height}+{x}+{y}')#устанавливаем размер и положение окна о программе окно будет шириной window width высотой window height и его левый верхний угол будет в точке с координатами x и y

        about_window.transient(self.root)#делаем окно о программе дочерним по отношению к главному оно будет поверх него
        about_window.grab_set()#перехватываем все события ввода для этого окна делая его модальным

        info_frame = tk.Frame(about_window, bg=FRAME_BG_COLOR, padx=20, pady=20)#создаем фрейм внутри окна о программе для размещения информации с фоном и отступами
        info_frame.pack(expand=True, fill="both")#размещаем фрейм в окне о программе растягивая его заполняя все доступное пространство

        title_label = tk.Label(#создаем метку для заголовка копи стим
            info_frame,#внутри информационного фрейма
            text="Copy Steam",#текст заголовка
            font=(FONT_FAMILY_MAIN, FONT_SIZE_LARGE, FONT_BOLD),#шрифт заголовка
            bg=FRAME_BG_COLOR,#цвет фона метки
            fg=ACCENT_COLOR#цвет текста метки
        )
        title_label.pack(pady=(0, 15))

        info_text_content = [
            ("Версия:", "(0.1.0)"),
            ("Создатели:", "Jegor Samsonov \nEduard Garusov "),
            ("Описание:", "Этот игровой лаунчер был разработан для обеспечения удобного и приятного доступа к вашей коллекции мини-игр."),
            ("Технологии:", "Python 3, Tkinter, Pillow"),
            ("Особенности:", "- Запуск игр одним кликом\n- Просмотр описаний и обложек\n- Стильный дизайн, вдохновленный известным лаунчером Steam"),
            ("Благодарности:", "Особая благодарность всем, кто участвовал в тестировании, предлагал идеи и оказывал поддержку на всех этапах разработки."),
            ("Начало разработки:", "01.06.2025"),
            ("Релиз:", "ХХ.ХХ.ХХХХ")
        ]

        for header, text in info_text_content:#проходимся по каждому элементу списка информации
            header_label = tk.Label(#создаем метку для заголовка раздела
                info_frame, text=header, font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL, FONT_BOLD),#внутри информационного фрейма с текстом и шрифтом
                bg=FRAME_BG_COLOR, fg=TEXT_COLOR, anchor="nw", justify="left"#с цветом фона текста выравниванием по северо западу и текстом по левому краю
            )#конец создания метки заголовка
            header_label.pack(fill="x", pady=(7,0))

            text_label = tk.Label(#создаем метку для текста раздела
                info_frame, text=text, font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL),#внутри информационного фрейма с текстом и шрифтом
                bg=FRAME_BG_COLOR, fg=TEXT_COLOR, wraplength=380,#с цветом фона текста и ограничением ширины текста для переноса
                anchor="nw", justify="left"#с выравниванием по северо западу и текстом по левому краю
            )#конец создания метки текста
            text_label.pack(fill="x", pady=(0,10))#размещаем метку текста растягивая по ширине с отступом снизу 10 пикселей

        close_button = tk.Button(#создаем кнопку закрыть
            info_frame, text="Закрыть", command=about_window.destroy,#внутри информационного фрейма с текстом и командой закрытия окна
            font=(FONT_FAMILY_MAIN, FONT_SIZE_NORMAL), bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR,#шрифт цвет фона и цвет текста кнопки
            activebackground=BUTTON_ACTIVE_BG_COLOR, relief="flat", width=10#цвет фона при наведении плоский стиль и ширина кнопки
        )#конец создания кнопки
        close_button.pack(pady=(20,0))



root_window = tk.Tk()
app = GameLauncherApp(root_window)
root_window.mainloop()
