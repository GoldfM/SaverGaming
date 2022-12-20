# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init python:
    count_adds = 0
    dictDND = {'situation1': 'null', 'situation2': 'null', 'situation3': 'null'}
    def drag_place(drags, drop):
        global left_dropable, right_dropable, count_adds


        if not drop:
            return

        dictDND[drop.drag_name] = drags[0].drag_name
        count_adds+=1
        drop.droppable=False
        drags[0].draggable = False
        if count_adds==3:
            return True
        return
# The game starts here.

label DragNDrop:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    scene tech
    define instruct = Character(None, kind=nvl, color="#c8c8ff")

    "Ты должен прослушать аудиозаписи снизу, а затем соотнести каждую из них со сценой, наиболее подходящей для ее использования"
    "Перетащи кружок с номером, соответствующим номером аудиозаписи на картинку из сцены, которая наиболее подходит для данной мелодии"
    call screen drag_sample2


    
    if dictDND['situation1'] == 'song' and dictDND['situation2'] == 'dance' and dictDND['situation3'] == 'battle':
        $add_score=5
        $game_checker = True
    else:
        $add_score=0
        $game_checker = False
    $score = score + add_score

screen drag_sample2:
    modal True
    draggroup:
        drag:
            drag_name "battle"
            child "/images/DragNDrop/num1.png"
            xpos 0.1
            ypos 0.6
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "song"
            child "/images/DragNDrop/num2.png"
            xpos 0.4
            ypos 0.6
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "dance"
            child "/images/DragNDrop/num3.png"
            xpos 0.7
            ypos 0.6
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "situation1"
            xpos 0.1
            ypos 0.2
            child "/images/DragNDrop/song.jpg"
            draggable False
            droppable True
        drag:
            drag_name "situation2"
            xpos 0.4
            ypos 0.2
            child "/images/DragNDrop/dance.jpg"
            draggable False
            droppable True
        drag:
            drag_name "situation3"
            xpos 0.7
            ypos 0.2
            child "/images/DragNDrop/battle.jpg"
            draggable False
            droppable True
    imagebutton:
        xalign 0.1
        yalign 0.95
        idle "images/DragNDrop/btn1.png"
        action Play('sound', '/sounds/DragNDrop/battle.mp3')
    imagebutton:
        xalign 0.4
        yalign 0.95
        idle "images/DragNDrop/btn1.png"
        action Play('sound', '/sounds/DragNDrop/song.mp3')
    imagebutton:
        xalign 0.7
        yalign 0.95
        idle "images/DragNDrop/btn1.png"
        action Play('sound', '/sounds/DragNDrop/dance.mp3')

screen drag_sample3:
    draggroup:
        drag:
            drag_name "situation1"
            xpos 0.1
            ypos 0.6
            child "/images/DragNDrop/sit1.jpg"
            draggable False
            droppable False
        drag:
            drag_name "situation2"
            xpos 0.4
            ypos 0.6
            child "/images/DragNDrop/sit2.jpg"
            draggable False
            droppable False

        drag:
            drag_name "situation3"
            xpos 0.6
            ypos 0.6
            child "/images/DragNDrop/sit3.jpg"
            draggable False
            droppable False