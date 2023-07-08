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

class Key:
    def __init__(self, name, keydesc, keyusedesc, keyroomdesc, keyexits):
        self.name = name
        self.keydesc = keydesc
        self.keyusedesc = keyusedesc
        self.keyroomdesc = keyroomdesc
        self.keyexits = keyexits

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


# Define the rooms and items, adding a name and description. No exits are set until all the rooms are declared.

room1 = Room(1, "Main Chamber", "You're standing in a dark cavern. You hear the sound of dripping water.", [None, None, None, None], None, None, None)

lockedchest = Item("Chest", "A very sturdily built CHEST. It's securely locked.", None, False, None, None, None, None, None, None, False)
ruby = Item("Ruby", "A very large and valuable ruby.", None, True, None, None, None, None, None, None, False)
bread = Item("Bread", "A loaf of fine Dwarfish Sabmel bread..", None, True, None, 0, "You eat the Sabmel bread. It's very refreshing.", None, None, None, True)
brokenchest = Item("Broken Chest", "The BROKEN CHEST lies in splinters thanks to your efforts with the axe.", None, False, ruby, None, None, None, None, None, False)


room3 = Room(3, "South Chamber", "You see an old chest.", [None, None, None, None], None, None, None)
room3.items = [lockedchest]

armour = Item("Armour", "A battered set of dwarf plate mail armour. It's not your size but could come in useful.", None, True, None, None, None, None, None, None, False)
axe = Item("Axe", "The AXE is caked with dirt but you can see it's still razor sharp.",
"You see the skeleton of a dwarf.", True, None, 3, "You use the axe to smash open the chest.",lockedchest, brokenchest, "You see a BROKEN CHEST.", False)
skeleton = Item("Skeleton", "The dwarf's skeleton is still wearing a suit of ARMOUR. The bones are yellowed.", None, False, armour, None, None, None, None, None, False)

room2 = Room(2, "North Chamber", "You see the SKELETON of a dwarf holding an AXE.", [None, None, None, None], None, None, None)
room2.items = [axe, skeleton]


room1 = Room(1, "Main Chamber", "You're standing in a dark cavern. You hear the sound of dripping water.", [None, None, None, None], None, None, None)


room4 = Room(4, "East Chamber", "You see entrance to the cave where you arrived earlier. The gate is locked. It's stained red with rust.",[None,None,None,None], None, None, None)

grille = StatItem("Grille", "The iron grille is old and rusty but you seem some sharp edges.", None, False, None, None, "You grasp the grille and try to move it but only manage to scratch your hand. Lose 3 HP", None, None, None, False, -3)
sword = Weapon("Sword", "A sharp and sturdy sword.", None, True, None, 0, "You swing the sword around with great skill.", None, None, None, False, 2)
room5 = Room(5, "West Chamber", "You see an iron grille set into the wall. Someone has prised it open.",[None,None,None,None], None, None, None)
room5.items = [grille,sword]

mace = Weapon("Mace", "A stubby but lethal-looking mace.", None, True, None, 0, "You swing the mace around clumsily.", None, None, None, False, 1)
necklace = StatItem("Necklace", "A necklace made from yellowed bones.", None, True, None, 0, "You feel a sudden pain as you try to wear the bone necklace. Lose 3 HP.", None, None, None, True, -3)
nugget = Item("Nugget", "A shiny gold nugget.", None, True, None, 0, None, None, None, None, False)
hobgoblin = Enemy("HobGoblin", True, "A menacing hobgoblin stands before you.", "The lifeless body of a hobgoblin lies on the ground.", mace, 6, [necklace,nugget])
room5.enemies = [hobgoblin]

room6 = Room(6, "Cave Entrance", "You step out blinking into the sunlight.",[None,None,None,room4], None, None, None)

# Here the room exits are defined in a list in NSEW order.

room1.exits = [room2, room3, room4, room5]
room2.exits = [None, room1, None, None]
room3.exits = [room1, None, None, None]
room4.exits = [None,None,None,room1]
room5.exits = [None,None,room1,None]
room6.exits = [None,None,None,room4]

# Here we define the keys.

redkey = Key("Red Key", "An old key stained red with rust.", "You use the red key to unlock the gate.", "You see the entrance to the cave where you arrived earlier. The red gate lies open.", [None,None,room6,room1])
room4.key = redkey


bread = StatItem("Bread", "A loaf of fine Dwarfish Sabmel bread.", None, True, None, 0, "You eat the Sabmel bread. It's very refreshing. Gain 2HP.", None, None, None, True, 2)


player_name = input("What is your name, brave adventurer? ")
print("Greetings", player_name + "!")

player = Player(player_name, room1, [redkey], 10, [bread], None)

def trytomove(direction):
    current_room = player.currentroom
    exits = current_room.exits

    if direction in ['N', 'S', 'E', 'W']:
        direction_index = ['N', 'S', 'E', 'W'].index(direction)
        if exits[direction_index] is not None:
            new_room = exits[direction_index]
            player.currentroom = new_room
            return
    print("You can't go that way.")

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

def fight(enemy_name):
    current_room = player.currentroom
    enemy = None

    if player.weapon == None:
        print("You can't fight without a weapon!")
        return

    for room_enemy in current_room.enemies:
        if room_enemy.name.lower() == enemy_name.lower():
            enemy = room_enemy
            break

    if enemy and enemy.alive:
        print(f"A battle begins with the {enemy.name}!")

        while enemy.alive and player.hp > 0:
            # Player's turn
            player_damage = player.weapon.damage
            enemy.hp -= player_damage
            print(f"You hit the {enemy.name} with your {player.weapon.name}. It causes {player_damage} damage.")

            # Check enemy's HP
            if enemy.hp <= 0:
                enemy.alive = False
                print(f"The {enemy.name} has been defeated!")
                lootbody(enemy)
                break

            # Enemy's turn
            enemy_damage = enemy.weapon.damage
            player.hp -= enemy_damage
            print(f"The {enemy.name} hits you with its {enemy.weapon.name}. It causes {enemy_damage} damage.")

            # Check player's HP
            checkhp()

        if player.hp <= 0:
            print("You have been defeated! Game Over.")
            exit(0)
    else:
        print("There is no such enemy here.")


def lootbody(enemy):
    current_room = player.currentroom

    print(f"You defeated the {enemy.name} in combat!")
    print(f"You find the following items on the {enemy.name}'s body:")

    if enemy.weapon != None:
        current_room.items.append(enemy.weapon)
        print(f"- {enemy.weapon.name}")

    if enemy.loot is not None:
        for item in enemy.loot:
            current_room.items.append(item)
            print(f"- {item.name}")

    # Remove the enemy from the room
    current_room.enemies.remove(enemy)


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

    if current_room.enemies == None:
        print("There are no enemies here.")
        return

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
    checkkeys()
    listroomitems()
    listenemies()
    listexits()

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
    elif action_input.lower().startswith("fight "):
        enemy_name = action_input[6:]
        fight(enemy_name)
    elif action_input.upper() in ['N', 'S', 'E', 'W']:
        trytomove(action_input.upper())
    else:
        print("You can't do that.")