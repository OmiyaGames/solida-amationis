# The game starts here.
label gameover:

    # Switch to scene 1
    scene bg gameover
    $ scenario = 'gameover'
    $ conversationPhase = 0

    # TODO: These display lines of dialogue.
    so "Placeholder text"
    me "No!"
    me "No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no-"

    # This ends the game.
    return
