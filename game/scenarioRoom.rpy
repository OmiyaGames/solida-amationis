# Starting the room scenario
label room:
    # Setup the minigame variables
    python:
        # Clear the inventory
        del inventory[:]

        # Setup variables
        leftOverItems = list(ALL_ITEMS)

        def displayItems(choices):
            item = renpy.display_menu(choices)
            inventory.append(item)
            leftOverItems.remove(item)

        def randomItem():
            # Shuffle the items
            renpy.random.shuffle(leftOverItems)

            # Display menu
            choices = []
            for newChoice in leftOverItems[0:3]:
                choices.append((newChoice, newChoice))
            displayItems(choices)

        def chooseNextItem():
            # Display menu
            choices = []
            for newChoice in leftOverItems[2:5]:
                choices.append((newChoice, newChoice))
            displayItems(choices)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg room
    play music "Horror 1.mp3"

    # Actually play the item collecting minigame here
    me "Oh, egads, I'm late for my date!"

    "I was getting excited by the date I hooked up online today, that I couldn't sleep last night."
    "Now I only have enough time to pack 3 things."
    "This is already starting to become a nightmare!"

    me "Quick! What should I bring?"
    $ randomItem()

    me "And what else?"
    $ chooseNextItem()

    me "And finally?"
    $ randomItem()

    # Check if the player has the lucky penny
    if 'Lucky Penny' in inventory:
        # Increase probability of survival immediately
        $ probabilityOfSuccess += 0.05

    me "Right, I hope I make it to the cafe soon! Can't leave the date hanging."

    # Go to the cafe
    jump cafe
