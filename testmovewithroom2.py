class room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class player:
    def __init__(self, name, currentroom):
        self.name = name
        self.currentroom = currentroom

room1 = room("Main Cavern", "You are standing in a dark cavern. You hear the sound of dripping water.")
room2 = room("North Chamber", "You see the skeleton of a dwarf holding an axe.")
room3 = room("South Chamber", "You see an antique wooden chest. It's locked.")
room4 = room("East Chamber", "You see entrance to the cave where you arrived earlier. The gate is locked. It's stained red with rust.")
room5 = room("West Chamber", "You see an iron grille set into the wall.")

player.currentroom = room1

def move():
    print(player.currentroom.name)
    print(player.currentroom.description)
    print("Which way will you go?")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            player.currentroom = room2
            move()
        elif action_input in ['s', 'S']:
            player.currentroom = room3
            move()
        elif action_input in ['e', 'E']:
            player.currentroom = room4
            move()
        elif action_input in ['w', 'W']:
            player.currentroom = room5
            move()
        else:
            print("You cannot go that way.")


def get_player_command():
    return input('Action: ')


move()