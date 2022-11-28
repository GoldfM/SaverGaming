﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#25ff25")
define AIHome = Character('Умный дом', color = "#ff6600", image = 'robot')
define gg = Character('Вы', color = "#00fff7")
define artem = Character('Артем', color = "#dc3936", image = 'artem')
define alice = Character('Алиса', color = "#dc36c3",image = 'alice')
define pasha = Character('Паша', color = "#4736dc")
define admin = Character('Администратоп', color = "#12a4ab", image = 'receptionist')
define adam = Character('Адам Качинский', color = "#12a4ab")
define marcin = Character('Марцин Блаха', color = "#12a4ab")
define mihal = Character('МИХАЛ', color = "#12a4ab")



define phone_ = Character('Телефон', color = "#a4bda7")
define audio.phone_call = "sounds/rington.mp3"
define audio.aplodisment = "sounds/aplodisment.mp3"
define score = 0
define add_score=0
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init python:
    
    onn = ImageDissolve("eye.png", 0.9, 20, reverse=False) 
    off = ImageDissolve("eye.png", 0.7, 10, reverse=True) 
label start:
    #play music "music/fiesta.mp3"
    
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
        "Вы чувствуете себя очень усталым, и готовы пожертвовать всем ради нескольких часов сна"
        "Спать дальше":
            call sleep from _call_sleep
        "Встать, вопреки всему":
            call wake_up from _call_wake_up
    
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
    stop sound
    "Вы берете телефон"
    menu:
        artem "Доброе утро [name_], ты ведь не забыл какой сегодня день?"
        "Ой, кажется забыл, можешь напомнить?":
            artem @ annoyed"Хватит дурачится, за еду за тобой через час, отправимся в институт, будь готов"
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
            artem @ annoyed "Зря тебе доверили такую ответственную роль, ты слишком не серьезен. Скажи спасибо, что Алиса настояла на твоей кандидатуре."
            gg "И я тебя люблю"
        "Не переживай, я не подведу":
            artem "Надеюсь.."
    gg "Расскажи какой у нас план действий, во сколько начинаем?"
    artem "Вначале Павел, как лидер проекта, скажет речь, потом ты пройдешь небольшой инструктаж и можем начинать."
    jump institute
label institute:
    scene institut with dissolve
    artem "Приехали, нас уже ждут в коворкинге"
    scene institut inside with dissolve
    "Как только вы входите вас окликает женский голос"
    show alice at right with dissolve
    menu:
        alice "Привет, как спалось?"
        "Нормально..":
            alice "Отлично, кстати, хорошие новости, я буду курировать тебя на протяжении всего твоего \"путешествия\". Так что в любой непонятной ситуации можешь на меня положиться"
        "Я спал 4 часа, зачем начинать так рано?":
            alice "Ой да ладно, для заядлого игромана это небольшая проблема. Кстати, хорошие новости, я буду курировать тебя на протяжении всего твоего \"путешествия\". Так что в любой непонятной ситуации можешь на меня положиться"

    menu:
        "Я и сам прекрасно справлюсь":
            alice "Какие мы самоуверенные, так или иначе я всегда буду на связи"
        "Отлично, вдвоем веселее":
            alice "Я тоже так думаю"
    alice "Пошли, Паша сейчас начнет выступать"
    hide alice with dissolve
    scene institut inside two with fade
    show pavel at left
    pasha "Ребята сегодня великий день для всего игрового сообщества. В этой комнате собрались самые преданные фанаты игровой индустрии."
    pasha "Как вы все знаете, после так называемого игрового кризиса30-ых годов игровая индустрия пришла в упадок. Компании начали делать игры ради выручки, а толковых разработчиков становилось все меньше и меньше."
    pasha "Постепенно игры деградировали и интерес к новым продуктам отпал. Последняя игра вышла 63 года назад."
    pasha "Но даже несмотря на это в мире остаются преданные делу геймеры, они пересматривают старые киберспортивные матчи, играют в игры 70 летней давности."
    pasha "Именно из таких людей состоит наша команда 'Pheonix'. Каждый из нас свято верит в возрождение игровой индустрии и прикладывает для этого все возможные услилия"
    pasha "И сейчас мы как никогда близки к этому. Сегодня [name_] отправится в 2012 год во времена разработки одной из лучших игр человечества, которую я уверен, каждый из вас проходил не один раз -Ведьмак 3."
    pasha "[name_] вместе с командой разработчиков CD project red пройдет путь создания этой культовой игры, чтобы мы могли собрать все необходимые для гейм-девелопера знания. Некогда популярной, но ныне мертвой профессии"
    pasha "Если сегодня все пройдет по плану наша научно-исследовательская команда превратится в студию разработки игр 'Pheonix'"
    pasha "На этом у меня все."
    play sound aplodisment
    pasha "Да прибудет с нами сила."
    alice "Не будем терять времени. Пошли в лабораторию, проведем последний инструктаж и в бой!"
    alice "[name_], за мной"
    stop sound
    jump prepare_for_travel

