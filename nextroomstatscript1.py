class Room:
    def __init__(self, number, name, description, exits, key, items, enemies):
        self.number = number
        self.name = name
        self.description = description
        self.exits = exits
        self.key = key
        self.items = items
        self.enemies = enemies


class Player:
    def __init__(self, name, currentroom, keyring, hp, inventory, weapon):
        self.name = name
        self.currentroom = currentroom
        self.keyring = keyring
        self.hp = hp
        self.inventory = inventory
        self.weapon = weapon


class Item:
    def __init__(self, name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc, disposable):
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
        self.disposable = disposable

class StatItem(Item):
    def __init__(self, name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc, disposable, hp_change):
        super().__init__(name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc, disposable)
        self.hp_change = hp_change

class Weapon(Item):
    def __init__(self, name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc, disposable, damage):
        super().__init__(name, itemdesc, updroomdesc, portable, revealsitem, usedin, usedesc, removesroomitem, addsroomitem, useroomdesc, disposable)
        self.damage = damage

class Enemy:
    def __init__(self, name, alive, description, deaddesc, weapon, hp, loot):
        self.name = name
        self.alive = alive
        self.description = description
        self.deaddesc = deaddesc
        self.weapon = weapon
        self.hp = hp
        self.loot = loot



grille = StatItem("Grille", "The iron grille is old and rusty but you seem some sharp edges.", None, False, None, None, "You grasp the grille and try to move it but only manage to scratch your hand. Lose 3 HP", None, None, None, False, -3)
sword = Weapon("Sword", "A sharp and sturdy sword.", None, True, None, 0, "You swing the sword around with great skill.", None, None, None, False, 2)
room5 = Room(5, "West Chamber", "You see an iron grille set into the wall. Someone has prised it open.",[None,None,None,None], None, None, None)
room5.items = [grille,sword]

mace = Weapon("Mace", "A stubby but lethal-looking mace.", None, True, None, 0, "You swing the mace around clumsily.", None, None, None, False, 1)
hobgoblin = Enemy("HobGoblin", True, "A menacing hobgoblin stands before you.", "The lifeless body of a hobgoblin lies on the ground.", mace, 6, None)
room5.enemies = [hobgoblin]


bread = StatItem("Bread", "A loaf of fine Dwarfish Sabmel bread.", None, True, None, 0, "You eat the Sabmel bread. It's very refreshing. Gain 2HP", None, None, None, True, 2)


player_name = input("What is your name, brave adventurer? ")
print("Greetings", player_name + "!")

player = Player(player_name, room5, [], 10, [bread], None)

def checkhp():
    if player.hp > 10:
        player.hp = 10
    elif player.hp <= 0:
        print("You have been killed! Game Over.")
        exit(0)

def listroomitems():
    current_room = player.currentroom
    if current_room.items:
        print("You see the following items:")
        for item in current_room.items:
            print("- " + item.name)
    else:
        print("There are no items in this area.")

def trytotake(item):
    current_room = player.currentroom

    for room_item in current_room.items:

        if room_item.name.lower() == item.lower():
            if isinstance(room_item, StatItem):
                player.hp += room_item.hp_change
                print(room_item.usedesc)
                return

            if isinstance(room_item, Weapon):
                print("You have taken the", room_item.name + ".")
                player.weapon = room_item
                current_room.items.remove(room_item)
                return

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
    print(player.name)
    print("HP:",player.hp)

    if player.weapon != None:
        print("Current weapon: ", player.weapon.name)
    else:
        print("Current weapon: None")


    print("You are carrying:")
    if not player.inventory:
        print("Nothing.")
    else:
        for item in player.inventory:
            print(item.name)


def listenemies():
    current_room = player.currentroom

    for enemy in current_room.enemies:
        if enemy.alive:
            print(enemy.description)
        else:
            print(enemy.deaddesc)


def lookat(item):
    for room_item in player.currentroom.items:
        if room_item.name.lower() == item.lower():
            print(room_item.itemdesc)
            if room_item.revealsitem is not None:
                player.currentroom.items.append(room_item.revealsitem)
                print("You also see", room_item.revealsitem.name + ".")
            return

    for enemy in player.currentroom.enemies:
        if enemy.alive:
            print(enemy.description)
            return
        else:
            print(enemy.deaddesc)
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
            if inventory_item.usedin == current_room.number or inventory_item.usedin == 0:
                if isinstance(inventory_item, StatItem):
                    player.hp += inventory_item.hp_change
                if inventory_item.removesroomitem is not None:
                    current_room.items.remove(inventory_item.removesroomitem)
                if inventory_item.addsroomitem is not None:
                    current_room.items.append(inventory_item.addsroomitem)
                print(inventory_item.usedesc)
                inventory_item.usedin = 9999
                if inventory_item.useroomdesc != None:
                    current_room.description = inventory_item.useroomdesc
                if inventory_item.disposable == True:
                    player.inventory.remove(inventory_item)
                return
            else:
                print("You can't use the", inventory_item.name, "here.")
                return

    print("You don't have the", item + ".")


while True:
    checkhp()
    print(player.currentroom.name)
    print(player.currentroom.description)
    listroomitems()
    listenemies()

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