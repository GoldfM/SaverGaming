﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#25ff25")
define AIHome = Character('Умный дом', color = "#ff6600", image = 'robot')
define gg = Character('Вы', color = "#00fff7")
define artem = Character('Артем', color = "#dc3936")
define alisa = Character('Алиса', color = "#dc36c3")
define pasha = Character('Паша', color = "#4736dc")



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

    $ name_ = renpy.input("Введите ваше имя", length=11, default = "Максим", allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ").strip()
    if name_ == "":
        $ name_ = "Максим"
    scene black with dissolve
    "{cps=10}Начинаем погружение,  [name_]{/cps}"
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
    AIHome "Сегодня 4 ноября 2106 года, температура в Москве -9 гардусов, к обеду потеплеет до -2, но лучше одевайтесь потеплее."
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
    "Как только вы входите вас окликает женский голос"
    menu:
        alisa "Привет, как спалось?"
        "Нормально..":
            alisa "Отлично, кстати, хорошие новости, я буду курировать тебя на протяжении всего твоего \"путешествия\". Так что в любой непонятной ситуации можешь на меня положиться"
        "Я спал 4 часа, зачем начинать так рано?":
            alisa "Ой да ладно, для заядлого игромана это небольшая проблема. Кстати, хорошие новости, я буду курировать тебя на протяжении всего твоего \"путешествия\". Так что в любой непонятной ситуации можешь на меня положиться"

    menu:
        "Я и сам прекрасно справлюсь":
            alisa "Какие мы самоуверенные, так или иначе я всегда буду на связи"
        "Отлично, вдвоем веселее":
            alisa "Я тоже так думаю"
    alisa "Пошли, Паша сейчас начнет выступать"
    scene cabinet with fade
    pasha "Ребята сегодня великий день для всего игрового сообщества. В этой комнате собрались самые преданные фанаты игровой индустрии."
    pasha "Как вы все знаете, после так называемого игрового кризиса30-ых годов игровая индустрия пришла в упадок. Компании начали делать игры ради выручки, а толковых разработчиков становилось все меньше и меньше."
    pasha "Постепенно игры деградировали и интерес к новым продуктам отпал. Последняя игра вышла 63 года назад."
    pasha "Но даже несмотря на это в мире остаются преданные делу геймеры, они пересматривают старые киберспортивные матчи, играют в игры 70 летней давности."
    pasha "Именно из таких людей состоит наша команда 'Pheonix'. Каждый из нас свято верит в возрождение игровой индустрии и прикладывает для этого все возможные услилия"
    pasha "И сейчас мы как никогда близки к этому. Сегодня [name_] отправится в 2012 год во времена разработки одной из лучших игр человечества, которую я уверен, каждый из вас проходил не один раз -Ведьмак 3."
    pasha "[name_] вместе с командой разработчиков CD project red пройдет путь создания этой культовой игры, чтобы мы могли собрать все необходимые для гейм-девелопера знания. Некогда популярной, но ныне мертвой профессии"
    pasha "Если сегодня все пройдет по плану наша научно-исследовательская команда превратится в студию разработки игр 'Pheonix'"
    pasha "На этом у меня все. Да прибудет с нами сила."
    "*Шквал апплодисментов*"
    alisa "Не будем терять времени. Пошли в лабораторию, проведем последний инструктаж и в бой!"
    alisa "[name_], за мной"
    jump prepare_for_travel

label prepare_for_travel:
    scene time_machine with fade
    "Вы заходите в комнату, где установлена машина времени 'Phoenix 12'"
    alisa "Впечатляет, не правда ли? Ума не приложу, как Паша выпросил разрешение на ее использование у университета. Наши ученые не любят отправлять в прошлое абы-кого."
    menu:
        "У нас влиятельные спонсоры":
            alisa "Тут не поспоришь, Паша смог заинтересовать несколько крупных компаний нашим проектом. Они помогают нам с оборудованием и финансами."
            menu:
                alisa "Каждая из них надеется получить большую прибыль от наших будущих игр. А ведь это когда-то и погубило индустрию..."
                "Мы не повторим ошибок прошлого.":
                    alisa "Для начала давай отправимся в прошлое и научимся делать игры"
                "Много денег - это всегда хорошо":
                    "Какой ты циничный, аж противно! В \"Phoenix\" все работают за идею."
        "Паша не последний человек в университет":
            alisa "Павел Борисович работает в университете уже 10 лет, из которых 5 лет он посвятил этому проекту. Упорства ему не занимать, слишком много сил и времени он потратил на эту авантюру, поэтому никакие преграды его не остановят."
            gg "Повезло нам с руководителем"
            alisa "Да, он душка!"
    alisa "А теперь давай перейдем к инструктажу"
    alisa "Давай. Я уверена, ты все прекрасно знаешь и помнишь. Но, по протоколу, я должна провести этот инструктаж."
    alisa "Итак, перед началом работы ты получишь специальный передатчик, в виде гарнитуры, с помощью которой мы сможем поддерживать связь в прошлом"
    alisa "Так же возьми документы некого Джорджа Якоби польского студента, которому CD project red разрешила наблюдать за созданием 3 Ведьмака, с целью обучения."
    alisa " Этого человека, можно сказать, создали наши ребята: придумали ему биографию, сделали паспорт, внесли во все возможные реестры в прошлом и договорились о его обучении с CD project-ами."
    alisa "Как тебе уже миллион раз говорили, никто в прошлом не должен узнать, кто и откуда ты на самом деле, иначе крышка нашей будущей великой студии."
    alisa "Вроде все, если что ты всегда сможешь позвать меня и я отвечу, а в случае чего верну тебя обратно в настоящее."
    alisa "Ах ну и конечно, в прошлом твоя задача - узнать как можно больше про три отрасли гейм-девелопинга: дизайн (визуальная состовляющая игры), написание сценария и непосредственно реализация проекта (написание кода)"
    alisa "Вопросы?"
    jump questions

label questions:
    menu:
        "Сколько времени я проведу в прошлом?":
            alisa "Университет разрешил нам отправить тебя только на один день, так что действовать придется оперативно."
            jump questions
        "Что случится, если кто-то узнает, что я из прошлого?":
            alisa "Уфф, не знаю и знать не хочу, уверена, что ничего хорошего"
            jump questions
        "Напомни, а почему именно Ведьмак 3?":
            alisa "В этой игре прекрасно все: сюжет, графика, различные механики, дизайн локаций и т. д. Отличный пример для подражания. Ну и это любимая игра Паши."
            jump questions
        "Вопросов нет":
            jump end_prepare
label end_prepare:
    alisa "Тогда приступим! Садись в кресло."
    alisa "Положи руки на подлокотники и закрой глаза."
    alisa "Все, хорошего путешествия! Не подведи нас!"