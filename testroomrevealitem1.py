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
    def __init__(self, name, itemdesc, updroomdesc, portable, revealsitem):
        self.name = name
        self.itemdesc = itemdesc
        self.updroomdesc = updroomdesc
        self.portable = portable
        self.revealsitem = revealsitem

armour = Item("Armour", "A battered set of dwarf plate mail armour. It's not your size but could come in useful.", None, True, None)
axe = Item("Axe", "The axe is caked with dirt but you can see it's still razor sharp.","You see the skeleton of a dwarf.", True, None)
skeleton = Item("Skeleton", "The dwarf's skeleton is still wearing a suit of ARMOUR. The bones are yellowed.", None, False, armour)

testroom = Room(1, "Old Tomb", "You see the SKELETON of a dwarf holding an AXE.", [None, None, None, None], None, None)
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
                print("You have taken the", room_item.name + ".")
                if room_item.updroomdesc != None:
                    current_room.description = room_item.updroomdesc
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
            if room_item.revealsitem is not None:
                player.currentroom.items.append(room_item.revealsitem)
                print("You also see", room_item.revealsitem.name + ".")
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