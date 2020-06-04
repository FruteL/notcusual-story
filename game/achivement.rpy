transform achievement_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 2.2 yalign .02

screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    timer 3.0 action Hide("scr_achievement_get")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (550, 170)
        hbox:
            vbox:
                spacing 30
                image icon xalign 0.5 yalign 0.5
            vbox:
                xoffset 10
                spacing 10
                xsize 330
                text title:
                    size 48
                    color ("#FFFFFF")
                    #font "fonts/chalk.ttf"
                    id title
                text a_text:
                    size 40
                    color ("#80D4FF")
                    #font "fonts/chalk.ttf"
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text


                



init python:
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        achievement.grant(ach_id)
        renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                          a_text=ach['text'], icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                          icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)




    # Define your achievements here
    if not persistent.achievements_dict:
        persistent.achievements_dict = { "start": {"type": 0, # One time achievent
                                                             "title": "Начало!", # Also neame for steam
                                                             "text": "Что будете заказывать?", # description
                                                             "icon": "images/ach/ach1.png" #160x160 image
                                                             },
                                                             "Roma": {"type": 0, # One time achievent
                                                             "title": "Сочувствие", # Also neame for steam
                                                             "text": "Ему же нет 18!", # description
                                                             "icon": "images/ach/ach2.png"
                                                             },
                                                             "Kate": {"type": 0, # One time achievent
                                                             "title": "Рыжее счастье", # Also neame for steam
                                                             "text": "И было очень близко", # description
                                                             "icon": "images/ach/ach3.png"
                                                             },
                                                             "Alone": {"type": 0, # One time achievent
                                                             "title": "Титан одиночества", # Also neame for steam
                                                             "text": "С лицом пленника Освенцима ", # description
                                                             "icon": "images/ach/ach4.png"
                                                             },
                                                             "Vas": {"type": 0, # One time achievent
                                                             "title": "Новое начало", # Also neame for steam
                                                             "text": "Carpe diem ", # description
                                                             "icon": "images/ach/ach5.png"
                                                             }
                                        }
                                        
## Achievement Screen ###############
###
### Just for seeing your Achievement####
###
########

screen achi():
    tag menu
    style_prefix "achi"
    add im.FactorScale("gui/menus/main_menu.png", 1.7)
    text "Список достижений" xalign 0.5 yalign 0.1
    vbox:
        spacing 30
        yalign 0.5
        xalign 0.5
        style_prefix("achi_text")
        for i, a in reversed(persistent.achievements_dict.items()):
            window:
                background "#333333cc"
                xysize (850, 160)
                if (achievement.has(i)):
                    hbox:
                        spacing 20
                        image a['icon']
                        vbox:
                            spacing 10
                            text a['title'] size 60 color ("#80D4FF")
                            text a['text']
                else:
                    hbox:
                        spacing 20
                        image "images/ach/not_get.png"
                        vbox:
                            spacing 10
                            text "???" size 60 color ("#80D4FF")
                            text ""
                            text "?????????"
    #textbutton _("Очистить все достижения") xalign 0.5 yalign 0.8 action Achievement.clear_all()
    textbutton _("Вернутся") xalign 0.1 yalign 0.95 action Return()
 
style achi_button_text is gui_text:
    size 100
    color ("#FFFFFF")
    font "fonts/chalk.ttf"
style achi_text:
    size 100
    color ("#FFFFFF")
    font "fonts/chalk.ttf"
style achi_text_text:
    size 40
    color ("#FFFFFF")
    font "fonts/chalk.ttf"