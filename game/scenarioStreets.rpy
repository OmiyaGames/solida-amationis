# The game starts here.
label streets:

    # Switch to scene 1
    scene bg streets
    $ scenario = 'streets'
    $ conversationPhase = 0

    # TODO: These display lines of dialogue.
    me "Placeholder text"
    so "Once you add a story, pictures, and music, you can release it to the world!"

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)

    # TODO: indicate what happens after the conversation
    "Placeholder text: then [soName] loses eyebrows, ear lobe, or tooth. But that's OK, cause we hid it with a hat!"
    $ probabilityOfSuccess -= 0.1

    # Move to the streets.
    if renpy.random.random() < probabilityOfSuccess:
        "Placeholder text: also, we made it to the park!"
        jump park
    else:
        jump gameover

    # This ends the game.
    return
