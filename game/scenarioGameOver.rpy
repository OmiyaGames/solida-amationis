# The game starts here.
label gameover:

    # Switch to scene 1
    $ scenario = 'gameover'
    $ conversationPhase = 0

    stop music fadeout 1.0

    # These display lines of dialogue.
    $ soNoun = getPronoun(soGender, 'Possessive')
    "Suddenly, [soName]'s body lurches forward, [soNoun] face turning towards the ground."
    so "Hurg-"
    "I jolt."
    me "[soName]!"
    "[soName] struggles to speak."
    so "[meName]...{w=0.5}I...{w=0.5}feel...{w=0.5}"
    "[soName]'s body starts to fall."
    me "[soName]!!"
    $ soNoun = getPronoun(soGender, 'Personal')
    "I grab [soNoun]. [soNoun] limps."
    me "[soName]!!!"
    "I gasped in horror. Dangling out of [soNoun] mouth was a set of thick blood veins."
    "Attached to the end was an exposed heart, beating weakly."
    me "No!"
    "I can't let it end like this."
    me "No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no-"

    # This ends the game.
    "...{p}...{p}...{p}{w=1}Love is over..."
    jump start
