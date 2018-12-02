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
    so "*Cough*"
    me "Sorry I'm late!"

    $ rand = renpy.random.randint(0, 1)
    if rand == 1:
        so "You kept me waiting."
        "Uh, oh, not good."
    else:
        so "Oh, no, you're fine."
        "Well, things might not be so bad after all."

    me "Huff, puff...well, are there anything good on the menu?"

    $ rand = renpy.random.choice(('The Californian', 'The Hot Mess', 'The Holmes', 'The Hudson'))
    so "There are some interesting sandwiches here.  I think I'm going to get [rand]."

    menu:
        me "Then I'll get..."

        "The Rensselaer":
            me "Gotta have those veggies."
            so "And roast beef, I presume?"
            me "You know me too well."
        "The Sage":
            me "The turkey and cranberry combination sounds intriguing."
        "The Uncle Sams":
            me "Can't go wrong with ham, cheese, and rye."
            so "You'd think this sandwich would have a more...patriotic mix."
        "The Watson":
            me "What can I say? I want a good old fashioned burger."
            so "With boiled onions and mushrooms."
            me "Yes, that too."
        "The Harvest Moon":
            me "Bageled sandwich with turkey and apple. Something different."

    $ rand = renpy.random.randint(0, 1)
    if rand == 1:
        "As the waiter came along, we placed the order."
    else:
        "As the waitress came along, we placed the order."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)

    # TODO: indicate what happens after the conversation
    "Placeholder text: then [soName] loses a fingernail. But that's OK, cause I have bandaids!"
    "Placeholder text: also, food was good, yadda, yadda, yadda. Off to the park!"

    # Move to the streets.
    jump streets
