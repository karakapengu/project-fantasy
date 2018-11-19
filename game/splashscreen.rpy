#Splashscreen
image splash = ("splashscreen game.png")

label splashscreen:
    show bg da
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
