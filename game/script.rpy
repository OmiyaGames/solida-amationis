# The script of the game goes in this file.

python early:
    MALE_NAMES = (
        "Taro",
        "Alex",
        "Konstantine",
        "Ben"
    )
    FEMALE_NAMES = (
        "Hana",
        "Alex",
        "Andrea",
        "Amanda"
    )
    PRONOUNS = (
        "Male",
        "Female",
        "NonBinary"
    )
    mePronoun = renpy.random.choice(list(PRONOUNS))
    soPronoun = renpy.random.choice(list(PRONOUNS))
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
    # Randomly choose a name for the SO
    soName = 'SO'
    if soPronoun == PRONOUNS[0]:
        soName = renpy.random.choice(list(MALE_NAMES))
    elif soPronoun == PRONOUNS[1]:
        soName = renpy.random.choice(list(FEMALE_NAMES))
    elif renpy.random.random() < 0.5:
        soName = renpy.random.choice(list(MALE_NAMES))
    else:
        soName = renpy.random.choice(list(FEMALE_NAMES))

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define so = Character("[soName]")
define me = Character('Me')
define probabilityOfSuccess = 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    $ meThey = getPronoun(mePronoun, 'Possessive')
    $ soThey = getPronoun(soPronoun, 'Possessive')
    "Testing: my prounoun is [meThey], [soName] is [soThey]"
    me "Oh, egads, I'm late for my date!"
    "I was getting excited by a new **nder date I hooked up today, but I overslept"
    me "Quick!  What should I bring?"
    "Placeholder Text: I brought bandaids, hat, and an...eyepatch?"

    scene bg cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show so happy

    # These display lines of dialogue.

    so "You've created a new Ren'Py game."

    so "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
