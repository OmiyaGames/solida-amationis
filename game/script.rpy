# The script of the game goes in this file.

python early:
    MALE_NAMES = (
        'Taro',
        'Alex',
        'Konstantine',
        'Ben'
    )
    FEMALE_NAMES = (
        'Hana',
        'Alex',
        'Andrea',
        'Amanda'
    )
    PRONOUNS = (
        'Male',
        'Female',
        'NonBinary'
    )
    def getPronoun(gender, case):
        if gender == PRONOUNS[0]:
            if case == 'Possessive':
                return 'his'
            elif case == 'Personal':
                return 'he'
            elif case == 'Reflexive':
                return 'himself'
        elif gender == PRONOUNS[1]:
            if case == 'Possessive':
                return 'her'
            elif case == 'Personal':
                return 'she'
            elif case == 'Reflexive':
                return 'herself'
        else:
            if case == 'Possessive':
                return 'their'
            elif case == 'Personal':
                return 'they'
            elif case == 'Reflexive':
                return 'theirselves'
    def getName(gender):
        if gender == PRONOUNS[0]:
            return renpy.random.choice(list(MALE_NAMES))
        elif gender == PRONOUNS[1]:
            return renpy.random.choice(list(FEMALE_NAMES))
        elif renpy.random.random() < 0.5:
            return renpy.random.choice(list(MALE_NAMES))
        else:
            return renpy.random.choice(list(FEMALE_NAMES))

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character('[meName]')
define meName = 'Player'
define mePronoun = PRONOUNS[2]

define so = Character('[soName]')
define soName = 'Significant Other'
define soPronoun = PRONOUNS[2]

define probabilityOfSuccess = 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg room

    # Just setting up the player
    python:
        meName = renpy.input('Please enter your name:', '', length=20)
        meName = meName.strip()

        if not meName:
            meName = 'Player'
    menu:
        'Please select the gender you\'d like to play as:'

        'Non-Binary':
            $ mePronoun = PRONOUNS[2]
        'Male':
            $ mePronoun = PRONOUNS[0]
        'Female':
            $ mePronoun = PRONOUNS[1]
    menu:
        'Please select the gender you\'d like to date:'

        'Non-Binary':
            $ soPronoun = PRONOUNS[2]
        'Male':
            $ mePronoun = PRONOUNS[0]
        'Female':
            $ soPronoun = PRONOUNS[1]

    # Setup the rest of the variables
    $ meNoun = getPronoun(mePronoun, 'Possessive')
    $ soNoun = getPronoun(soPronoun, 'Possessive')
    $ soName = getName(soPronoun)

    # Actually play the item collecting minigame here
    "Testing: my prounoun is [meNoun], [soName] is [soNoun]"
    me "Oh, egads, I'm late for my date!"
    "I was getting excited by the date I hooked up online today, that I couldn't sleep last night."
    "This is already starting to become a nightmare."
    me "Quick!  What should I bring?"
    "Placeholder Text: I brought bandaids, hat, and an...eyepatch?"

    # Switch to scene 1
    scene bg cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named 'so happy.png' to the images
    # directory.
    #show so happy

    # These display lines of dialogue.
    me "Sorry I'm late!"
    so "You kept me waiting."
    me "Huff, puff...well anything good on the menu?"
    so "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
