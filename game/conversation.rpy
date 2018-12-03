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
            topic = renpy.random.choice(conversationTopics)
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
    define p1 = me
    define p2 = so
    if soStartsConversation:
        $ p1 = so
        $ p2 = me
    if topic == 'Profession':
        call convoProfession(p1, p2)
    elif topic == 'Interests':
        call convoInterests(p1, p2)
    elif topic == 'Hobbies':
        if soStartsConversation:
            call convoSoHobbies()
        else:
            call convoMeHobbies()
    else:
        # Default to talking about the flu season
        if soStartsConversation:
            call convoSoFluSeason()
        else:
            call convoMeFluSeason()

    # All done
    return


# This section has all the conversation topics, each starting with "label,"
# followed by the name of the subroutine indicating who starts the topic,
# and what the topic is about.  Check the comments for more details

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

# Subroutine for conversing on profession
label convoProfession(p1, p2):
    python:
        PROFESSION = (
            ("Social Worker",
                ("Social Work",
                "Psychology")
            ), ("Musician",
                ("Music Composition",
                "Music Performance",
                "Music Education",
                "Liberal Arts with Music concentration")
            ), ("Game Designer",
                ("Computer Science",
                "Information Technology",
                "Game Development",
                "Art")
            ), ("Teacher",
                ("Primary Education",
                "Secondary Education",
                "Higher Education")
            ), ("Writer",
                ("Liberal Arts",
                "English",
                "Creative Writing",
                "Journalism")
            ), ("IT Professional",
                ("Computer Science",
                "Cybersecurity",
                "Information Technology")
            ), ("Architect",
                ("Architectural",
                "Art",
                "Applied Mathematics")
            )

        # Setup variables
        professions = list(PROFESSION)

        # define functions
        def randomProfession():
            rand = renpy.random.choice(professions)
            professions.remove(rand)
            return (rand[0], renpy.random.choice(list(rand[1])))

        def chooseProfession():
            # Shuffle list
            renpy.random.shuffle(professions)

            # Get the first 3 choices
            choices = []
            for newChoice in professions[0:3]:
                choices.append((newChoice[0], newChoice))

            # Display the menu
            rand = renpy.display_menu(choices)
            professions.remove(rand)
            return (rand[0], renpy.random.choice(list(rand[1])))

    p1 "So what do you do?"

    if p2 == so:
        $ randProf, randMajor = randomProfession()
    else:
        $ randProf, randMajor = chooseProfession()
    p2 "I'm a [randProf]."
    p1 "That's so cool! What did you study?"
    p2 "I majored in [randMajor]. What about you?"

    if p1 == so:
        $ randProf, randMajor = randomProfession()
    else:
        $ randProf, randMajor = chooseProfession()
    p1 "I'm a [randProf]. I studied [randMajor]."
    p2 "That sounds really interesting! Do you like it?"
    #p1 "Yes, a lot. And you? Do you like your job?"
    if p1 == so:
        $ rand = renpy.random.randint(0, 3)
        if rand == 0:
            p1 "I absolutely love it, and I can't imagine doing anything else."
        elif rand == 1:
            p1 "I like it, but I'd like to switch careers at some point."
        else:
            $ randProf, randMajor = randomProfession()
            p1 "No, I really don't like it at all, so I'm looking at making a career shift to [rand]."
    else:
        menu:
            me "Well..."
            "I love it!":
                p1 "I absolutely love it, and I can't imagine doing anything else."
            "I like it...":
                p1 "I like it, but I'd like to switch careers at some point."
            "I don't really like it.":
                $ randProf, randMajor = randomProfession()
                p1 "No, I really don't like it at all, so I'm looking at making a career shift to [rand]."
    p2 "Ah, very good."

    # All done
    return



# Subroutine for conversing on interests
label convoInterests(p1, p2):
    python:
        INTERESTS = (
            "Reading",
            "Writing",
            "Yoga",
            "Biking",
            "Climbing",
            "History",
            "Gaming",
            "Meditation",
            "Pilates",
            "Mathematics",
            "Fashion",
            "Photography",
            "Physics",
            "Programming",
            "Woodworking",
            "Crocheting",
            "Knitting",
            "Cooking",
            "Baking",
            "Costuming",
            "Anime",
            "Film",
            "Art",
        )

        # Setup variables
        interests = list(INTERESTS)

        # define functions
        def randomInterest():
            rand = renpy.random.choice(interests)
            interests.remove(rand)
            return rand

        def chooseInterest():
            # Shuffle list
            renpy.random.shuffle(interests)

            # Get the first 3 choices
            choices = []
            for newChoice in interests[0:3]:
                choices.append((newChoice, newChoice))

            # Display the menu
            rand = renpy.display_menu(choices)
            interests.remove(rand)
            return rand

    p1 "What do you do when you're not at work?"

    if p2 == so:
        $ randInter = randomInterest()
    else:
        $ randInter = chooseInterest()
    p2 "I really enjoy [randInter].  I read a lot about it and try to attend lectures and films about it when I can."
    p2 "How about you?"

    if p1 == so:
        $ randInter = randomInterest()
    else:
        $ randInter = chooseInterest()
    p1 "I really like [randInter], so I do it a lot."
    p2 "Nice!"

    if p1 == so:
        $ randInter = randomInterest()
    else:
        $ randInter = chooseInterest()
    p1 "Do you like [randInter]?"

    if p2 == so:
        $ randInter = renpy.random.choice(interests)
    else:
        $ randInter = chooseInterest()
    p2 "Yeah, definitely."
    p2 "Not so much, but it's cool that you're into it!"

    # All done
    return
