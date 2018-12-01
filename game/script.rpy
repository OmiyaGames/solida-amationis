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
define scenario = 'room'
define conversationPhase = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg setup

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
            $ soPronoun = PRONOUNS[0]
        'Female':
            $ soPronoun = PRONOUNS[1]

    # Setup the rest of the variables
    $ soName = getName(soPronoun)
    $ meNoun = getPronoun(mePronoun, 'Possessive')
    $ soNoun = getPronoun(soPronoun, 'Possessive')

    # Actually play the item collecting minigame here
    "Testing: my prounoun is [meNoun], [soName] is [soNoun]"

    # Go to the room minigame
    jump room
