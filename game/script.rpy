# The script of the game goes in this file.

python early:
    config.searchpath.extend(['game//music'])
    ALL_TOPICS = (
        'Profession',
        'Interests',
        'Hobbies',
        'Flu Season'
    )
    ALL_ITEMS = (
        'Smartphone',
        'Bandage',
        'Lucky Penny',
        'Handkerchief',
        'Hat',
        'Band-Aid'
    )
    MALE_NAMES = (
        'Alan',
        'Ben',
        'Callen',
        'Duncan',
        'Evan',
        'Fred',
        'Greg',
        'Henry',
        'Iggy',
        'Jack',
        'Konstantine',
        'Lenard',
        'Mike',
        'Nick',
        'Ozzy',
        'Pat',
        'Ron',
        'Steve',
        'Tom',
        'Victor',
        'Zack'
    )
    FEMALE_NAMES = (
        'Athena',
        'Brittany',
        'Claire',
        'Dianne',
        'Emma',
        'Faith',
        'Gabe',
        'Hannah',
        'Illia',
        'Jenny',
        'Kate',
        'Laura',
        'Miley',
        'Nicole',
        'Olivia',
        'Paula',
        'Rachel',
        'Sam',
        'Temmie',
        'Vivi',
        'Zoe',
    )
    NON_BINARY_NAMES = (
        'Alex',
        'Beck',
        'Pat',
        'Ash',
        'Jude',
        'Robin',
        'Ozzy',
        'Theo',
        'Tea',
        'Quinn',
        'Wren',
        'Brook',
        'Casey',
        'Eli',
        'Jess',
        'Micah',
        'Raphael',
        'Sam',
        'Toby',
        'Gabe'
    )
    PRONOUNS = (
        'Male',
        'Female',
        'Non-Binary'
    )
    CASE = (
        'Possessive',
        'Personal',
        'Reflexive'
    )
    def getPronoun(gender, case):
        if gender == PRONOUNS[0]:
            if case == CASE[0]:
                return 'his'
            elif case == CASE[1]:
                return 'he'
            elif case == CASE[2]:
                return 'himself'
        elif gender == PRONOUNS[1]:
            if case == CASE[0]:
                return 'her'
            elif case == CASE[1]:
                return 'she'
            elif case == CASE[2]:
                return 'herself'
        else:
            if case == CASE[0]:
                return 'their'
            elif case == CASE[1]:
                return 'they'
            elif case == CASE[2]:
                return 'themselves'
    def getName(gender):
        if gender == PRONOUNS[0]:
            return renpy.random.choice(list(MALE_NAMES))
        elif gender == PRONOUNS[1]:
            return renpy.random.choice(list(FEMALE_NAMES))
        else:
            return renpy.random.choice(list(NON_BINARY_NAMES))

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character('[meName]', color='#ff9933')
define meName = ''
define meGender = PRONOUNS[2]

define so = Character('[soName]', color='#66ccff')
define soName = 'Significant Other'
define soGender = PRONOUNS[2]

# TODO: Add some more conversation topics when I have the time
define DEFAULT_PROBABILITY_OF_SUCCESS = 0.9
define conversationTopics = list(ALL_TOPICS)
define probabilityOfSuccess = DEFAULT_PROBABILITY_OF_SUCCESS
define inventory = []
define conversationPhase = 0
define scenario = 'room'

# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either 'bg room.png' or 'bg room.jpg') to the
    # images directory to show it.
    scene bg setup
    stop music

    python:
        # Reset all the variables
        conversationTopics = list(ALL_TOPICS)
        probabilityOfSuccess = DEFAULT_PROBABILITY_OF_SUCCESS

        # Just setting up the player
        meName = renpy.input('Please enter your first name:', meName, length=20)
        meName = meName.strip()

        if not meName:
            meName = 'Player'
    menu:
        'Please select the gender you\'d like to play as:'

        'Non-Binary':
            $ meGender = PRONOUNS[2]
        'Male':
            $ meGender = PRONOUNS[0]
        'Female':
            $ meGender = PRONOUNS[1]
    menu:
        'Please select the gender you\'d like to date:'

        'Non-Binary':
            $ soGender = PRONOUNS[2]
        'Male':
            $ soGender = PRONOUNS[0]
        'Female':
            $ soGender = PRONOUNS[1]

    # Setup the rest of the variables
    $ soName = getName(soGender)
    $ meNoun = getPronoun(meGender, 'Possessive')
    $ soNoun = getPronoun(soGender, 'Possessive')

    # Go to the room minigame
    jump room
