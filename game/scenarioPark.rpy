# The game starts here.
label park:

    # Switch to scene 1
    scene bg park
    $ scenario = 'park'
    $ conversationPhase = 0

    # TODO: These display lines of dialogue.
    me "Placeholder text"
    so "Once you add a story, pictures, and music, you can release it to the world!"

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)
    call conversation(not rand)

    # TODO: indicate what happens after the conversation
    "Placeholder text: then [soName] loses eyeball, tongue, fingers. But I had a smartphone!"
    $ probabilityOfSuccess -= 0.1

    # Move to the streets.
    if renpy.random.random() < probabilityOfSuccess:
        "Placeholder text: also, we went to the hospital!"
        jump hospital
    else:
        jump gameover

    # This ends the game.
    return
