# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t_a = Character("Ticket Attendee")
define plli_a = Character("PLII A")
define plli_b = Character("PLII B")
define idk = Character("???")
define p_name = Character("[p_name]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    #"The air blew through the line and you couldn’t help but shiver."
    #"The end of summer was close and fall was coming in."
    #"You couldn’t help but wonder what the future would hold."
    #t_a "Please step up to get your ticket!"
    #"The line you were standing in shuffled forward and you pulled your coat closer to you."
    #plli_a "I can’t believe we get to see them in person!"
    #plli_b "I know! It’s been so long since we got to see their debut teaser–this concert will go down in history!"
    #"You watched as the two fans huddled close, happily talking about the newest idol group."
    #"The very one you got to meet so long ago."
    #"A memory flickers in your mind and you couldn’t help but replay it…"

    # show bg temp with fade

    $p_name = renpy.input("What's your name?")
    $p_name = p_name.strip()
    if p_name == "":
        $p_name = "PLII"

    idk "%(p_name)s?"
    p_name "Uh, yeah... Sorry about that."
    idk "That’s alright. I understand. Is something bothering you?"
    "Seeing the gentle curve of his lips, you are reminded of who he is. To you."
    p_name "No. Sorry. I just slept late last night, that’s all."

    show yejun neutral

    "Nam Yejun. A high school friend. You lost touch with him two years ago. You remember grieving the companionship you shared. And you also remember moving on, with the melancholy that follows adulthood."
    show yejun happy
    yejun "Were you catching up on your favorite group’s reality show again?"
    p_name "Haha... how did you know..."
    "You also remember feeling elated when you met Yejun again 5 months ago."

    show yejun cheerful
    y "Because two weeks ago you texted me about how you planned on binging it after your project’s due date?"
    p_name "Ugh... Sometimes I hate how good you are at remembering my embarrassing moments..."
    "Yejun chuckles at your defeated tone, aquamarine eyes gleaming with fondness."
    "You wave a hand, signaling your desire to change the subject."
    p_name "Anyway... Enough about my moment of weakness. How’s your mission going?"

    show yejin confident
    "At that, Yejun’s posture straightened from his previous slouch on the cafe table."
    y "Well, first of all, thank you for remembering, despite your lack of sleep."
    "You notice a twinkle of mischief in his normally kind irises."
    p_name "Hey! I’m not that forgetful!"

    show yejun cheerful
    "He smiles, eyes disappearing behind rising cheeks amusingly."
    y "And second, it went amazing! We found our final member!"
    p_name "Oh my god! Congratulations!"
    y "Thank you. Thank you."
    "You lean across the table in excitement."
    p_name "Does that mean you will finally be able to settle on a debut date?"
    "Hearing your inquiry, his posture turns more subdued and creases the surface between his eyebrows."
    
    # This ends the game.

    return
