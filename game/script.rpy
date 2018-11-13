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
image bg blro = ("blro.png")

##character image##
image bs = ("blacksmith.png")
image dad = ("father.png")
image dad2 = ("father2.png")

# Other Variables
define white = Fade(0.5, 1.0, 0.5, color="#fff")
define armor = False
define books = False
define windows = False
##############################################START##################################
label start:
    ## PROLOGUE
    # Opening Scene
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

    # Blacksmith Scene
    "ugh... my head is still dizzy."
    "where am i?"
    b "Ah, you're finally awake."
    "who?"
    scene bg blro with dissolve
    "what is this place?"
    show bs with dissolve
    b "yo."
    ai "Who are you?"
    b "Me? I'm a blacksmith, you can call me Uncle."
    "who is this guy{w}, the way he talks kinda sounds anoying."
    b "what with that face?{w} cheer up! im making dinner."
    hide bs with dissolve
    "what a weird guy.{w} where am i anyway?"
    $ inspect = 0

    #This is the first choice, need revision in inpect value
    menu blackroom:
        "inspect armor":
            $ armor += True
            "it looks handmade."
        "inspect books":
            $ books += True
            "i can see some enchant words in there."
        "inspect windows":
            $ windows += True
            "i saw a castle{w}, never seen this place before."
    if armor == True and books == True and windows == True:
        jump bsr
    else:
        jump blackroom
label bsr:

    "this place is..."
    "{i}A Forgery{/i}{w}, That's the only thing appear in my mind."
    "oh wait did that guy said he was a blacksmith?{w} well my mind is still hazy that time."
    "should i go outside?"
    menu out:
        "yes":
            "well i cant just stay here."
            jump out2
        "no":
            "im not feeling like it."
            jump out2
label out2:
    b "DINNER READY!"
    "oh..."
    #new bg#
    b "looks who finally get out from his cave{w}, bon apetit!"
    ai "ye-yeah."
    "i never seen this meal before."
    "{i}Groooowl~{/i}"
    "fuck, im hungry."
    "well... chooser cant be beggars"
    b "look at you{w} eating my food like there's no tomorrow."
    "wait{w}, theres one thing that i need to clear out first."
    ai "uh... uncle."
    b "yes yes, what do you want from this uncle?"
    ai "what am i doing here?"
    b "im just gonna say it{w}, i found you on the street."
    ai "huh?"
    b "my son is out from the town so im lonely, you know?"
    ai "what?"
    b "so i taking of you since nobody will."
    "this is too much."
    b "dont be sad kid{w}, atleast you got place to stay"
    "i dont want to hear that from a kidnaper mouth."
    "but even thought...."
    ai "i dont remember where i live."
    b "lost your memory?"
    ai "this is frustating."
    b  "calm down kid{w}, guess you only got this old man to protect you from now on"
    "shut up, i dont want to admit it."
    "come on, who am i kidding."
    ai "hey oldman{w}, i'll be in you care."
    b "obviously."
    "i have no choice."
    #blacksmith arc D#


    return
#########################################END###################################3
