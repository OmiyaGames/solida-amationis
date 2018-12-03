# FYI, any line that starts with a "#" is a comment
# The code completely ignores any lines that comes after it.

# Also, I use single quotes and double quotes rather interchangeably,
# but would recommend using double quotes to annotate the start and end
# of a string, e.g. "This is a string"

# Enacts a random conversation
# This is pretty code-heavy. Unless a new topic is meant to be added,
# I would recommend skipping down to the first "return" line
label conversation(soStartsConversation = true):

    python:
        # Setup variables
        topic = 'random'

        # Check who starts first
        if soStartsConversation:
            # Choose a random topic
            topic = renpy.random.choice(conversationTopics);
        else:
            # Shuffle the topics
            renpy.random.shuffle(conversationTopics)
            choices = []
            for newChoice in conversationTopics[0:2]:
                choices.append((newChoice, newChoice))
            me("Hmm, what should we talk about?")
            topic = renpy.display_menu(choices)
        conversationTopics.remove(topic)

    # Check which topic to speak about, and who starts the conversation
    # Then call the subroutine (listed below) to talk about that topic
    if topic == 'Holidays':
        if soStartsConversation:
            call convoSoHolidays()
        else:
            call convoMeHolidays()
    elif topic == 'Hobbies':
        if soStartsConversation:
            call convoSoHobbies()
        else:
            call convoMeHobbies()
    elif topic == 'Flu Season':
        if soStartsConversation:
            call convoSoFluSeason()
        else:
            call convoMeFluSeason()
    else:
        # Default to talking about the weather
        if soStartsConversation:
            call convoSoWeather()
        else:
            call convoMeWeather()

    # All done
    return


# This section has all the conversation topics, each starting with "label,"
# followed by the name of the subroutine indicating who starts the topic,
# and what the topic is about.  Check the comments for more details

# Subroutine for conversing on the flu season, starting with the SO
label convoSoFluSeason():
    so "Ugh, I hate the flu season. I even got the snuffles."
    me "I know, it sucks."
    "And the narrator described talked about some mysterious disease people were dying right-and-left from."
    "OoOo, forshadowing!"

    # All done
    return

# Subroutine for conversing on the flu season, starting with the Player
label convoMeFluSeason():
    me "I've been seeing a lot coughs from people around me, lately."
    so "Well, of course, it's the dreaded flu season."
    "And the narrator described talked about some mysterious disease people were dying right-and-left from."
    "OoOo, forshadowing!"

    # All done
    return



# Subroutine for conversing on the weather, starting with the SO
label convoSoWeather():
    # This line below has the SO speaking
    so "Lets talk about the weather."
    # This line below has the Player speaking
    me "OK."
    # This line below has the Narrator...narrating
    "And the narrator described about the cold, harsh winter."

    # For creating branching narrative, start with "menu:" like the example below
    # Any lines below a colon must be indented.
    menu:
        # This question below will be printed on the bottom of the screen
        so "So determine how the weather affects me."

        # Depict by simple having a string, followed by a colon
        "Absolutely nothing":
            # If no conversations should occur when making a choice, use "pass" like the line below
            pass
        "Decrease the probability of SO's survival":
            # And this would be a prime opportunity to have a conversation
            so "Wait, seriously!? What's wrong with you!?"
            me "Well, Taro needed something to demonstrate dropping numbers, so this choice was added in."
            me "And, well, I was curious."
            so "You're both jerks!!"

            # For any bad choices, you can add a penalty like the line below:
            $ probabilityOfSuccess -= 0.1
            # Above line decreases the probability that the SO survives by 10 percent.
            # I would recommend keeping the probability of success above 30 percent or so.

    # If a custom text needs to be inserted in a string, use [], with a variable name in-between
    # To insert single-line python code, use $
    # (Note: the code at the top of this file also uses "python:" to demonstrate running multi-line python code)
    # The lines below creates a new variable named, "aCustomString" with a custom string value.
    # Then this line gets inserted into the narrator's narration with the [].
    $ aCustomString = "This is a custom string."
    "Taro also needed to demonstrated how custom string works. It's like this: [aCustomString]"

    # Using custom strings is more important for inserting names, gender and pronouns.
    "The player's name is [meName]. Significant other's is [soName]."
    "The player's gender is [meGender]. Significant other's is [soGender]."

    # For pronouns, I created a function demonstrated below.
    # To get they/he/she...
    $ meNoun = getPronoun(meGender, 'Personal')
    $ soNoun = getPronoun(soGender, 'Personal')
    "The player's personal pronoun is [meNoun]. Significant other's is [soNoun]."

    # To get their/his/her...
    $ meNoun = getPronoun(meGender, 'Possessive')
    $ soNoun = getPronoun(soGender, 'Possessive')
    "The player's posessive pronoun is [meNoun]. Significant other's is [soNoun]."

    # To get themselves/himself/herself...
    $ meNoun = getPronoun(meGender, 'Reflexive')
    $ soNoun = getPronoun(soGender, 'Reflexive')
    "The player's reflexive pronoun is [meNoun]. Significant other's is [soNoun]."

    # All done
    return

# Subroutine for conversing on the weather, starting with the player
label convoMeWeather():
    me "Lets talk about the weather."
    so "OK."
    "And the narrator described about the cold, harsh winter."

    # All done
    return



# Subroutine for conversing on hobbies, starting with the SO
label convoSoHobbies():
    so "What hobbies do you have?"
    me "Uh..."
    "And the narrator described about video games."

    # All done
    return

# Subroutine for conversing on hobbies, starting with the Player
label convoMeHobbies():
    me "What hobbies do you have?"
    so "Uh..."
    "And the narrator described about video games."

    # All done
    return



# Subroutine for conversing on the holidays, starting with the SO
label convoSoHolidays():
    so "What are you going to do for the holidays?"
    me "Uh..."
    "And the narrator described about buying video games."
    "And the power of copy and paste."

    # All done
    return

label convoMeHolidays():
    me "What are you going to do for the holidays?"
    so "Uh..."
    "And the narrator described about buying video games."
    "And the power of copy and paste."

    # All done
    return
