# The game starts here.

label room:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg room

    # Setup the rest of the variables
    $ meNoun = getPronoun(mePronoun, 'Possessive')
    $ soNoun = getPronoun(soPronoun, 'Possessive')

    # Actually play the item collecting minigame here
    me "Oh, egads, I'm late for my date!"
    "I was getting excited by the date I hooked up online today, that I couldn't sleep last night."
    "This is already starting to become a nightmare."
    me "Quick!  What should I bring?"
    "Placeholder Text: I brought bandaids, hat, and an...eyepatch?"

    # Go to the cafe
    jump cafe