label prepare_for_travel:
    scene time_machine with fade
    "Вы заходите в комнату, где установлена машина времени 'Phoenix 12'"
    alice "Впечатляет, не правда ли? Ума не приложу, как Паша выпросил разрешение на ее использование у университета. Наши ученые не любят отправлять в прошлое абы-кого."
    menu:
        "У нас влиятельные спонсоры":
            alice "Тут не поспоришь, Паша смог заинтересовать несколько крупных компаний нашим проектом. Они помогают нам с оборудованием и финансами."
            menu:
                alice "Каждая из них надеется получить большую прибыль от наших будущих игр. А ведь это когда-то и погубило индустрию..."
                "Мы не повторим ошибок прошлого.":
                    alice "Для начала давай отправимся в прошлое и научимся делать игры"
                "Много денег - это всегда хорошо":
                    alice @ annoyed"Какой ты циничный, аж противно! В \"Phoenix\" все работают за идею."
        "Паша не последний человек в университет":
            alice  "Павел Борисович работает в университете уже 10 лет, из которых 5 лет он посвятил этому проекту. Упорства ему не занимать, слишком много сил и времени он потратил на эту авантюру, поэтому никакие преграды его не остановят."
            gg "Повезло нам с руководителем"
            alice "Да, он душка!"
    alice "А теперь давай перейдем к инструктажу" 
    alice "Давай. Я уверена, ты все прекрасно знаешь и помнишь. Но, по протоколу, я должна провести этот инструктаж."
    alice "Итак, перед началом работы ты получишь специальный передатчик, в виде гарнитуры, с помощью которой мы сможем поддерживать связь в прошлом"
    alice "Так же возьми документы некого Феликса Вуйчика польского студента, которому CD project red разрешила наблюдать за созданием 3 Ведьмака, с целью обучения."
    alice " Этого человека, можно сказать, создали наши ребята: придумали ему биографию, сделали паспорт, внесли во все возможные реестры в прошлом и договорились о его обучении с CD project-ами."
    alice "Как тебе уже миллион раз говорили, никто в прошлом не должен узнать, кто и откуда ты на самом деле, иначе крышка нашей будущей великой студии."
    alice "Вроде все, если что ты всегда сможешь позвать меня и я отвечу, а в случае чего верну тебя обратно в настоящее."
    alice "Ах ну и конечно, в прошлом твоя задача - узнать как можно больше про три отрасли гейм-девелопинга: дизайн (визуальная состовляющая игры), написание сценария и непосредственно реализация проекта (написание кода)"
    alice "Вопросы?"
    jump questions

label questions:
    menu:
        "Сколько времени я проведу в прошлом?":
            alice "Университет разрешил нам отправить тебя только на один день, так что действовать придется оперативно."
            jump questions
        "Что случится, если кто-то узнает, что я из прошлого?":
            alice "Уфф, не знаю и знать не хочу, уверена, что ничего хорошего"
            jump questions
        "Напомни, а почему именно Ведьмак 3?":
            alice "В этой игре прекрасно все: сюжет, графика, различные механики, дизайн локаций и т. д. Отличный пример для подражания."
            alice "Ну и это любимая игра Паши."
            jump questions
        "Вопросов нет":
            jump end_prepare
label end_prepare:
    alice "Тогда приступим! Садись в кресло."
    alice "Положи руки на подлокотники и закрой глаза."
    alice "Все, хорошего путешествия! Не подведи нас!"
    scene black with off
    image animated2 = Movie(play="time_lapse.ogv", pos=(0,0), anchor=(0, 0))
    scene animated2
    with Pause(7)
    jump start_travel

