
init:
    $ time = 5
    $ p_choise = 0
    $ enemy_choices = ["rock", "paper", "rock", "scissors", "scissors"]
    $ num_game = 0
    $ enemy_ch = ""
    $ first = 0

style button_text:
    color "#fff"
    selected_color "#ff0"

define points = 0

screen knb_timer:
    timer time repeat True action [Hide('knb_game_buttons'), Show('knb_game_result')]
    bar value AnimatedValue(0, time, time, time) xmaximum 200 xalign 0.5 yalign 0.05

screen knb_game_buttons:
    modal True
    use knb_timer
    add '/images/RPS/' + enemy_ch + '_idle.png' align .5, .3
    hbox:
        align .5, .5
        imagebutton auto '/images/RPS/rock_%s.png' focus_mask True action [Play('sound', '/audio/done_1.mp3'), SetVariable('p_choise', 'rock'), SelectedIf(p_choise == 'rock')] hovered Play('sound', '/audio/odd2.mp3')
        imagebutton auto '/images/RPS/scissors_%s.png' focus_mask True action [Play('sound', '/audio/done_1.mp3'), SetVariable('p_choise', 'scissors'), SelectedIf(p_choise == 'scissors')] hovered Play('sound', '/audio/odd2.mp3')
        imagebutton auto '/images/RPS/paper_%s.png' focus_mask True action [Play('sound', '/audio/done_1.mp3'), SetVariable('p_choise', 'paper'), SelectedIf(p_choise == 'paper')] hovered Play('sound', '/audio/odd2.mp3')

screen knb_game_result:
    modal True
    add '/images/RPS/' + enemy_ch + '_idle.png' align .5, .3
    if enemy_ch == p_choise:
        text 'Ничья!' align .77, .5
        python:
            global points
            points = points + 1
    elif enemy_ch == 'rock' and p_choise == 'scissors':
        text 'Ты проиграл!!!' align .77, .5
    elif enemy_ch == 'rock' and p_choise == 'paper':
        text 'Ты победил!!!!' align .77, .5
        python:
            global points
            points = points + 3
    elif enemy_ch == 'paper' and p_choise == 'scissors':
        text 'Ты победил!!!' align .77, .5
        python:
            global points
            points = points + 3
    elif enemy_ch == 'paper' and p_choise == 'rock':
        text 'Ты проиграл!!' align .77, .5
    elif enemy_ch == 'scissors' and p_choise == 'paper':
        text 'Ты проиграл!!' align .77, .5
    elif enemy_ch == 'scissors' and p_choise == 'rock':
        text 'Ты победил!!' align .77, .5
        python:
            global points
            points = points + 3
    else:
        text 'Ты не сделал выбор' align .77, .5
        $ num_game = num_game - 1
    if p_choise <> 0:
        add '/images/RPS/' + p_choise + '_idle.png' align .5, .6
    #text '' + str(points) + '' align .1, .2
    imagebutton auto '/images/RPS/next_%s.png' focus_mask True action [Hide ('knb_game_result'), Jump('start_game')] hovered Play('sound', '/audio/odd2.mp3') align .75, .65



label RPS_game:
    scene ai with dissolve
    $ p_choise = 0
    e 'Научи искусственный интеллект побеждать! Правила простые. Камень бьет Ножницы, Ножницы бьют Бумагу, Бумага бьет Камень!'
    jump knb_play
    
label start_game:
    scene ai with dissolve
    $ p_choise = 0
    if num_game < 5:
        jump knb_play
    else:
        jump to_end

label to_end:
    if points > 14:
        jump sucess
    else:
        jump failed

label knb_play:
    python:
        enemy_ch = enemy_choices[num_game]
        p_choise = 0
    $ num_game = num_game + 1
    show screen knb_game_buttons
    scene ai
    pause

label sucess:
    $add_score = 10
    $score = score + add_score
    scene computer office intellect
    marcey "Ты отлично справился, тренажер конечно сильно отличается от реальности, но все же ты показал достойный результат"
    return

label failed:
    $ p_choise = 0
    $ enemy_ch = ""
    scene computer office intellect
    marcey "Не расстраивайся, у тебя все еще впереди"
    $ points = 0
    $ num_game = 0
    return