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
#variables to keep track of the tasks completed:
default spinning = 0
default reading = 0
default foraging = 0
default necklace = False

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
            text "This is hardly enough. Baba Yaga will not be pleased with this amount." align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            imagebutton idle "play-again-button.png" align(0.5, 0.84) action Function(reset_click_counter) at button_hover
        elif clicks < 20: # 10-19
            text "This is still not enough." align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            imagebutton idle "play-again-button.png" align(0.5, 0.84) action Function(reset_click_counter) at button_hover
        elif clicks < 30: # 20-29
            text "I need just a bit more." align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            imagebutton idle "play-again-button.png" align(0.5, 0.84) action Function(reset_click_counter) at button_hover
        else: # 30 or more.
            text "This should be enough" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
            textbutton "End" align(0.5, 0.84) action Return()
            
        imagebutton idle "play-again-button.png" align(0.5, 0.94) action Function(reset_click_counter) at button_hover
        #textbutton "End" align(0.5, 0.84) action Return()

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
            $ respect += 1
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
            $ respect += 1
            jump standground
        "Offer her labor in exchange":
            #add +1 to respect variable
            $ respect += 1
            jump offerwork

label standground:
    show vas at left
    v "I will not! I have walked for hours in the dark and cold to seek your aid and I will not return empty handed to watch my father wither and die because an old crone shooed me away!"
    hide vas
    "[v]'s voice echoed into the highest branches of the trees, her words frosting in the wicked midnight air."
    
    "Baba Yaga looked the young woman up and down before scoffing through her nose at her."
    show ba at right
    baba "Is that so?"
    baba "Well if you insist on being a brat, I suppose I can offer you something to get you off my hide."
    baba "But make no mistake, girl, I will need something in exchange for your demand of my services."
    hide ba
    jump offerwork

label offerwork:
    show vas at left
    v "I can work for you."
    hide vas
    show ba at right
    baba "Hmf, you hardly look the type. I need a girl who can work with her hands. What work can you do?"
    hide ba
    jump tasks

label tasks:
    show vas at left
    "I can..."
    menu:
        "Forage":
            $ foraging += 1
            jump forage
        "Read":
            $ reading += 1
            jump read
        "Spin yarn":
            $ spinning += 1
            #"spinning is now: [spinning]" #delete this later
            jump spin
    

label forage:
    #a foraging mini game 
    #find a necklace in the forest --- will be able to take it with or leave it with baba as a promise to return one day
    #followed by scene with baba yaga to establish character relationship development
    #will need to create an inventory for this part of the game
    "drag and drop minigame"
    $ necklace = True
    "necklace is obtained: [necklace]"
    jump tasks

label read:
    #a memory mini game
    #followed by scene with baba yaga to establish character relationship development
    #
    
    "memory minigame"

    #once it is done:
    "The witch seemed slightly less ornary to see the young woman had managed to make sense of the mess."
    jump tasksAfterRead

label spin:
    #a spindle minigame where you can spin yarn and make cloth
    #followed by scene with baba yaga to establish character relationship development
    hide vas
    call screen click_counter_game #call on minigame screen
    if spinning == 1:
        "After a long day of spinning yarn, [v] showed the older woman her progress."
        "Baba Yaga sniffed in mild approval, glancing over the mountain of spool the young woman had managed to spin."
        show ba at right
        baba "Good enough..."
        hide ba
        "Her eyes briefly took in the state of the girl's hands."
        show ba at right
        baba "Up with you now. I'll have another task for you tomorrow at dawn."
        hide ba
        "[v] stood up from her seat."
        show vas at left
        v "But my father--"
        hide vas
        show ba at right
        baba "Your father will be fine."
        hide ba
        "The witch waved her hand dismissively."
        show vas at left
        v "You don't understand. When I left him he had a chill and was bed ridden." 
        v "He's unable to care for himself. If I don't return soon--"
        hide vas
        show ba at right
        baba "As I said, he will be fine. Your father will live if you perform your tasks, girl."
        baba "Now, you can sleep by the fire tonight. I expect you up and working at dawn."
        baba "And lotion your hands with the balm on the mantle. I won't tolerate lackluster work tomorrow because you have blisters."
        hide ba
        #show background image of fireplace
        "[v] fell asleep by the fire that night, consumed by worried thoughts for her father."
        "She prayed he would live through the night."
        show vas at left
        v "I'll be home soon, папа."
        hide vas
        "She whispered into the embers as she drifted into an exhausted sleep, the wind outside whistling a lullaby."
        jump nextMorning
    elif spinning == 2:
        show ba at right
        baba "Hmf, decent."
        hide ba
        "The old woman groused as she took in the spools of yarn [v] had managed to spin yet again."
        "Had she not known any better, [v] could have sworn she saw a glint of approval in the woman's eye."
        $ respect += 2
        show ba at right
        baba "That's enough for today."
        hide ba
        "Upon leaving the little back room of the hut, [v] was surprised to see the table set with a small meal."
        "When the old woman told her to sit and eat, she did not protest."
        "They sat and ate in relative silence until the witch spoke."
        show ba at right
        baba "You don't spin very often, do you, girl?"
        hide ba
        "[v] glanced up from her bowl, which she had been devouring only a moment before."
        show vas at left 
        v "No...It is not my usual work."
        hide vas
        show ba at right
        baba "I expected as much from the state of your palms. Soft as petals."
        baba "What work do you do then?"
        hide ba
        show vas at left
        v "My father is an apothecary. He has been teaching me to be one for most of my life."
        hide vas
        "[b] made a noise of mild disapproval."
        show ba at right
        baba "What of your mother? How is she to tolerate a daughter that cannot perform such household responsibilities?"
        hide ba
        "A moment passed before [v] answered the woman's question."
        show vas at left
        v "My mother passed when I was young."
        v "My father took me on as an apprentice shortly after. He wanted me to have a skillset that would provide me with enough to get by..."
        v "In case anything happened to him."
        hide vas
        "The witch appeared to have nothing to say to this."
        "They ate the rest of the meal in silence before it was time to rest for the night."
        "After cleaning their dishes, [v] went to lay by the fire yet again and found a blanket beside the straw mat on the floor."
        "Wrapping herself in it and settling into to the warm embrace of the fire, she drifted off."
        jump finalMorning
    elif spinning == 3:
        "At the end of the final day, [baba] came to inspect the young woman's work yet again."
        "And again, she could find no fault in the quality of the work the girl had produced."
        jump afterTasks