label start_travel:
    scene officeout with fade
    gg "Уфф, тошнотворная процедура"
    menu:
        alice "А ты крепкий, обычно людей выворачивает сразу после перемещения. Как слышно?"
        "Могла бы и предупредить":
            alice"Зачем? Ты бы только напрягся лишний раз"
        "Слышно хорошо":
            alice"Отлично"
    alice"Заходи внутрь"
    scene office with fade
    show receptionist at right
    admin "День добрый, молодой человек, вы к кому?"
    gg "Я студент, у меня сегодня назначена небольшая экскурсия"
    menu:
        admin"Имя фамилию, будьте добры"
        "[name_]":
            call name_not_in_base from _call_name_not_in_base
        "Джим Керри":
            call name_not_in_base from _call_name_not_in_base_1
        "Феликс Вуйчик":
            pass
        "*Шепотом позвать Алису*":
            alice facepalm "Ты издеваешься? Феликс Вуйчик, не тупи!"
            gg "Феликс Вуйчик"
    admin "Хорошо, ждите здесь, за вами сейчас придут"
    scene black with fade
    "{cps=10}Спустя 5 минут{/cps}"
    jump talk_with_adam
label name_not_in_base:
    admin "В базе вы не записаны"
    alice @ facepalm "Дурак, ты все испортишь! Феликс Вуйчик"
    gg "По документам, я Джордж Якоби, то мой псевдоним"
    "Администратор посмотрела на вас, как на сумасшедшего, но, проверив ваши документы, принялась еще раз проверять базу"
    alice @ facepalm "{cps=10}Придурок.{/cps}"
    return

label talk_with_adam:
    scene adam with fade
    adam "Добрый день, Феликс, приятно видеть молодых энтузиастов в нашем офисе, я Адам Кичинский - глава студии CD project red. Надеюсь, сегодняшний экскурс по нашему офису будет полезным для вас."
    menu:
        adam "Перед тем как мы начнем, позвольте вопрос, что привело вас в игровую индустрию?"
        "Желание разбогатеть":
            $add_score = 0
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            adam "Деньги - это хорошо, но на одном желании разбогатеть далеко не уйдешь... Успех в игровой индустрии напрямую зависит от того, насколько ты любишь то, что ты делаешь."
        "Любовь к играм":
            $add_score = 5
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            adam "Да, многие  фанаты игровой культуры приходят работать эту сферу. Но нужно учесть, что процесс разработки игр сильно отличается от прохождения готовых продуктов. Это тяжелый труд, который не всем приходится по вкусу."
        "Желание создать собственную студию, чьи проекты покорят людей по всему миру":
            $add_score = 10
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            adam "Хороший ответ, надеюсь, у вас все получится. Сегодня наша сфера нуждается в толковых специалистах."
    if add_score>0:
        alice "Ты же понимаешь, что в зависимости от твоих действий будет определяться успех нашего проекта?"
    else:
        alice @ annoyed "Ты же понимаешь, что в зависимости от твоих действий будет определяться успех нашего проекта?"

    adam "Я думаю, можно приступать к экскурсии, наша студия сейчас работает над новой игрой по миру Ведьмака."
    adam "Сегодня вы посетите отдел дизайна, гейм-дизайна и разработки. Начнем с наших гейм-дизайнеров. Идите за мной."
    jump game_design

