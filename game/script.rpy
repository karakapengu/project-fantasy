#This is a custom dissolve transform
transform pindah:
    alpha 0.0
    xalign 1.0
    yalign 1.0
    linear .2 alpha 1.0 #This is the dissolve part, linear is the time
#####KARAKTER##########
define qq = Character("?????")
define f = Character("father")
define ai = Character("Aiden")
define ju = Character("Julie")
define ph = Character("Phyrie")
define ar = Character("Arthur")
define ru = Character("Ruby")
define k = Character("King")
define q = Character("Queen")
define b = Character("Blacksmith")
define al = Character("alia")

#Scene bg
image bg in1 = ("intro.png")
image bg in2 = ("intro2.png")
image bg da = ("dark.png")
##character image##
image dad = ("father.png")
image dad2 = ("father2.png")
#else#
define white = Fade(0.5, 1.0, 0.5, color="#fff")


label start:
    scene bg da with dissolve
    "That day...{w} I'm awake because of the ruckus outside."
    "so I go and check it out...{w} I can't believe what I'm seeing that day."
    show bg in1 with white
    "The village{w}, is attacked by a dragon"

    show dad with dissolve
    f "RUN AIDEN, GO FIND SOMEWHERE SAFE!"
    ai "Fa-father."
    hide dad
    show dad2
    f "I'll catch you soon!"
    hide dad2 with dissolve
    ai "DAD!!!"
    show bg da with dissolve
    "i does what father told me to do and go as far away from the village."
    "but...{w} when i comeback..."
    scene bg in2 with dissolve
    "It's finished."
    "Ugh, i feel dizzy{w}, i cant keep-" with vpunch
    scene bg da with dissolve
    pause
    



    # This ends the game.

    return
