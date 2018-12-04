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
    $ p1 = me
    $ p2 = so
    if soStartsConversation:
        # Swap figures
        $ p1 = so
        $ p2 = me
    if topic == 'Profession':
        call convoProfession(p1, p2)
    elif topic == 'Interests':
        call convoInterests(p1, p2)
    elif topic == 'Hobbies':
        call convoHobbies(p1, p2)
    else:
        # Default to talking about the flu season
        call convoFluSeason(p1, p2)

    # All done
    return


# This section has all the conversation topics, each starting with "label,"
# followed by the name of the subroutine indicating who starts the topic,
# and what the topic is about.  Check the comments for more details

# Subroutine for conversing on the flu season, starting with the Player
label convoFluSeason(p1, p2):
    python:
        dialog = {
            "Yes": ("Yeah, have you heard about the severe coughs that's been killing people lately?", "I get scared thinking about it."),
            "No":  ("Not at all.", "The cold has never bothered me, anyway.")
        }
    p1 "I hope the flu hasn't gotten to you."
    p2 "'Tis the season, isn't it?  There are a lot of people with the coughs lately."
    p1 "I hope it doesn't bother you too much."

    define rand = "Welp"
    if p2 == so:
        python:
            rand = renpy.random.choices(dialog.keys())
            for response in dialog[rand]:
                p2(response)
    else:
        menu:
            "Yes":
                python:
                    for response in dialog["Yes"]:
                        p2(response)
            "No":
                python:
                    for response in dialog["No"]:
                        p2(response)

    python:
        dialog = {
            "Yeah, where's the snow?": ("I know, right?  Like, I feel colder without it than with!"),
            "Yeah, it's frigid out there.": ("I'm concerned I haven't suited up properly for it."),
            "I think it's fine.": ("Aw, you're lucky.  I wished I had your genes.")
        }
    p1 "Still, the weather has been crazy, hasn't it?"
    if p2 == so:
        python:
            rand = renpy.random.choices(dialog.keys())
    else:
        menu:
            "Yeah, where's the snow?":
                $ rand = "Yeah, where's the snow?"
            "It's frigid out there.":
                $ rand = "Yeah, it's frigid out there."
            "It's fine.":
                $ rand = "I think it's fine."
    python:
        for response in dialog[rand]:
            p1(response)

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
            p1 "No, I really don't like it at all, so I'm looking at making a career shift to [randProf]."
    else:
        menu:
            me "Well..."
            "I love it!":
                p1 "I absolutely love it, and I can't imagine doing anything else."
            "I like it...":
                p1 "I like it, but I'd like to switch careers at some point."
            "I don't really like it.":
                $ randProf, randMajor = randomProfession()
                p1 "No, I really don't like it at all, so I'm looking at making a career shift to [randProf]."
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
        $ randInter = renpy.random.choice(("Yeah, definitely.", "Not so much, but it's cool that you're into it!"))
    else:
        menu:
            "Definitely.":
                $ randInter = "Yeah, definitely."
            "Not so much.":
                $ randInter = "Not so much, but it's cool that you're into it!"
    $ p2(randInter)

    # All done
    return



# Subroutine for conversing on interests
label convoHobbies(p1, p2):
    python:
        movies = {
            "Antiviral": ("Oh!  I was talking about David.  You're thinking of his son, Brandon.", "Very good movie!  The ending creeped me out though."),
            "Doki Doki": ("*Laughs*  That's not a movie!", "It's okay if you don't know about him. I can show you later."),
            "Stalker": ("The book, movie, or game?", "Either way, I'm totally over talking about this one.  Too depressing for my tastes."),
            "Videodrome": ("Good choice!  My favorite is eXistenZ.", "Videodrome made me squirm though.  I'm glad I finally have someone to talk about this stuff with!")
        }
    p1 "So what kind of stuff are you into?"
    p2 "*blushes* What do you mean?"
    p1 "Like movies and games."
    p2 "Oh!  Yeah, I'm into that stuff.  I'm a bit of a nerd."
    p1 "Really!  Me too!"
    p2 "*laughs*  Yeah?  I'm kinda into Cronenberg.  I hope that's not weird..."
    p2 "You know who that is, right?"
    p1 "Yeah... totally."
    p2 "Awesome! What's your favorite movie of his?"

    define rand = "Welp"
    if p1 == so:
        python:
            rand = renpy.random.choices(movies.keys())
            p1(rand)
    else:
        menu:
            "Antiviral":
                $ rand = "Antiviral"
            "Doki Doki":
                $ rand = "Doki Doki"
            "Stalker":
                $ rand = "Stalker"
            "Videodrome":
                $ rand = "Videodrome"
    python:
        if rand == "Doki Doki":
            probabilityOfSuccess -= 0.2
        elif rand == "Stalker":
            probabilityOfSuccess -= 0.1
        for response in movies[rand]:
            p2(response)
    # All done
    return