label game_design:
    scene marcin with fade
    marcin "Добро пожаловать в отдел игрового дизайна, я Марцин Блаха, ведущий сценарист компании."
    menu:
        "Приятно познакомиться, я Феликс Вуйчик":
            $add_score = 5
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            pass
        "Упасть на колени и боготворить его":
            $add_score = 0
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            "На вас посмотрели как на сумасшедшего и подняли на ноги"
        "Очень приятно, для меня это огромная честь общаться с человеком, который написал сценарий к культовому Ведьмаку 3.":
            $add_score = 0
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            marcin "Спасибо большое, я польщен. Но вы что-то путаете, я только работаю над ним"
            "Неловкое молчание..."
            alice @ facepalm "Баран"
        "И что? А я Феликс Вуйчик":
            $add_score = 0
            $score = score + add_score
            #$renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
            marcin "Кхм. Приятно познакомиться, Феликс Вуйчик"

    marcin "Давайте начнем экскурсию в мир разработки игр"
    marcin "Работа гейм-дизайнера играет очень важную роль в создании продукта. Мы отвечаем за все ключевые аспекты игры."
    marcin "От нас зависит будет ли игра успешной."
    marcin "Продукт может быть идеально запрограммирован, а модели будут поражать игрока своей красотой, но если за этим великолепием не будет хорошего сюжета, гармоничной атмосферы и продуманного баланса, проект обречен на провал."
    marcin "Дизайнеры и программисты лишь воплощают наши идеи, без нас не может обойтись ни одна игра."
    marcin "Пойдем к проектору, там я наглядно все покажу и расскажу."
    marcin "Начнем с главного - это конечно же сценарий, у любой игры должен быть хоть какой-нибудь сюжет, определяющий ее цель для игрока. В нашем новом проекте мы взяли за основу сюжета цикл книг Анджея Сапковского \"Ведьмак\"."
    marcin "Моя задача, как сценариста, создать интересную историю для игрока, которая заставит его проникнуться миром  писателя, также я работаю над внутриигровыми диалогами."
    marcin "Гейм-дизайнер также продумывает, как будут выглядеть персонажи, локации и предметы в игре, а еще подбирает музыкальное сопровождение, затем передает свое представление дизайнерам, которые пытаются воплотить его задумки."
    marcin "Таким образом мы создаем атмосферу игры, ее настроение."
    marcin "Кстати музыкальное сопровождение очень важная часть игры. Подобрать правильные композиции не всегда бывает легко."
    marcin "Хочешь попробовать себя в роли гейм-дизайнера? Попробуй подобрать музыку к трем сценам из нашей новой игры."
    $game_checker = False
    
    call DragNDrop from _call_DragNDrop
    stop sound
    #$ renpy.notify(f"Количество ваших очков: {score} (+{add_score})")
    if game_checker:
        marcin"Да у тебя талант парень!"
    else:
        marcin "Не лучший выбор как по мне, ну да все приходит с опытом"
    marcin "Также на нашем отделе лежит ответственность за создание так называемого нарративного дизайна. То есть создание повествования через кассеты, дневники, записки, описание предметов. "
    marcin "Также нарративный дизайнер следит за тем, чтобы сюжет и геймплей не шли отдельно друг от друга. Условно говоря, следит, чтобы не было несостыковок. Вот кстати пример записки из игры."
    marcin "В общем и целом, профессия геймдизайнера подразумевает под собой полную разработку идей игры. Гейм-дизайнер обязан обладать творческим мышлением."
    marcin "То есть, если ты чувствуешь в себе недостаток креативности и воображения, то скорее всего, тебе лучше выбрать другую профессию."
    marcin "Но не только воображение важно в нашей профессии, гейм-дизайнер отвечает за концепции механик игры, а также за игровой баланс, то есть чтобы игра не была слишком простой или сложной."
    marcin "Да и вообще, мы напрямую работаем с отделом разработки и дизайна, поэтому мы должны трезво оценивать наши технические возможности, поэтому знания в областях дизайна и программирования для нас лишними не будут."
    marcin "На этом у меня, пожалуй, все."
    jump questions_marcin
label questions_marcin:
    menu:
        marcin "Готов ответить на твои вопросы, если они есть."
        "Сколько составляет средняя зарплата гейм-дизайнера?":
            marcin "Сложно сказать, все зависит от твоего опыта, заслуг, компании в которой ты работаешь. Но на первых парах, как мне кажется, денег много не заработаешь, пока не сделаешь себе имя. В общем, все в твоих руках!"
        "Что вы можете посоветовать начинающим гейм-дизайнерам?":
            marcin "Тяжелый вопрос, наверное, больше читать, книги развивают воображение, а оно крайне нужно в нашем деле. Тем более работа писателей во многом схожа с нашей."
        "Что вы считаете главным в своей работе?":
            marcin "Ох, так сразу и не скажешь. Цель нашей профессии - создать интересный, наполненный яркими красками игровой мир, который сможет увлечь игроков. Каждый успешный продукт обладает своей фишкой, оригинальной идеей, способной удивить целевую аудиторию."
        "Вопросов нет, спасибо, что уделили время, было очень познавательно.":
            marcin "Всегда рад помочь, тогда все, тебе пора в отдел графического дизайна, удачи тебе в твоих начинаниях!"
            gg "Спасибо еще раз, всего доброго"
            jump design

    jump questions_marcin

