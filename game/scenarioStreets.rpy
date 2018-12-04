# The game starts here.
label streets:

    # Switch to scene 1
    scene bg streets A
    $ scenario = 'streets'
    $ conversationPhase = 0

    # These display lines of dialogue.
    "You walk against the raging wind.  Every few steps, you look at the ground to watch for black ice.  Frost creeps over the discolored concrete.  You can't wait to get to the park."
    me "Lead me the way."
    so "Gladly. It's just straight this way."
    "We passed some local stores, many of them empty.  To pass some time, we conversed."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)

    # Start the body-loss section
    so "*Cough, cough*"
    "It appeared [soName]'s coughs were getting worse."
    me "Are you alright?"
    so "Yeah, I think so-"

    # Change music
    stop music fadeout 1.0
    play music "Horror 2.mp3"
    "[soName] suddenly jutted forward, as if to throw up."
    me "[soName]!!"
    $ soNoun = getPronoun(soGender, 'Possessive')
    "As I rushed to [soNoun] side, I saw [soName] holding holding something."

    # Jump to a random body loss situation
    $ rand = renpy.random.randint(0, 3)
    if rand == 0:
        jump streetsLostEyebrow
    else:
        jump streetsLostEarLobe

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

            $ soNounPersonal = getPronoun(soGender, 'Personal').title()
            "[soName] looks over at the closest store window, checking [soNoun] reflection.  [soNounPersonal] adjusts the hat on [soNoun] head."
            so "Nice!"

        "Use a handkerchief as a makeshift hat." if 'Handkerchief' in inventory:
            $ inventory.remove('Handkerchief')
            me "I've got a handkerchief. You can use it like a hat."
            me "That way, you can cover the brow pretty easily."
            so "Good idea!"
            "I hand over my handkerchief."

            $ soNounPersonal = getPronoun(soGender, 'Personal').title()
            "[soName] looks over at the closest store window, checking [soNoun] reflection.  [soNounPersonal] adjusts the handkerchief on [soNoun] head."
            so "Good enough."

        "Apply a band-aid to the missing brow." if 'Band-Aid' in inventory:
            $ inventory.remove('Band-Aid')
            me "Here's a band-aid that we can use to cover the brow."
            so "Wow, good call! Can you help me stick it on here?"
            "[soName] points to [soNoun] brow, gesturing for me to put the band-aid on."
            me "Sure thing."
            "I apply the band-aid to [soNoun] missing brow."

            # Skin-touch = improved probability of success...is my internal line of thinking
            $ probabilityOfSuccess += 0.05
            me "Done."
            so "Many thanks!"

        "Wrap the bandage over the missing brow." if 'Bandage' in inventory:
            $ inventory.remove('Bandage')
            me "Uh, well I got this bandage that you can wrap around your head to cover the missing brow."
            so "That...sounds like overkill."
            $ probabilityOfSuccess -= 0.05
            me "*Shrug*  Just say you had a head injury."
            so "I was more concerned that I was using up so much of your bandage for something so simple."
            me "Oh."
            "We applied the bandage over [soNoun] head anyway."

        "Apologize." if 'Hat' not in inventory:
            $ probabilityOfSuccess -= 0.2
            me "Sorry, I have nothing."
            so "Oh, well. I'll live."
    jump endStreets



label streetsLostEarLobe:
    "It was a small piece of flesh."
    me "Oh..."
    "I feel sick and confused."
    $ rand = renpy.random.choice(('right', 'left'))
    so "My [rand] ear feels...lighter."
    "I looked up at [soName]'s face."
    me "That's stra-{p}It's gone."
    so "What?"
    me "Your [rand] earlobe.  It's gone."

    $ soNoun = getPronoun(soGender, 'Possessive')
    "[soName] puts [soNoun] hand on [soNoun] [rand] ear to confirm."
    so "Yikes."

    $ soNoun = getPronoun(soGender, 'Personal')
    "[soNoun] tries to reattach the small flesh to the missing earlobe."

    menu:
        so "Do you have something to fix this?"

        "Apply a band-aid to reattach the earlobe." if 'Band-Aid' in inventory:
            $ inventory.remove('Band-Aid')
            me "Maybe this band-aid might reattach the earlobe.  Temporarily."
            so "Hmm, worth a shot. Can you help me?"

            $ soNoun = getPronoun(soGender, 'Possessive')
            "[soName] hands me [soNoun] her earlobe.  I take it, and tape the flesh and ear together."
            me "I think I got it."
            "[soName] looks over at the closest store window, and checks [soNoun] reflection."

            # Skin-touch = improved probability of success...is my internal line of thinking
            $ probabilityOfSuccess += 0.05
            so "Looks good to me!"

        "Wrap the bandage over the missing brow." if 'Bandage' in inventory:
            $ inventory.remove('Bandage')
            me "You can wrap this bandage around your head to keep it protected from outside elements."
            so "Good call, thank you."

            $ probabilityOfSuccess -= 0.1
            $ soNoun = getPronoun(soGender, 'Possessive')
            $ soNounPersonal = getPronoun(soGender, 'Personal')
            $ soNounPersonalCaps = soNounPersonal.title()
            "[soNounPersonalCaps] puts the missing earlobe into [soNoun] pocket, then looks over at the closest store window. Using its reflection [soNounPersonal] wraps the bandage over [soNoun] head."
            so "All wrapped up."
            me "...Seriously?  A pun?"
            so "Cut me some slack, how would {i}you{/i} make this situation better?"
            me "Touché."

        "Hand over the hat." if 'Hat' in inventory:
            $ inventory.remove('Hat')
            me "You can use this hat to cover the ear."
            "I hand over my hat."
            me "It's not much."
            so "Still, I'll give it a shot."

            $ probabilityOfSuccess -= 0.05
            $ soNoun = getPronoun(soGender, 'Possessive')
            $ soNounPersonal = getPronoun(soGender, 'Personal')
            "[soName] puts the missing earlobe into [soNoun] pocket, then looks over at the closest store window. Using its reflection [soNounPersonal] adjusts the hat."
            so "Like nothing has ever happened."

        "Apologize." if 'Hat' not in inventory:
            $ probabilityOfSuccess -= 0.2
            me "Sorry, I have nothing."
            so "Oh, well. I'll live."
    jump endStreets



label endStreets:
    stop music fadeout 1.0
    play music "Cafe.mp3"

    $ soNoun = getPronoun(soGender, 'Possessive')
    "We walked a little farther until [soName] lifted [soNoun] hand."
    so "There's the park."
    "[soName] pointed at a small amphitheater emerging into view."
    me "Oh, neat."
    if renpy.random.random() < probabilityOfSuccess:
        jump park
    else:
        jump gameover

    # This ends the game.
    return
