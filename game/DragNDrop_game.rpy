# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")

init python:
    count_adds = 0

    def drag_place(drags, drop):
        global left_dropable, right_dropable, count_adds


        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        count_adds+=1
        drop.droppable=False
        drags[0].draggable = False
        if count_adds==2:
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
    call screen drag_sample2


    
    e "{color=#000}{vspace=75}The [draggable] was put in [droppable]{/color}"

    jump start

    # This ends the game.

    return

screen drag_sample2:
    modal True
    draggroup:
        drag:
            drag_name "circle"
            child "/images/DragNDrop/circle.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "triangle"
            child "/images/DragNDrop/triangle.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "square"
            child "/images/DragNDrop/square.png"
            xpos 700
            ypos 100
            draggable True
            droppable False
            dragged drag_place
            drag_raise True
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "/images/DragNDrop/spot.png"
            draggable False
            droppable True
        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "/images/DragNDrop/spot.png"
            draggable False
            droppable True


screen drag_sample3:
    draggroup:
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "/images/DragNDrop/spot.png"
            draggable False
            droppable False
        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "/images/DragNDrop/spot.png"
            draggable False
            droppable False