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

    stop music fadeout 1.0
    play music "Hospital.mp3"
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
    me "Well, I better get going before it gets too late.  Hey, [soName], call me if you need any help."
    so "Will do."
    "I flash [soName] a smile before I leave."

    # Switch to streets, normal
    scene bg streets A
    "As I walk back home, I take a brief look at brochure.  The street lights are only bright enough to make a few sentences legible."
    me "\"Do you have Solida amationis?  Symptoms include:\""
    "Looks like any regular medical brochures."
    me "\"Coughs, chills, sneezes\" blah, blah."
    "My vision blurs for bit, mostly out of boredom.  But a line catches my eye."
    me "\"Patients also site experiencing physical paralysis when asked a question or when forced to make a decisio-\""
    me "{b}ACH-{/b}"
    "I cover my mouth.  As the sneeze comes in, I feel something slimey and round hit the palm of my hand."

    stop music fadeout 1.0
    "I{w=0.5} open{w=0.5} my{w=0.5} hand."

    # Switch to streets, cut in half
    scene bg streets B
    me "No..."
    "It's an eyeball."
    "{i}My eyeball.{/i}"
    me "No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no-"

    scene bg setup
    "{b}Credits{/b}"
    "Writers:{p}Taro Omiya{p}Muse en Lystrala{p}J. H. Freedman"
    "Music:{p}Muse en Lystrala"
    "Quality Assurance:{p}Frederika Edgington-Giordano"
    "Images:{p}\"Photograph of a Woman in a Coffee Shop\" by Igor Starkov"
    "Images cont.:{p}\"White Hospital Beds\" by Pixabay"
    "Images cont.:{p}Everything else by Taro Omiya"
    "Support us on Patreon!{p}Developer: {a=https://www.patreon.com/OmiyaGames}Omiya Games{/a}{p}Music:{a=https://www.patreon.com/geekmusica}Geek Musica{/a}"
    "Special Thanks:{p}Tech Valley Game Space{p}Ludum Dare 43{p}And you!"

    # This ends the game.
    return
