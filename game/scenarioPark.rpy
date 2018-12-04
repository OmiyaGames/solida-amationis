# The game starts here.
define lostBodyPart = "eye"
label park:

    # Switch to scene 1
    scene bg park
    $ scenario = 'park'
    $ conversationPhase = 0

    # Describe the park
    "The biting wind eases into a brisk breeze.  Finally you can relax and let the day come at its own pace."
    "The riverside park was small, with one side housing an amphitheater and the other, rather jarringly, a parking lot larger than the park itself."
    so "I used to walk this riverside often as a kid."
    me "Heh, must be relaxing watching the boats go by."
    so "Yes it is."
    "Only a few people were walking around the area. Given the cold weather, no kids were hanging around either."
    "We picked a bench to watch time go by."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand) from _call_conversation_1

    # Start the body-loss section
    "After a few minutes of conversation, you notice that [soName] is shivering."
    me "Is everything alright?"
    so "*COUGH*"

    stop music fadeout 1.0
    play music "Horror 2.mp3"
    "I jumped. This sounded far more severe than before."
    me "[soName]!!"
    "I quickly got up and rushed in front of [soName]."
    me "[soName], are you-"

    # Check if SO survives
    if renpy.random.random() < probabilityOfSuccess:

        # If so, jump to a random body loss situation
        if renpy.random.randint(0, 2) == 0:
            jump parkLostEyeball
        else:
            jump parkLostFinger
    else:
        # if not...
        jump gameover

    # For safety reasons, adding a return to end the game.
    # Should never arrive here, anyway.
    return

label parkLostEyeball:
    "[soName] was holding an eyeball."
    so "I..."

    $ rand = renpy.random.choice(('right', 'left'))
    $ soNoun = getPronoun(soGender, 'Possessive')
    "[soName] looked up, [soNoun] empty [rand] eyesocket starring back."
    so "What should I do?"
    "[soNoun] other eye blurs, ready to cry."
    $ lostBodyPart = "eye"

    jump endPark

label parkLostFinger:
    "[soName] was holding a severed finger."
    so "I..."

    $ rand = renpy.random.choice(('right', 'left'))
    $ soNoun = getPronoun(soGender, 'Possessive').title()
    "[soNoun] [rand] hand was visibly missing a finger."
    so "What should I do?"
    "[soNoun] eyes blurs, ready to cry."
    $ lostBodyPart = "finger"
    jump endPark

label endPark:
    me "W-we call the ambulance."

    $ soNoun = getPronoun(soGender, 'Possessive')
    if 'Smartphone' in inventory:
        "Despite all the shaking, I manage to find the strength to pull my phone and dial the emergency."
    else:
        so "I...I forgot my phone."
        me "Don't worry, I-"
        "I checked my pockets."

        # Oh, noez!
        $ probabilityOfSuccess -= 0.3
        me "...crud, I don't have mind, either."
        "I must have left it back home."
        so "W-we'll need to ask from someone else."
        me "I-I'll take care of it."
        "I ran to the closest stranger I could find."
        me "Can I borrow your phone!? We have a medical emergency!!"
        "Fortunately, the stranger was kind enough to offer one.  I dialed the emergency immediately."

    me "Y-yes, this is [meName]. W-we need treatment for [soName] who just lost [soNoun] [lostBodyPart]!"
    "In my panic, I stuttered where we were located, and answered questions as best I could."
    "Eventually, the receiver assured us they'll be coming shortly."
    stop music fadeout 1.0
    play music "Cafe.mp3"

    if 'Smartphone' in inventory:
        "I sit next to [soName]."
    else:
        "I thank the stranger and return their phone before running back to [soName]."

    me "They said they'll be coming shortly."
    so "..."
    "We cuddled and waited. It seemed like forever."
    "After a while, I noticed the sirens coming closer."
    me "Look, they're here!"

    # Check if SO survives
    if renpy.random.random() < probabilityOfSuccess:
        # Move to the hospital.
        "Sure enough, the blarring lights filled the view. [soName] was going to make it."
        jump hospital
    else:
        jump gameover

    # This ends the game.
    return
