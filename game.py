def intro():
    print "[Intro]"


def handle_room(room_name):

    friendly_name = "Unknown"

    operations = None
    if room_name == "start_room":
        friendly_name = "Start room"
        operations = [["north","empty_cave_north"],["south","gold_room"],["east","empty_cave_east"],["west","empty_cave_west"]]
        print "You find yourself in a cave with a flickering torch on the wall."
        print "You can make out four paths, each equally as dark and foreboding."
    elif room_name == "empty_cave_north":
        print "Another unremarkable part of the cave. You must forge onwards."
        friendly_name = "Empty cave"
        operations = [["north", "empty_cave_north"], ["south", "start_room"]]
    elif room_name == "empty_cave_east":
        print "Another unremarkable part of the cave. You must forge onwards."
        friendly_name = "Empty cave"
        operations = [["west", "start_room"], ["east", "dagger_room"]]
    elif room_name == "empty_cave_west":
        print "Another unremarkable part of the cave. You must forge onwards."
        friendly_name = "Empty cave"
        operations = [["west", "giant_spider_room"], ["east", "start_room"]]
    elif room_name == "giant_spider_room":
        print "A giant spider jumps down from its web in front of you!"
        friendly_name = "Spider"
        operations = [["east", "empty_cave_west"]]
    elif room_name == "dagger_room":
        print "You notice something shiny in the corner."
        print "It's a dagger! You pick it up."
        friendly_name = "Dagger"
        operations = [["west", "empty_cave_east"]]

    print "Room: " + friendly_name

    return operations


def play():
    intro()

    game_over = False
    room_name = "start_room"
    while not game_over:
        operations = handle_room(room_name)

        print "Choose an action?"
        input = raw_input()

        if input == "quit":
            game_over = True;
        else:
            found = False
            for direction, name in operations:
                if input == direction:
                    found = True
                    print "Moving " + direction
                    room_name = name
                    break

            if not found:
                print "'" + input + "' is not a valid action."

    print "Game over"

play()

