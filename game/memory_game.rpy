label simongame (difficulty=0, endgame=0,goquick=0):
    #это Кодировка старая игра последовательность Саймон.
#Во-первых, определить какую-то переменную и сброс счетчиков.
    $ sequence=[] #последовательность ответа.
    $ nowpush=0#последовательности итератор
    $ thecolor=0#кнопку Вы должны нажать.
    $ maxtry = 2
   
label turnsequence: #теперь вызовем рандомизатор, чтобы добавить знаки.
    python:
        for i in range (0,difficulty):
            added=renpy.random.randint(0,3)   
            sequence.append(added)
    $nowpush=0
   
label showthesequence: #теперь показывают на экране, которые отображают последовательность
    if nowpush==len(sequence):
        jump theguessin#отскочить, если последовательность завершена
    show screen voidgame
    $ renpy.pause(0.5,hard=True)
    show screen displaysequence
    hide screen voidgame
    $ renpy.pause(0.5,hard=True)
    if nowpush< len(sequence):
        $ nowpush+=1
    jump showthesequence

label theguessin:#этот ярлык подготовить экран, скрывая то, что осталось от предыдущих
    $ nowpush=0
    hide screen displaysequence
  #Теперь вызовем на экране ввода данных
    $ nowpush=0
label guessthesequence: #сейчас ввод команд игрока, чтобы повторить последовательность
    if nowpush==len(sequence):
        jump turnsequence #если завершить, повторить сначала
    call screen inputcolor
    $ myguess=_return #вот нажатой кнопки
    $ theright =sequence[nowpush]#правильный кнопку, которую нужно нажать в данный момент
    if theright==myguess:
        $nowpush+=1
        if nowpush==(endgame):
            jump winner
        jump guessthesequence
    if theright!=myguess:
        $ curtry = curtry + 1
        if curtry == maxtry:
            jump looser
        jump memory_game
label winner:#в messagge для определения победы
    "Ты выиграл!"
    return
label looser: #сообщение
    "Ты проиграл!"
    return

   
screen displaysequence:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        if sequence[nowpush]==0:
            add "redon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==1:
            add "blueon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==2:
            add "greenon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==3:
            add "yellowon.png"
        else:
            add "buttonoff.png"
screen voidgame:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        add "buttonoff.png"
        add "buttonoff.png"
        add "buttonoff.png"
        add "buttonoff.png"
   
screen inputcolor:
    use racetheclock(goquick) #this is a moving bar, so techie!
    text "Ваша очередь" xalign 0.5 yalign 0.9
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        imagebutton idle "buttonoff.png" hover "redon.png" action Return(0)
        imagebutton idle "buttonoff.png" hover "blueon.png" action Return(1)
        imagebutton idle "buttonoff.png" hover "greenon.png" action Return(2)
        imagebutton idle "buttonoff.png" hover "yellowon.png" action Return(3)
       

screen racetheclock(goquick):
    $ mytime=AnimatedValue(value=10.0, range=10.0, delay=goquick, old_value=0.0)
    bar value mytime xalign 0.5 yalign 0.1 xsize 500
    timer goquick action Jump("too_slow")
   
label too_slow:
    "Время вышло!"
    return
    
   


# Игра начинается здесь.
label memory_game:
    "Повторите теже самые кнопки что мигают"
    call simongame pass (difficulty=1,endgame=5,goquick=5)
    "ну вот и все"

    jump start
