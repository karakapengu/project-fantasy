#####KARAKTER##########
define qq = Character("?????", what_prefix='"', what_suffix= '"')
define f = Character("Father", what_prefix='"', what_suffix= '"')
define ai = Character("Aiden", what_prefix='"', what_suffix= '"')
define ju = Character("Julie", what_prefix='"', what_suffix= '"')
define ph = Character("Phyrie", what_prefix='"', what_suffix= '"')
define ar = Character("Arthur", what_prefix='"', what_suffix= '"')
define ru = Character("Ruby", what_prefix='"', what_suffix= '"')
define k = Character("King", what_prefix='"', what_suffix= '"')
define q = Character("Queen", what_prefix='"', what_suffix= '"')
define b = Character("Blacksmith", what_prefix='"', what_suffix= '"')
define al = Character("Alia", what_prefix='"', what_suffix= '"')

#Scene bg
image bg in1 = ("intro.png")
image bg in2 = ("intro2.png")
image bg da = ("dark.png")
image bg blro = ("blro.png")
image bg blk = ("blk.png")
image bg trfr = ("forest.jpg")
image bg stre = ("street.jpg")
##character image##
image bs = ("blacksmith.png")
image dad = ("father.png")
image dad2 = ("father2.png")
image m = ("myster.png")

# Other Variables
define white = Fade(0.5, 1.0, 0.5, color="#fff")
define armor = False
define books = False
define windows = False
##############################################START##################################
label start:
    ## PROLOGUE
    # Flashback 1
    scene bg da with dissolve
    centered "Unnamed Village, 469 AD"
    centered "That day...{w} I'm awake because of the ruckus outside."
    centered "so I go and check it out...{w} I can't believe what I'm seeing that day."
    show villageburn:
        yalign 1.0
        xalign 1.0
        ease 6.0 xalign 0.0
    with white
    pause
    show villageburn:
        zoom 0.75
    with dissolve
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
    "{i}crumbling{/i}" with hpunch
    "that sound...{w} from behind"
    "some stone material from the local house fall right onto me."
    "Ugh, i feel dizzy{w}, i cant keep-" with vpunch
    "....."
    show m with dissolve
    "who?"
    scene bg da with dissolve and vpunch
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

    menu blackroom:
        "Inspect armor":
            $ armor += True
            "it looks handmade."
        "Peek the books":
            $ books += True
            "i can see some enchant words in there."
        "See through the windows":
            $ windows += True
            "i saw a castle{w}, never seen this place before."
    if armor >= True and books >= True and windows >= True:
        jump bsr
    else:
        jump blackroom
label bsr:

    "this place is..."
    "{i}A forgery{/i}{w}, that's the only thing appear in my mind."
    "oh wait did that guy said he was a blacksmith?{w} Well my mind is still hazy that time."
    "should i go outside?"
    menu out:
        "Yes":
            "well i cant just stay here."
            jump out2
        "No":
            "Well, I'm still dizzy after all"
            jump out2
label out2:
    b "DINNER READY!"
    "oh..."
    scene bg blk :
        zoom 1.5
        xalign 0.6
        ease 4.0 xalign 0.0
    with dissolve
    pause
    show bg blk :
        zoom 1.0
    with dissolve
    show bs with easeinright

    b "looks who finally get out from his cave{w}, bon appétit!"
    ai "ye-yeah."
    hide bs with easeoutright
    "i never seen this meal before."
    "{i}Groooowl~{/i}"
    "damn, im hungry."
    "well... beggar cant be chooser."
    b "look at you{w} eating my food like there's no tomorrow."
    b "eat up and get strong okay."
    "shut up oldman."
    "....."
    "wait{w}, theres one thing that i need to clear out first."
    ai "uh... uncle."
    show bs with easeinright
    b "yes yes, what do you want from this uncle?"
    ai "what am i doing here?"
    b "im just gonna say it{w}, i found you on the street."
    ai "huh?"
    b "my son is out from the town so im lonely, you know?"
    ai "what?"
    b "so im taking care of you since nobody will."
    "this is too much."
    b "dont be sad kid{w}, atleast you got place to stay."
    "i dont want to hear that from a kidnapper mouth."
    "but even thought...."
    ai "i dont remember where i live."
    b "lost your memory?"
    ai "Maybe, this is frustating."
    b  "calm down kid{w}, guess you only got this old man to protect you from now on."
    "shut up, i dont want to admit it."
    "come on, who am i kidding."
    ai "hey oldman{w}, i'll be in you care."
    b "obviously."
    scene bg da with dissolve
<<<<<<< HEAD
    centered "i have no choice."

=======
    pause
>>>>>>> 25bbe3f3989aa746394c4747551a44c6f57bb3cc
    ###training arc###
    # Nanti tambahin semacam splash screen disini
    scene bg da with fade
    centered "Blacksmith's House, 479 AD"
    show bg blk with dissolve
    ai "im going out."
    show bs with dissolve
    b "be careful kid."
    "you dont need to answer that."
    ##new bg##
    scene bg stre with dissolve
    "Several years ago, I'm just a stranger in this town..."
    "well this is my life now{w}, guess im just gonna bear with it."
    "....."
    show bg trfr with dissolve
    "time for another training."

    #edited bg
    #Another Flashback
    show bg da with dissolve
    b "you should find a job."
    ai "huh?{w} why?"
    b "you cant just live here forever{w}, i want you to be success in the future, you know?"
    ai "pain in the ass."
    b "how about being a soldier?"
    ai "why soldier?"
    b "my son wants to be a soldier{w}, you two should make a party and do some duty."
    "....."
    ai "well{w}, its not like i have anything to do"
    b "i'll put you in an academy i know."
    ai "i dont wanna."
    b "no dinner tonight."
    ai "..."
    ai "fine."
    #back previous bg
    centered "and then i graduated."
    centered "I still waiting for aplication aproval{w}, while that still taking care of guess i'll train my body."
    scene bg trfr with dissolve





    return
#########################################END###################################3
