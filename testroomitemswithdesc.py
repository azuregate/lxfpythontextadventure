class Room:
    def __init__(self, number, name, description, exits, key, items):
        self.number = number
        self.name = name
        self.description = description
        self.exits = exits
        self.key = key
        self.items = items

class Player:
    def __init__(self, name, currentroom, keyring, inventory):
        self.name = name
        self.currentroom = currentroom
        self.keyring = keyring
        self.inventory = inventory

class Item:
    def __init__(self, name, itemdesc, updroomdesc, portable):
        self.name = name
        self.itemdesc = itemdesc
        self.updroomdesc = updroomdesc
        self.portable = portable

axe = Item("Axe", "The axe is caked with dirt but you can see it's still razor sharp.", "You see the skeleton of a dwarf.", True)
skeleton = Item("Skeleton", "The dwarf's skeleton is still wearing plate mail. The bones are yellowed.", None, False)

testroom = Room(1, "Old Tomb", "You see the skeleton of a dwarf holding an axe.", [None, None, None, None], None, None)
testroom.items = [axe, skeleton]

player_name = input("What is your name, brave adventurer? ")
print("Greetings", player_name + "!")

player = Player(player_name, testroom, [], [])

def trytotake(item):
    current_room = player.currentroom

    for room_item in current_room.items:
        if room_item.name.lower() == item.lower():
            if room_item.portable:
                player.inventory.append(room_item)
                current_room.items.remove(room_item)
                if room_item.updroomdesc != None:
                    current_room.description = room_item.updroomdesc
                print("You have taken the", room_item.name + ".")
            else:
                print("You can't pick up the", room_item.name + ". It can't be moved.")
            return

    print("There is no", item + " here.")

def listinventory():
    print(player.name + ", you are carrying:")
    if not player.inventory:
        print("Nothing.")
    else:
        for item in player.inventory:
            print(item.name)

def lookat(item):
    for room_item in player.currentroom.items:
        if room_item.name.lower() == item.lower():
            print(room_item.itemdesc)
            return

    for inventory_item in player.inventory:
        if inventory_item.name.lower() == item.lower():
            print(inventory_item.itemdesc)
            return

    print("There is no", item + " here.")

while True:
    print(player.currentroom.name)
    print(player.currentroom.description)

    action_input = input("What would you like to do? ")

    if action_input.lower().startswith("take "):
        item_name = action_input[5:]
        trytotake(item_name)
    elif action_input.lower() == "inventory":
        listinventory()
    elif action_input.lower().startswith("look "):
        item_name = action_input[5:]
        lookat(item_name)
    else:
        print("You can't do that.")