# The game starts here.
label gameover:

    # Switch to scene 1
    scene bg gameover
    $ scenario = 'gameover'
    $ conversationPhase = 0

    # TODO: These display lines of dialogue.
    so "Placeholder text"
    "And just like that, I watched in horror as the date fall apart into pieces."
    me "No!"
    me "No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no-"

    # This ends the game.
    "Love is over..."
    jump start
