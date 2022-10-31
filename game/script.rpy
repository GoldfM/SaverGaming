# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#25ff25")
define AIHome = Character('Умный дом', color = "#ff6600")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init python:
    onn = ImageDissolve("eye.png", 0.9, 20, reverse=False) 
    off = ImageDissolve("eye.png", 0.7, 10, reverse=True) 
label start:
    image animated = Movie(play="wait.ogv", pos=(0,0), anchor=(0, 0))
    scene animated
    with Pause(1)

    show e at center with dissolve
    
    e "Я перед анимированным фоном!"

    $ name_ = renpy.input("Введите ваше имя", length=11, default = "Максим", allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ").strip()
    if name_ == "":
        $ name_ = "Максим"
    scene black with dissolve
    "Доброй ночи [name_]"
    jump morning
label morning:
    scene home with onn 
    pause 0.2
    scene black with off
    pause 0.2
    scene home with onn
    pause 0.2

    AIHome "Доброе утро [name_], ваш сегодняшний сон составил всего лишь 4 часа. Не хотел вас тревожить, но вы просили разбудить вас в 6:00, сказали что это очень важно."
    AIHome "Сегодня 4 ноября 2106 года, температура в Москве -9 гардусов, к обедупотеплеет до -2, но лучше одевайтесь потеплее."
    menu:
        "Вы чувствуете себя очень усталым, и готовы пожертвоватьвсем ради нескольких часов сна"
        "Спать дальше":
            jump sleep
        "Встать, вопреки всему":
            jump wake_up
    return
