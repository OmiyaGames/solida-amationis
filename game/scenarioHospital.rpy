# The game starts here.
label hospital:

    # Switch to scene 1
    scene bg hospital
    $ scenario = 'hospital'
    $ conversationPhase = 0

    # These display lines of dialogue.
    define doc = Character('Doctor', color='#ffffff')
    doc "Solida amationis."
    me "Come again?"
    "My focus suddenly returned back to the stale room, with the white curtain covering the sides."
    so "It's what I'm suffering from, [meName]."
    me "Oh, right."
    "My memory has been a blur since the ambulance arrived. Only now can I clearly see the [soName] lying in the stetcher."
    doc "Yes, it's a very scary infection. Initially, it looks like any common cold, but over time, the symptomes worsens to rapid reduction in body mass."
    doc "Fortunately, it's not too difficult to treat."
    "My body loosens a bit."
    me "That's a relief."
    so "Yeah."
    doc "It takes a few days to recover from this infection. I hope that's fine with you?"
    so "Yes."
    doc "Good. I'll arrange everything, then."

    $ rand = renpy.random.choice(list(PRONOUNS))
    $ rand = getPronoun(rand, 'Possessive')
    "The doctor turns [rand] back towards us. As he enters the records into the terminal, [soName] rolls towards me."
    so "I'm sorry for ruining our date."
    "I can hear the doctor snorting in the background."

    menu:
        "I respond,"

        "Don't be silly.":
            me "Don't be silly, your life matters to me than this date."
        "You're alive.":
            me "You're alive.  That's what matters."
        "I'm fine.":
            me "Seriously, I'm fine.  Don't worry about it."

    "[soName] smiles."
    so "You're right. Thank you."
    "[soName] rolls back to a comfortable position."
    so "Looks like everything is taken care of here."
    me "Yeah, sounds like you'll be fine."
    "The doctor turns back towards us."
    doc "All done.  I've got some brochures for both of you in case you want to know about Solida amationis and its treatment."
    "The doctor handed each of us a copy."
    doc "Don't forget to read it!"
    "I get up, brochure in hand."
    me "Well, I better get going.  Hey, [soName], call me if you need any help."
    so "Will do."
    "I flash [soName] a smile before I leave."

    # Switch to scene 1
    scene bg streets

    # This ends the game.
    return
