# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    menu:
        "Во будем поиграем?"
        "Memory":
            $ curtry = 0
            jump memory_game
        "RPS":
            jump RPS_game
        "Drag and droup":
            jump DragNDrop
        "Locker":
            jump locker
    return

