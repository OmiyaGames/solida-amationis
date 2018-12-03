# The game starts here.
define cafeStaff = 'Waitress'
define staff = Character('[cafeStaff]')

label cafe:

    # Switch to scene 1
    scene bg cafe
    $ scenario = 'cafe'
    $ conversationPhase = 0

    "The aroma of espresso permeates the café.  You can hear the sizzle of a panini press and the chatter of a handful of customers."
    "A few romantic couples are scattered among the college students on their laptops."
    "You arrive a bit late.  So much for making a good first impression."

    # These display lines of dialogue.
    so "*Cough*"
    me "[soName], sorry I'm late!"

    if renpy.random.randint(0, 1) == 1:
        so "You kept me waiting."
        "Uh, oh, not good."
    else:
        so "Oh, no, you're fine."
        "Well, things might not be so bad after all."

    me "Huff, puff...well, are there anything good on the menu?"

    $ rand = renpy.random.choice(('The Californian', 'The Hot Mess', 'The Holmes', 'The Hudson'))
    so "There are some interesting sandwiches here.  I think I'm going to get [rand]."

    menu:
        me "Then I'll get..."

        "The Rensselaer":
            me "Gotta have those veggies."
            so "And roast beef, I presume?"
            me "You know me too well."
        "The Sage":
            me "The turkey and cranberry combination sounds intriguing."
        "The Uncle Sams":
            me "Can't go wrong with ham, cheese, and rye."
            so "You'd think this sandwich would have a more...patriotic mix."
        "The Watson":
            me "What can I say? I want a good old fashioned burger."
            so "With boiled onions and mushrooms."
            me "Yes, that too."
        "The Harvest Moon":
            me "Bageled sandwich with turkey and apple. Something different."

    python:
        cafeStaff = "waitress"
        if renpy.random.randint(0, 1) == 1:
            cafeStaff = "waiter"
    "As the [cafeStaff] came along, we placed the order."

    # Have a conversation
    $ rand = (renpy.random.randint(0, 1) == 1)
    call conversation(rand)

    # TODO: indicate what happens after the conversation
    "As we finish the conversation, the [cafeStaff] comes in and delivers our meals."
    staff "Bon Appétit!"

    "We chew down the food and commented on the delicious flavor of each meal. As we're finishing up the meal, suddenly, [soName] comments."
    so "Urk, I bit on something hard!"
    me "That doesn't sound good."
    so "Wait..."
    "[soName] spits out the hard object in question. It looks like...an entire fingernail?"
    me "Ugh, gross, I'm calling the [cafeStaff] about this."

    $ soNoun = getPronoun(soGender, 'Possessive')
    so "Yeah, plea- OH, WHAT!?"
    "[soName] exclaimed while looking at [soNoun] hand. The fingernail on [soNoun] has come clean off."

    menu:
        me "Yikes, what should I do?"

        "Apply a band-aid to the finger." if 'Band-Aid' in inventory:
            $ inventory.remove('Band-Aid')

        "Hand a handkerchief." if 'Handkerchief' in inventory:
            $ inventory.remove('Handkerchief')

        "Wrap the bandage around the finger." if 'Bandage' in inventory:
            # Doesn't really make much sense to remove bandage from the inventory
            # on such a small damage
            #$ inventory.remove('Bandage')
            pass

        "Ask [cafeStaff] for help.":
            $ probabilityOfSuccess -= 0.2

    me "Yikes, well, that was a frightning experience."
    so "Yeah, no kidding."
    "As we finished that conversation, the [cafeStaff] handed our check."
    "After we made the payment, we discussed where to go next."
    so "How about the park at the riverside? It's within walking distance."
    me "Yeah, I like that idea. A nice place to cool down and relax."

    # Move to the streets.
    jump streets
