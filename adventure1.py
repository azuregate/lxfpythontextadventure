# Here we define the 'room', 'player' and key classes.

class room:
    def __init__(self, number, name, description, exits, key):
        self.number = number
        self.name = name
        self.description = description
        self.exits = exits
        self.key = key

class player:
    def __init__(self, name, currentroom, keyring):
        self.name = name
        self.currentroom = currentroom
        self.keyring = keyring

class key:
    def __init__(self, keyusedesc, keyroomdesc, keyexits):
        self.keyusedesc = keyusedesc
        self.keyroomdesc = keyroomdesc
        self.keyexits = keyexits

# Define the rooms, adding a name and description. No exits are set until all the rooms are declared.

room1 = room(1, "Main Cavern", "You are standing in a dark cavern. You hear the sound of dripping water.",[None,None,None,None], None)
room2 = room(2, "North Chamber", "You see the skeleton of a dwarf holding an axe.",[None,None,None,None], None)
room3 = room(3, "South Chamber", "You see an antique wooden chest. It's locked.",[None,None,None,None], None)
room4 = room(4, "East Chamber", "You see entrance to the cave where you arrived earlier. The gate is locked. It's stained red with rust.",[None,None,None,None], None)
room5 = room(5, "West Chamber", "You see an iron grille set into the wall. Someone has prised it open.",[None,None,None,None], None)
room6 = room(6, "Cave Entrance", "You step out blinking into the sunlight.",[None,None,None,None], None)

# Here the room exits are defined in a list in NSEW order.

room1.exits = [room2, room3, room4, room5]
room2.exits = [None, room1, None, None]
room3.exits = [room1,None,None,None]
room4.exits = [None,None,None,room1]
room5.exits = [None,None,room1,None]
room6.exits = [None,None,None,room4]

# Here we define the keys.

redkey = key("You use the red key to unlock the gate.", "You see the entrance to the cave where you arrived earlier. The red gate lies open.", [None,None,room6,room1])

# If a key is needed to unlock an exit in a room, we now add it here.

room4.key = redkey

# As the game starts players input their name. They start in Room 1 (Main Chamber).

player.name = input("What is your name, brave adventurer? ")
print("Greetings ", player.name,"!")


player.currentroom = room1
player.keyring = [None,None,None,None,redkey]

def checkkeys():
    currentroom = player.currentroom
    if currentroom.key != None and currentroom.key in player.keyring:
                print(currentroom.key.keyusedesc)
                currentroom.description = currentroom.key.keyroomdesc
                currentroom.exits = currentroom.key.keyexits
                currentroom.key = None
checkkeys()

def listexits():
    if player.currentroom.exits[0] != None:
        print("You see an exit to the North.")
    if player.currentroom.exits[1] != None:
        print("You see an exit to the South.")
    if player.currentroom.exits[2] != None:
        print("You see an exit to the East.")
    if player.currentroom.exits[3] != None:
        print("You see an exit to the West.")
listexits()

def move():
    while True:
        print (player.currentroom.name)
        print (player.currentroom.description)
        checkkeys()
        listexits()
        print("Which way will you go?")

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
