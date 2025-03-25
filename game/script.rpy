# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t_a = Character("Ticket Attendee")
define plli_a = Character("PLII A")
define plli_b = Character("PLII B")
define idk = Character("???")


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

    idk "%(p_name) hey?"

    # This ends the game.

    return
