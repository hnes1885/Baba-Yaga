# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(what_italic=True) #narrator, script is always in italics to indicate
define v = Character(_("Vasilisa"), color="#c8ffc8") #main character
define f = Character(_("Ivan"), color="#c8c8ff") #main character's father
define baba = Character("Baba Yaga")

image vas = "images/Vasilisa.png"
image ba = "images/Baba_Yaga.png"
image wheel = "images/Wheel.png"

#defining stats here that will increase/decrease with character interactions with NPCs and impact the ending of your relationship with the NPCs 
default respect = 0
default affection = 0

init python:
    def click_counter():
        global clicks
        global timer

        if clicks == 0:
            timer = True

        clicks += 1

    def reset_click_counter():
        global clicks 
        global timer
        global countdown
        global count_clicks

        clicks = 0
        timer = False
        count_clicks = True
        countdown = 5

transform button_hover:
    on hover:
        easein 0.2 zoom 1.05
    on idle:
        easein 0.2 zoom 1.0

transform rotate_rays:
    rotate 0
    linear 50 rotate 360
    repeat

screen click_counter_game:
    image "Black.png"
    key "K_x" action If(count_clicks, Function(click_counter), NullAction())
    image "rays.png" xalign 0.5 yoffset -45 at rotate_rays
    image "Spindle.png" align(0.5, 0.4)
    text "Clicks: [clicks] Time left: [countdown]" align(0.5, 0.65) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
    imagebutton idle "Wheel.png" align(0.5, 0.4) sensitive count_clicks action Function(click_counter) at button_hover

    if not count_clicks: # "count_clicks" is NOT True? If so the countdown timer ran out.
        if clicks < 10: # 0-9
            text "Try again" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            imagebutton idle "play-again-button.png" align(0.5, 0.84) action Function(reset_click_counter) at button_hover
        elif clicks < 20: # 10-19
            text "That's pretty good!" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
        elif clicks < 30: # 20-29
            text "Wow, you're fast!" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            
        else: # 30 or more.
            text "You've got skills!" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            
            
        #imagebutton idle "play-again-button.png" align(0.5, 0.84) action Function(reset_click_counter) at button_hover
        textbutton "End" align(0.5, 0.84) action Return()

    if timer:
        timer 1.0 action If(countdown > 0, SetVariable("countdown", countdown - 1), SetVariable("count_clicks", False)) repeat countdown > 0

default clicks = 0
default count_clicks = True
default timer = False
default countdown = 5

# The game starts here.
label start:

    scene bg forest
    with fade

    # show background image of map
    # These display lines of dialogue.
    "In a certain kingdom in a certain land, in a little village on the edge of an ancient forest, there lived an apothecary and his young daughter, [v]."
    # show background of an apothecary
    show bg apothecary
    with fade
    "The two of them worked from sunrise to sunset alongside each other to run their small business."
    # show image of them foraging
    "At sunrise, they awoke to forage for ingredients to use in their remedies."
    # show image of hands exchanging a vial
    "By midday they would have filled the medicine vials of their returning neighbors and fellow villagers."
    #show image of hand chopping root vegetables 
    "And by sundown they closed their small shop and would return home. The apothecary would busy himself preparing dinner while his daughter ensured their personal inventory was well stocked."
    #show black screen
    "For one could never know for certain when an ailment would befall oneself..."
    "At least this was what [v]'s father always said."
    "The apothecary was a man of relatively fine health, built of strong immunity and even stronger ethics, but one winter's evening he fell ill with a terrible sickness."
    "[v] did not know what to make of it. She poured over the books her father kept in the house but she could not find a cure for the symptoms he was showing."
    "She felt helpless, unable to consult her father on what she should do, for he was drifting in and out of feverish dillusion, and there was no other apothecary within riding distance."
    "Her only hope to save her father lay deep within the forest that skirted the village. She had heard stories of Baba Yaga, the Boneylegged One, and how she resided within the protection of the ancient trees."
    menu:

        "Faced with an impossible position, she decided..."

        "To venture into the forest":
            jump gointoforest

        "To stay and hope her father's illness resolved itself":
            jump stayathome

    # This ends the game.
    #return

label gointoforest:
    #show background image of forest
    "Unwilling to see her father suffer further, [v] ventured into the forest and walked all night in the bitter winds and icy cold until she finally found the witch's hut."
    #show background image of baba yaga hut on chicken legs
    show bg hut
    with fade
    "Upon sensing someone was near her home, Baba Yaga's voice rang out from the glowing mouth of the hut."
  
    #show vasilisa and baba yaga as they speak
    show ba at right 
    baba "Who dares approach my home?!"
    hide ba

    show vas at left
    v "Hello, Babushka--"
    hide vas

    show ba at right
    baba "Who are you?! Speak up, girl!"
    hide ba

    show vas at left
    v "My name is Vasilisa and I am here to seek your assistance. My father--"
    hide vas

    show ba at right
    baba "What care have I for your wretched father? Be gone before I--"
    hide ba

    show vas at left
    menu:
        "Vasilisa interrupted the old woman, deciding her best option was to... "

        "Flatter and beg":
            jump beg
        "Stand her ground and raise her voice":
            #add +1 to respect variable
            jump standground

