# Enacts a random conversation
label conversation(soStartsConversation = true):
    # Choose a random topic
    python:
        topic = 'random'
        if len(conversationTopics) > 0:
            topic = renpy.random.choice(conversationTopics);
            conversationTopics.remove(topic)

    # Have a conversation about that topic
    if soStartsConversation:
        so "Lets talk about [topic]"
    else:
        me "Lets talk about [topic]"

    # All done
    return
