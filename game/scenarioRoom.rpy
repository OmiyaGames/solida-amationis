# Starting the room scenario
label room:
    # Setup the minigame variables
    python:
        # Clear the inventory
        del inventory[:]

        # Setup variables
        leftOverItems = list(ALL_ITEMS)

        def chooseItem():
            # Shuffle the items
            renpy.random.shuffle(leftOverItems)

            # Display menu
            choices = []
            for newChoice in leftOverItems[0:3]:
                choices.append((newChoice, newChoice))
            item = renpy.display_menu(choices)
            inventory.append(item)
            leftOverItems.remove(item)
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg room

    # Actually play the item collecting minigame here
    me "Oh, egads, I'm late for my date!"

    "I was getting excited by the date I hooked up online today, that I couldn't sleep last night."
    "Now I only have enough time to pack 3 things."
    "This is already starting to become a nightmare!"

    me "Quick! What should I bring?"
    $ chooseItem()

    me "And what else?"
    $ chooseItem()

    me "And finally?"
    $ chooseItem()

    me "Right, now to the cafe!"

    # Go to the cafe
    jump cafe
