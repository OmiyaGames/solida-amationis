# Enacts a random conversation
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
            for newChoice in conversationTopics[0:3]:
                choices.append((newChoice, newChoice))
            me("Hmm, what should we talk about?")
            topic = renpy.display_menu(choices)
            me(topic)
        conversationTopics.remove(topic)

    # TODO: have the conversation
    if soStartsConversation:
        so "Lets talk about [topic]"
    else:
        me "Lets talk about [topic]"

    # All done
    return
