# The game starts here.
label streets:

    # Switch to scene 1
    scene bg streets
    $ scenario = 'streets'
    $ conversationPhase = 0

    # TODO: These display lines of dialogue.
    "We walked out of the cafe. Perhaps due to our full stomach, the outside didn't feel as chilly as before."
    me "Lead me the way."
    so "Gladly. It's just straight this way."
    "The streets was a bit empty, probably due to it being the weekends."
    "We passed some wooden Uncle Sams statues."
    "While walking, we both conversed to pass some time."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)

    # Start the body-loss section
    so "*Cough, cough*"
    "It appeared [soName]'s coughs were getting worse."
    me "Are you alright?"
    so "Yeah, I think so-"
    "[soName] suddenly jutted forward, as if to throw up."
    me "[soName]!!"
    $ soNoun = getPronoun(soGender, 'Possessive')
    "As I rushed to [soNoun] side, I saw [soName] holding holding something."

    # Jump to a random body loss situation
    $ rand = (renpy.random.randint(0, 3) == 1)
    if rand == 0:
        jump streetsLostEyebrow
    elif rand == 1:
        jump streetsLostEarLobe
    else:
        jump streetsLostTooth

    # For safety reasons, adding a return to end the game.
    # Should never arrive here, anyway.
    return

label streetsLostEyebrow:
    "It was a set of short hair."
    me "I...uh..."
    "I stammered for bit, confused, until I looked at [soName]'s face."
    me "Your eyebrows!"
    so "Huh?"
    $ rand = renpy.random.choice(('right', 'left'))
    me "Your [rand] eyebrow fell off."
    $ soNoun = getPronoun(soGender, 'Possessive')
    "[soName] touched where [soNoun] eyebrow was to confirm."
    so "Ugh, so it is. *Sigh*, can't go around looking like this."

    menu:
        so "Do you have something to cover it?"

        "Hand over the hat." if 'Hat' in inventory:
            $ inventory.remove('Hat')
            me "You can use this hat to cover the brow."
            "I hand over my hat."
            so "Hey, nice going."
            "[soName] looks over at the closest store window, and adjusts the hat on [soNoun] head."
            so "Nice!"

        "Use a handkerchief as a makeshift hat." if 'Handkerchief' in inventory:
            $ inventory.remove('Handkerchief')
            me "I've got a handkerchief. You can use it like a hat."
            me "That way, you can cover the brow pretty easily."
            so "Good idea!"
            "I hand over my handkerchief."
            "[soName] looks over at the closest store window, and adjusts the handkerchief on [soNoun] head."
            so "Good enough."

        "Apply a band-aid to the missing brow." if 'Band-Aid' in inventory:
            $ inventory.remove('Band-Aid')
            me "Here's a band-aid that we can use to cover the brow."
            so "Wow, good call! Can you help me stick it on here?"
            "[soName] points to [soNoun] brow, gesturing for me to put the band-aid on."
            me "Sure thing."
            "I apply the band-aid to [soNoun] missing brow."

            # Skin-touch = improved probability of success...is my internal line of thinking
            $ probabilityOfSuccess += 0.1
            me "Done."
            so "Many thanks!"

        "Wrap the bandage over the missing brow." if 'Bandage' in inventory:
            $ inventory.remove('Bandage')
            me "Uh, well I got this bandage that you can wrap around your head to cover the missing brow."
            so "That...sounds like overkill."
            $ probabilityOfSuccess -= 0.1
            me "*Shrug*, maybe you can say you're cosplaying."
            so "I was more concerned that I was using up so much of your bandage for something so simple."
            me "Oh."
            "We applied the bandage over [soNoun] head anyway."
        "Apologize." if 'Hat' not in inventory:
            $ probabilityOfSuccess -= 0.2
            me "Sorry, I have nothing."
            so "Oh, well. I'll live."
    jump endStreets

label streetsLostEarLobe:
    # FIXME: this needs dialogue!
    jump endStreets

label streetsLostTooth:
    # FIXME: this needs dialogue!
    jump endStreets

label endStreets:
    "Placeholder text: then [soName] loses [bodyPart]. But that's OK, cause we hid it with a hat!"
    if renpy.random.random() < probabilityOfSuccess:
        "Placeholder text: also, we made it to the park!"
        jump park
    else:
        jump gameover

    # This ends the game.
    return
