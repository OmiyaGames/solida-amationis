# The game starts here.
label gameOver:

    # Switch to scene 1
    scene bg gameover
    $ scenario = 'gameover'
    $ conversationPhase = 0

    # These display lines of dialogue.
    me "Huff, puff...well anything good on the menu?"
    so "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