label nextMorning:
    #show new background image of fireplace fading in for smoother transition to morning
    "Upon the next morning, just as she had promised, the witch put [v] to work."
    "The cool morning air was enough to chase off any lingering sleep from her body."
    jump tasks

label finalMorning:
    "[v] awoke to find herself covered with a second horsehair blanket."
    "A new snow had fallen upon the forest outside, leaving the chicken leg hut in great need of warmth as the fire had died during the night."
    "The witch startled her when her slightly raspy voice broke her from her thoughts."
    show ba at right
    baba "Waste no more of the day, girl. There's still work to be done."
    hide ba
    "The witch hobbled outside the hut and climbed into her mortar."
    show ba at right
    baba "I expect to find you still working when I return."
    hide ba
    "Using her pestal, she launched herself into the air on her mortar, soaring into the treetops."
    "[v] was left to herself and her work yet again."
    jump tasks


#rest of story after the tasks are completed:
label afterTasks:
    show vas at left
    v "I have completed all the tasks you asked of me."
    hide vas 
    "The witch sniffed at her, hardly glancing up from her pot."
    show ba at right
    baba "So it seems."
    baba "I suppose you expect the medicine for your sickly father now, eh?"
    hide ba
    "She sighed through her nose and lifted her spoon from the pot in front of her, laddling a small amount of the brew into a waiting vial."
    show ba at right
    baba "This should be more than enough to cure him of his ailment."
    hide ba
    "[baba] then took one of the skulls from a fence post and lit it inside before placing it on a stick, impatiently handed it to the young woman."
    show ba at right
    baba "This will aid your way home. Take it and be gone."
    baba "And tell your father to look after himself unless he wishes to send his daughter to inconvenience others again."
    baba "I don't wish for your spoiled hide to darken my doorstep yet again so soon."
    hide ba
    show vas at left
    menu:
        "[v] spoke, taking both the vial and the lantern..."
        "Thank you, косынка.":
            #add +1 to respect variable
            #add +1 to affection variable
            $ affection += 2
            jump thankYou
        "And I have no wish to return so soon and labor under withering eye yet again.":
            #add +1 to respect variable
            $ respect += 1
            #add +1 to affection variable
            $ affection += 1
            jump snark

#have baba give her a skull light like in the story to guide her way home
#then as she leaves, give the option of leaving a necklace/piece of cloth she made/wove as a parting gift/possible promise to return one day maybe
#this will give more emotional impact to their relationship developed over the story
#note: can only have this choice pop up if respect and affection are above a certain threshold
label thankYou:
    "There was a moment of quiet, broken only by the quiet song of the winter wind outside."
    show ba at right
    baba "Go on now, away with you."
    hide ba
    "The woman sniffed again, her voice carrying a distinct lack of venom as [v] turned to leave the hut."
    "But she could have sworn she caught a wry smile gracing the witch's face before she turned her back and made her way to the edge of the fence."
    jump leaveNecklace
label snark:
    "[b]'s laugh was as harsh a bark as her yell, yet it carried with it hardly the same bite."
    show ba at right
    baba "Go on now, brat, while the night is still young."
    jump thankYou

label leaveNecklace:
    if necklace == True:
        "[v] reached the edge of the witch's fence before looking back."
        "She felt in her pocket the familiar weight of the necklace she had found in the woods."
        menu:
            "Keep it":
                jump continueToFather
            "Leave it on the fence":
                "[v] placed the necklace on one of the skulls that lined the fence posts before looking back at the chicken legged hut."
                "The windows glowed with a similar warmth to the eyes of the lantern skulls."
                "She hoped in the back of her mind that the witch would see it and know it was a promise to return one day."
                jump continueToFather
    else:
        jump continueToFather

label continueToFather:
    "As she walked into the wood, [v] found herself strangely comforted with the idea that she would be able to find the witch again, should she ever need to."
    "She had no basis for this belief. It was simply a thought that felt as certain as the ground beneath her feet and the sky beyond her head."
    "[baba] would be there, should she ever need her."
    "Of this, she was certain."

#Bad ending
label stayathome:
    #black screen
    "Instead of venturing into the wood, she opted to stay and tend to her father as best she could."
    "By the end of the week, her father was dead and she was left alone and destitute, for this was a time when women could not inherit property, and as such, she was unable to use her father's business to support herself."
    "Such is the fate of a woman in times like these."
    "{b}Bad Ending{/b}"
    return
