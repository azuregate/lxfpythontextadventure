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
    def __init__(self, name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc):
        self.name = name
        self.itemdesc = itemdesc
        self.updroomdesc = updroomdesc
        self.portable = portable
        self.revealsitem = revealsitem
        self.usedin = usedin
        self.usedesc = usedesc
        self.removesroomitem = removesroomitem
        self.addsroomitem = addsroomitem
        self.useroomdesc = useroomdesc


lockedchest = Item("Chest", "A very sturdily built CHEST. It's securely locked.", None, False, None, None, None, None, None, None)
ruby = Item("Ruby", "A very large and valuable ruby.", None, True, None, None, None, None, None, None)
brokenchest = Item("Broken Chest", "The BROKEN CHEST lies in splinters thanks to your efforts with the axe.", None, False, ruby, None, None, None, None, None)
axe = Item("Axe", "The AXE is caked with dirt but you can see it's still razor sharp.",
"You see the skeleton of a dwarf.", True, None, 2, "You use the axe to smash open the chest.",lockedchest, brokenchest, "You see a BROKEN CHEST.")

nextroom = Room(2, "South Chamber", "You see an old chest.", [None, None, None, None], None, None)
nextroom.items = [lockedchest]

player_name = input("What is your name, brave adventurer? ")
print("Greetings", player_name + "!")

player = Player(player_name, nextroom, [], [axe])


def trytotake(item):
    current_room = player.currentroom

    for room_item in current_room.items:
        if room_item.name.lower() == item.lower():
            if room_item.portable:
                player.inventory.append(room_item)
                current_room.items.remove(room_item)
                print("You have taken the", room_item.name + ".")
                if room_item.updroomdesc is not None:
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


def trytouse(item):
    current_room = player.currentroom

    for inventory_item in player.inventory:
        if inventory_item.name.lower() == item.lower():
            if inventory_item.usedin == current_room.number:
                if inventory_item.removesroomitem is not None:
                    current_room.items.remove(inventory_item.removesroomitem)
                if inventory_item.addsroomitem is not None:
                    current_room.items.append(inventory_item.addsroomitem)
                print(inventory_item.usedesc)
                current_room.description = inventory_item.useroomdesc
                return
            else:
                print("You can't use the", inventory_item.name, "here.")
                return

    print("You don't have the", item + ".")


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
    elif action_input.lower().startswith("use "):
        item_name = action_input[4:]
        trytouse(item_name)
    else:
        print("You can't do that.")