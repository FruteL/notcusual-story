################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"
    
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 500
    background Image(im.MatrixColor("gui/TextBox2.0.png", im.matrix.opacity(.75)), xalign=0.5, yalign=1.0)

style namebox:
    xpos 40
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos 10
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 40
    xsize 960
    ypos 140
    
   

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    #ypos 228
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        #textbutton _("M")
        imagebutton auto "gui/button/qmenu_%s.png" xalign 0.0 action ShowMenu('game_menu')

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.0
            spacing 40

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
        #imagebutton auto "gui/button/menubtn_%s.png" xalign 1.0 yalign 0.0 xsize 50 ysize 50 action ShowMenu()

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text
        

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 50


################################################################################
## Main and Game Menu Screens
################################################################################

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    python:
        if persistent.m == 1:
                renpy.music.queue("audio/gui/Stop Crying.mp3", channel = "music", fadein = 2)  
        renpy.music.set_volume(0.3, delay = 0, channel='music')
    
    tag menu
    
    style_prefix "main_menu"

    add im.FactorScale("gui/menus/main_menu.png", 1.7)
    
    text "Непростая" yalign 0.1 xalign 0.2 
    text "история" yalign 0.2 xalign 0.8 
    vbox:
        textbutton _("Начать") xalign 0.5 action Start()        
        textbutton _("Загрузить") xalign 0.5 action ShowMenu("load")
        textbutton _("Настройки") xalign 0.5 action ShowMenu("preferences")
        textbutton _("Достижения") xalign 0.5 action ShowMenu("achi")
        textbutton _("Выход") xalign 0.5 action Quit(confirm=not main_menu)

style main_menu_vbox:
    xmaximum 1200
    xalign 0.5
    yalign 0.75
    spacing 50
        
style main_menu_text is gui_text:
    size 170
    color ("#FFFFFF")
    font "fonts/chalk.ttf"
    
style main_menu_button_text is gui_text:
    size 120
    color ("#FFFFFF")
    font "fonts/chalk.ttf"  

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu():

    modal True
    tag menu
   
    style_prefix "game_menu"
    
    frame:
        has vbox
        textbutton _("Вернутся") xalign 0.5 action Return()
        textbutton _("Главное Меню") action MainMenu()
        textbutton _("Сохранить") xalign 0.5  action ShowMenu("save")
        textbutton _("Загрузить") xalign 0.5  action ShowMenu("load")
        textbutton _("Настройки") xalign 0.5 action ShowMenu("preferences")
        textbutton _("Выход") xalign 0.5 action Quit(confirm=not main_menu)
       
style game_menu_frame:
    xalign 0.5
    yalign 0.5
    xsize 850
    ysize 900
    #background 'gui/menus/game_menu.png'  
    background Frame(im.MatrixColor("gui/menus/game_menu.png", im.matrix.opacity(.75)), gui.frame_borders, tile=gui.frame_tile)
        
style game_menu_button_text is gui_text:
    size 100
    color ("FFFFFF")

style game_menu_vbox:
    xalign 0.5
    yalign 0.6
    spacing 20
    


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

default ch = 1
init python:
    config.thumbnail_height = 370
    config.thumbnail_width = 470
screen file_slots(title):

    add "gui/menus/save.png"
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    textbutton _("Вернутся") xalign 0.0 yalign 0.0 action Return()
    hbox:
        yalign 1.0
        xalign 0.5
        ymaximum 100
        spacing 20
        for i in range(1, 6):
            textbutton _("%d" % i) action FilePage(i)
    
    $ columns = 2
    $ rows = 3
    
    grid columns rows:
        yalign 0.5
        spacing 20
        xfill True
        ymaximum 1720
        for i in range (1, columns*rows + 1):
            button:
                xminimum 520
                xmaximum 520
                yminimum 430
                ymaximum 430
                background "gui/button/slot_background.png" 
                foreground "gui/button/slot_foreground.png" 
                action FileAction(i)
                

                add FileScreenshot(i) xalign 0.5 yalign 0.5
            
                $ file_name = FileSlotName(i, columns*rows)
                
        
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text


style slot_button is gui_button
style slot_button_text is gui_button_text:
    size 30
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style background:
    xmaximum 300
    
style button_text is gui_text:
    color("000000")

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    style_prefix "pref"
    add im.FactorScale("gui/menus/main_menu.png", 1.7)
    vbox:
          yalign 0.3
          spacing 100
          xalign 0.5
          text "Настройки" 
          vbox:
              spacing 60
              text "Text Speed"
              bar value Preference("text speed")
              text "Auto-Forward Time"
              bar value Preference("auto-forward time")
          vbox:
              spacing 60
              text "Music Volume"
              bar value Preference("music volume")
              text "Sound Volume"
              bar value Preference("sound volume")

          vbox:
              text _("Version [config.version!t]\n") 
    textbutton _("Вернутся") xalign 0.1 yalign 0.95 action Return()
    
style button_text is gui_text:
    size 80
    color ("#FFFFFF")
    font "fonts/chalk.ttf"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/hor_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/hor_[prefix_]thumb.png"
style pref_text is gui_text:
    size 80
    color ("#80D4FF")
    font "fonts/chalk.ttf"
    xalign 0.5
        
    
################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    
    if(message == layout.OVERWRITE_SAVE):
        $t = "Старое сохранение будет утеряно. Вы уверены?"
    if(message == layout.LOADING):
        $t = "Все несохраненные данные будут утеряны. Вы уверены?"
    if(message == layout.QUIT):
        $t = "Уверены?"
    if(message == layout.MAIN_MENU):
        $t = "Все несохраненные данные будут утеряны. Вы уверены?"
    
    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(t):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 85

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    size 70
    color ("#FFFFFF")
    font "fonts/chalk.ttf" 

style confirm_button:
    properties gui.button_properties("confirm_button") 

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 90
    color ("#FFFFFF")
    font "fonts/chalk.ttf" 


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 380

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 287

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 338

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    xsize 1000
    base_bar Frame("gui/slider/hor_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/hor_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 507