label beg:
    v "Please! My father is sick and I do not know how to aid him."
    v "I have heard you have knowledge that can heal unknown sicknesses."
    hide vas

    show ba at right
    baba "In some ways, yes. In other ways, no. Regardless, I am not in the business of tending to every pathetic welp that broaches my doorstep."
    baba "Now be gone!"
    hide ba

    menu: 
        "The witch would clearly need more convincing if Vasilisa was to succeed in aiding her father. She decided to..."

        "Stand her ground":
            #add +1 to respect variable
            jump standground
        "Offer her labor in exchange":
            #add +1 to respect variable
            jump offerwork

label standground:
    show vas at left
    v "I will not! I have walked for hours in the dark and cold to seek your aid and I will not return empty handed to watch my father wither and die because an old crone shooed me away!"
    
    "[v]'s voice echoed into the highest branches of the trees, her words frosting in the wicked midnight air."
    
    "Baba Yaga looked the young woman up and down before scoffing through her nose at her."

    baba "Is that so?"
    baba "Well if you insist on being a brat, I suppose I can offer you something to get you off my hide."
    baba "But make no mistake, girl, I will need something in exchange for your demand of my services."

    jump offerwork

label offerwork:
    v "I can work for you."

    baba "Hmmff, you hardly look the type. I need a girl who can work with her hands. What work can you do?"

    jump tasks

label tasks:
    menu:
        v "I can..."
        "Forage and brew medicine":
            jump forageAndBrew
        "Read and write":
            jump read
        "Spin yarn":
            jump spin
    

label forageAndBrew:
    #a foraging mini game 
    #find a necklace in the forest
    #followed by scene with baba yaga to establish character relationship development
    #will need to create an inventory for this part of the game
    "drag and drop minigame"
    jump tasks

label read:
    #a memory mini game
    #followed by scene with baba yaga to establish character relationship development
    #
    "memory minigame"
    jump tasks

label spin:
    #a spindle minigame where you can spin yarn and make cloth
    #followed by scene with baba yaga to establish character relationship development
    "timer click minigame"
    call screen click_counter_game
    screen hide
    jump afterTasks
    #jump tasks
    

#rest of story after the tasks are completed:
label afterTasks:
    v "I have completed all the tasks you asked of me, Babushka."
    "The witch sniffed at her, hardly glancing up from her pot."
    baba "So it seems."
    baba "I suppose you expect the medicine for your sickly father now, eh?"
    "She sighed through her nose and lifted her spoon from the pot in front of her, laddling a small amount of the brew into a waiting vial before handing it to her."
    baba "This should be more than enough to cure him of his ailment. Tell your father to look after himself unless he wishes to send his daughter to inconvenience others again."
    baba "I don't wish for your spoiled hide to darken my doorstep yet again so soon."
    
    menu:
        "[v] spoke, taking the vial"
        "Thank you, Babushka":
            #add +1 to respect variable
            #add +1 to affection variable
            jump thankYou
        "And I have no wish to return so soon and labor under withering eye yet again":
            #add +1 to respect variable
            #add +1 to affection variable
            jump snark

#have baba give her a skull light like in the story to guide her way home
#then as she leaves, give the option of leaving a necklace/piece of cloth she made/wove as a parting gift/possible promise to return one day maybe
#this will give more emotional impact to their relationship developed over the story
#note: can only have this choice pop up if respect and affection are above a certain threshold
label thankYou:
    "There was a moment of quiet, broken only by the quiet song of the winter wind."
    baba "Go on now, away with you."
    "The woman sniffed again as [v] turned to leave the hut."
    "But she could have sworn she saw a wry smile gracing the witch's face before she stepped out into the night."
    jump continueToFather
label snark:
    "[b]'s laugh was as harsh a bark as her yell, yet it carried with it hardly the same bite."
    baba "Go on now, brat, while the night is still young."
    jump thankYou

label continueToFather:

#Bad ending
label stayathome:
    #black screen
    "Instead of venturing into the wood, she opted to stay and tend to her father as best she could."
    "By the end of the week, her father was dead and she was left alone and destitute, for this was a time when women could not inherit property, and as such, she was unable to use her father's business to support herself."
    "Such is the fate of a woman in times like these."
    "{b}Bad Ending{/b}"
    return
