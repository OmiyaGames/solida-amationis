# The game starts here.
label hospital:

    # Switch to scene 1
    scene bg hospital
    $ scenario = 'hospital'
    $ conversationPhase = 0

    # These display lines of dialogue.
    me "Huff, puff...well anything good on the menu?"
    so "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
