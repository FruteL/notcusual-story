image bg disc = im.FactorScale("gui/menus/main_menu.png", 1.7)
image disp = "images/ach/disc.png"
label splashscreen:
    init python:
        persistent.m = 0
    scene bg disc with dissolve
    show disp with dissolve
    pause 15
    hide disp with dissolve
    pause 1
    $ persistent.m = 1
    return
    
label credits:
    scene black with dissolve
    show text "Автор идеи {p} Кандеев Павел {p}{p}Главный Сценарист {p} Кандеев Павел {p}{p}Бетта-ридер {p} Пилипенко Влада {p}{p}Художник {p} Пилипенко Влада {p}{p}Гейм-дизайнер {p} Пилипенко Влада {p}{p}Главный кодер {p} Кандеев Павел{p}{p}Работа со звуком {p} Кандеев Павел{p}{p}Get some ideas{p} Hideo Kojima" at text_slide_up
    pause 25
    return
    
init:
    transform text_slide_up:
        yalign 3
        linear 30 yalign -1.5