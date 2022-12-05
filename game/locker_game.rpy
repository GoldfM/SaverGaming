init python:

    numbl = 0

    numbc = 0

    numbr = 0

screen safe_code:

    modal True

    add "images/safe_i/cl_panel.png" align .5, .5 zoom 1.4

    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .320 yalign .345 action If(numbl < 9, SetVariable("numbl", numbl + 1), SetVariable("numbl", 0)) 
    add "images/safe_i/cl_%s.png"%(numbl) xalign .32 yalign .51 zoom 1.2
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .320 yalign .668 action If(numbl > 0, SetVariable("numbl", numbl - 1), SetVariable("numbl", 9))

    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .419 yalign .345 action If(numbc < 9, SetVariable("numbc", numbc + 1), SetVariable("numbc", 0))
    add "images/safe_i/cl_%s.png"%(numbc) xalign .42 yalign .51 zoom 1.2
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .419 yalign .668 action If(numbc > 0, SetVariable("numbc", numbc - 1), SetVariable("numbc", 9))

    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .517 yalign .345 action If(numbr < 9, SetVariable("numbr", numbr + 1), SetVariable("numbr", 0))
    add "images/safe_i/cl_%s.png"%(numbr) xalign .52 yalign .51 zoom 1.2
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .517 yalign .668 action If(numbr > 0, SetVariable("numbr", numbr - 1), SetVariable("numbr", 9))

    imagebutton auto "images/safe_i/enter_btn_%s.png" focus_mask True yalign .61 xalign .691 action If(numbl == 7, If(numbc == 1, If(numbr == 5, Jump("test"), Show("access_denied")), Show("access_denied")), Show("access_denied"))


screen access_denied:
    modal True
    text "Wrong Password!!!" size 50 xalign 0.5 yalign 0.32
    textbutton "Try Again" xalign 0.5 yalign 0.45 action Hide("access_denied")

label locker:
    scene bg
    call screen safe_code
    "Введите пароль"
    scene bg
    jump start
