# The game starts here.

label cafe:

    # Switch to scene 1
    scene bg cafe
    $ scenario = 'cafe'
    $ conversationPhase = 0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named 'so happy.png' to the images
    # directory.
    #show so happy

    # These display lines of dialogue.
    me "Sorry I'm late!"

    $ rand = renpy.random.randint(0, 1)
    if rand == 1:
        so "You kept me waiting."
        "Uh, oh, not good."
    else:
        so "Oh, no, you're fine."
        "Well, things might not be so bad after all."

    me "Huff, puff...well, are there anything good on the menu?"

    so "There are some interesting sandwiches here.  I think I'm going to get The Californian."

    menu:
        me "Then I'll get..."

        "The Rensselaer":
            pass
        "The Sage":
            pass
        "The Uncle Sams":
            pass
        "The Triple Decker":
            pass

    "We placed the order."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)
    call conversation(not rand)

    # TODO: indicate what happens after the conversation
    "Placeholder text: then [soName] loses a fingernail. But that's OK, cause I have bandaids!"
    "Placeholder text: also, food was good, yadda, yadda, yadda. Off to the park!"

    # Move to the streets.
    jump streets
