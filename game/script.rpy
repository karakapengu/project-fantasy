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

#else#
define white = Fade(0.5, 1.0, 0.5, color="#fff")

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
            $ inspect += 1
            "it looks handmade."
        "inspect books":
            $ inspect += 1
            "i can see some enchant words in there."
        "inspect windows":
            $ inspect += 1
            "i saw a castle{w}, never seen this place before."
    if inspect == 1:
        jump blackroom
    if inspect == 2:
        jump blackroom
    if inspect == 3:
        jump bsr
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
label out2


    return
#########################################END###################################3