label design:
    mihal "Привет, welcome. Ты тот самый студент, которому назначен небольшой экскурс в мир дизайна? Я Михал Мадей, один из главных дизайнеров компании"
    gg "Здравствуйте, рад знакомству"
    mihal "Ну что же, внимание на экран, я буду все рассказывать на примере нашей новой игры"
    mihal "Итак, в чем же заключается наша работа? Всё, что игрок видит непосредственно на мониторе -  работа графических дизайнеров."
    mihal "Как понятно из названия, данный отдел занимается графической составляющей игры, а этим являются анимации, спецэффекты, модели героев, текстуры мира, освещение, кат-сцены и прочее."
    mihal "Теперь подробнее пройдемся по основным составляющим"
    mihal "В первую очередь создаются концепт-арты  персонажей и окружения. На этом этапе работают с 2D."
    mihal "Художнику необходимо вжиться в  образ персонажа и отработать идею быстро и эффективно, представить персонажа, отразив все те его характеристики, которые заложены в техническом задании."
    mihal "Вот концепт-арты одной из героинь нашей новой игры, Трисс Меригольд и ее итоговая модель"
    mihal "Теперь о Моделях. Здесь работают с 3D. Люди этой профессии занимаются созданием высококачественных моделей персонажей и различных объектов игрового мира"
    mihal "При моделировании необходимо учитывать топологию модели, также нужно понимать, какие возможные коллизии могут происходить при том или ином движении модели. После завершения процесса создания все наработки модельера переходят к аниматору."

    mihal "Аниматоры “оживляют” персонажа. Сначала настраивают скелет персонажа, а затем придают необходимые движения посредством анимационных ключей, которые расставляются при том или ином нажатии кнопки. Аниматору не помешают базовые знания анатомии."
    mihal "Помимо персонажей аниматоры занимаются созданием динамичного окружения: благодаря им глаз игрока радуют травы, колыхающиеся на ветру, горящие в подземельях факела, дождь и другие нестатические явления."

    mihal "Также в дизайне есть отдельная команда, занимающаяся текстурами. Данная команда работает с различными поверхностями (лёд, вода, камень, металл)."
    mihal "Чем детальнее текстуры, тем лучше, но не стоит и забывать про производительность, которая может страдать от неоптимизированных объектов и анимаций."
    mihal "Также в команде есть люди, отвечающие  за освещение во всех локациях и сценах игры, они настраивают блики, яркость и интенсивность света каждой локации."
    mihal "Основная задача - найти баланс между светом и цветом и расставить необходимые акценты по ходу развития сюжета игры. Знания программирования здесь будут жирным плюсом."
    mihal "Ну и напоследок расскажу о UX и UI дизайне. Это создание пользовательского интерфейса. Определение темы, цветов, формы кнопок. Также сюда входит подбор шрифтов и определение макета интерфейса."
    mihal "UX и UI дизайнеры стремятся создать простой, удобный и стильный интерфейс. Гармоничный интерфейс всегда радует глаз."
    mihal "В общем и целом, всё что игрок видит на мониторе -  наша работа. Как понятно из названия наш отдел занимается графической составляющей игры, а этим являются анимации, спецэффекты, модели героев, текстуры мира, освещение, кат-сцены и прочее. "
    mihal "Чтобы работать в каком-либо ответвлении графического дизайна, помимо хорошего воображения неплохо иметь специфичные знания этого ответвления - теория цвета и свет, понимание ракурсов съемки, знание анатомии. Профессия достаточно креативная и интересная."
    mihal "Вот собственно говоря и все"
    jump questions_mihal
label questions_mihal:
    menu:
        mihal "Есть какие-нибудь вопросы?"
        "Дизайнер - прибыльная профессия?":
            mihal "Все зависит от твоего профессионализма, опыта и заслуг, как впрочем и везде. Я не жалуюсь"
        "Что, по вашему, главное в профессии графического дизайнера?":
            mihal "Любить свое дело, графический дизайнер - художник, задача которого воплотить в жизнь создавшийся в голове образ. Нельзя вымучивать из себя рисунок или модель, нужно, чтобы работа доставляла удовольствие, тогда успех не заставит себя ждать"
        "Можете  дать совет начинающим дизайнерам?":
            mihal "Конечно, рисуйте больше, пробуйте, экспериментируйте. делитесь своими работами на форумах, чтобы услышать критику. Чем больше у вас опыта, тем лучше"
        "Вопросов нет, спасибо за такую познавательную экскурсию":
            mihal "Всегда пожалуйста, рад бы пообщаться"
            "*Уходит*"
            alice "Отлично, остался последний рывок!"
            jump game_development
    jump questions_mihal

label game_development:
    "....."
