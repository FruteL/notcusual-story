# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Катюша")
define r = Character("Рома")
image kate =  im.FactorScale("images/sprites/kate_usual_smile.png", 1.2)
image roma = im.FactorScale("images/sprites/Rome_.png", 1.2) 
image bg cafe = "images/background/cafe.jpg"

# The game starts here.

label start:
    stop music fadeout 2
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kate

    # These display lines of dialogue.

    e "Сюжет еще в разработке."
    e "Вскоре появиться сам Геймплей!"
    e "На паре этих строк можно проверить систему сейв/лоад"
    hide kate with dissolve
    show roma
    r "Увы. на данный момент нам больше нечего показать"

    # This ends the game.

    return
