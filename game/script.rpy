# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#25ff25")
define AIHome = Character('Умный дом', color = "#ff6600")
define gg = Character('Вы', color = "#00fff7")
define artem = Character('Артем', color = "#dc3936")


define phone_ = Character('Телефон', color = "#a4bda7")
define audio.phone_call = "sounds/rington.mp3"

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
    #сделать миниатюру умного дома
    AIHome "Доброе утро [name_], ваш сегодняшний сон составил всего лишь 4 часа. Не хотел вас тревожить, но вы просили разбудить вас в 6:00, сказали что это очень важно."
    AIHome "Сегодня 4 ноября 2106 года, температура в Москве -9 гардусов, к обедупотеплеет до -2, но лучше одевайтесь потеплее."
    menu:
        "Вы чувствуете себя очень усталым, и готовы пожертвоватьвсем ради нескольких часов сна"
        "Спать дальше":
            call sleep
        "Встать, вопреки всему":
            call wake_up
    jump phone
    return


label sleep:
    gg "Думаю, ничего страшного не произойдет, если поспать еще пару часов"
    play sound phone_call
    "Только вы начали погружаться в сон, как зазвонил телефон"
    return

label wake_up:
    gg "Черт, почему все важные проекты ставят в такую рань?"
    play sound phone_call
    "Стоило вам встать с кровати, как зазвонил телефон"
    return
label phone:
    #Сделать миниатюру Артема
    gg "До начала еще 2 часа, а все уже на нервах..."
    "Вы берете телефон"
    menu:
        artem "Доброе утро [name_], ты ведь не забыл какой сегодня день?"
        "Ой, кажется забыл, можешь напомнить?":
            artem "Хватит дурачится, за еду за тобой через час, отправимся в институт, будь готов"
            "*сбросил трубку*"
            gg "И как в сообществе преданных игровых гиков оказался такой душнила..."
        "Конечно, как о таком забыть?":
            artem "Отлично заеду за тобой через час, поедем в институт"
            "*сбросил трубку*"
    jump road_to_Institute

label road_to_Institute:
    scene black with fade
    "Спустя час"
    scene machine with dissolve
    "Вы садитесь в машину к Артему"
    scene road with dissolve
    gg "Привет, Тема, как спалось?"
    menu:
        artem "Сегодня великий день, наша команда шла к этому долгое время, будущее компьютерных игр зависит только от тебя."
        "Да, да, да. А спалось как?":
            artem "Зря тебе доверили такую ответственную роль, ты слишком не серьезен. Скажи спасибо, что Алиса настояла на твоей кандидатуре."
            gg "И я тебя люблю"
        "Не переживай, я не подведу":
            artem "Надеюсь.."
    gg "Расскажи какой у нас план действий, во сколько начинаем?"
    artem "Вначале Павел, как лидер проекта, скажет речь, потом ты пройдешь небольшой инструктаж и можем начинать."
    jump institute
label institute:
    scene institut with dissolve
    artem "Приехали, нас уже ждут в коворкинге"

