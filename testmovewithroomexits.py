class room:
    def __init__(self, number, name, description, exits):
        self.number = number
        self.name = name
        self.description = description
        self.exits = exits

class player:
    def __init__(self, name, currentroom):
        self.name = name
        self.currentroom = currentroom

room1 = room(1, "Main Cavern", "You are standing in a dark cavern. You hear the sound of dripping water.",[None,None,None,None])
room2 = room(2, "North Chamber", "You see the skeleton of a dwarf holding an axe.",[None,None,None,None])
room3 = room(3, "South Chamber", "You see an antique wooden chest. It's locked.",[None,None,None,None])
room4 = room(4, "East Chamber", "You see entrance to the cave where you entered earlier.",[None,None,None,None])
room5 = room(5, "West Chamber", "You see an iron grille set into the wall. Someone has prised it open.",[None,None,None,None])

room1.exits = [room2, room3, room4, room5]
room2.exits = [None, room1, None, None]
room3.exits = [room1,None,None,None]
room4.exits = [None,None,None,room1]
room5.exits = [None,None,room1,None]


player.name = input("What is your name, brave adventurer? ")
print("Greetings ", player.name,"!")
player.currentroom = room1


def move():
    print (player.currentroom.name)
    print (player.currentroom.description)
    print("Which way will you go?")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N'] and player.currentroom.exits[0] != None:
            player.currentroom = player.currentroom.exits[0]
            move()
        elif action_input in ['s', 'S'] and player.currentroom.exits[1] != None:
            player.currentroom = player.currentroom.exits[1]
            move()
        elif action_input in ['e', 'E'] and player.currentroom.exits[2] != None:
            player.currentroom = player.currentroom.exits[2]
            move()
        elif action_input in ['w', 'W'] and player.currentroom.exits[3] != None:
            player.currentroom = player.currentroom.exits[3]
            move()
        else:
            print("You cannot go that way.")


def get_player_command():
    return input('Action: ')


move()