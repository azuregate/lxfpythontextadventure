# Import the necessary library for colored text (e.g., colorama)
from colorama import Fore, Style
import time
import progressbar2 as progressbar
import pygame

pygame.init()

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
necklace = StatItem("Necklace", "A necklace made from yellowed bones.", None, True, None, 0, "You feel a sudden pain as you try to wear the bone necklace. Lose 3 HP.", None, None, None, True, -3)
nugget = Item("Nugget", "A shiny gold nugget.", None, True, None, 0, None, None, None, None, False)
hobgoblin = Enemy("HobGoblin", True, "A menacing hobgoblin stands before you.", "The lifeless body of a hobgoblin lies on the ground.", mace, 6, [necklace,nugget])
room5.enemies = [hobgoblin]


bread = StatItem("Bread", "A loaf of fine Dwarfish Sabmel bread.", None, True, None, 0, "You eat the Sabmel bread. It's very refreshing. Gain 2HP.", None, None, None, True, 2)


player_name = input("What is your name, brave adventurer? ")
print("Greetings", player_name + "!")

player = Player(player_name, room5, [], 10, [bread], None)

def play_sword_clang():
    sound_file_path = "/home/nate/mu_code/sword.wav"
    sword_sound = pygame.mixer.Sound(sound_file_path)
    sword_sound.play()

def play_mace_clang():
    sound_file_path = "/home/nate/mu_code/mace.wav"
    sword_sound = pygame.mixer.Sound(sound_file_path)
    sword_sound.play()
    return

def showhpbar():
  # Calculate the percentage of hit points
    progress = player.hp / 10.0 * 100

        # Determine the color based on HP value
    if player.hp >= 7:
        hp_color = Fore.GREEN
    elif 4 <= player.hp <= 6:
        hp_color = Fore.YELLOW
    else:
        hp_color = Fore.RED

    # Create the progress bar string manually
    bar_length = 20
    filled_length = int(bar_length * progress // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    # Print the progress bar with the appropriate color
    print(hp_color + f"HP: [{bar}] {player.hp}/10 HP")
    return

def typewriter_effect(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fight(enemy_name):
    current_room = player.currentroom
    enemy = None

    if player.weapon is None:
        print("You can't fight without a weapon!")
        return

    for room_enemy in current_room.enemies:
        if room_enemy.name.lower() == enemy_name.lower():
            enemy = room_enemy
            break

    if enemy and enemy.alive:
        typewriter_effect(f"\033[31mA battle begins with the {enemy.name}!\033[0m")

        while enemy.alive and player.hp > 0:
            # Player's turn
            player_damage = player.weapon.damage
            enemy.hp -= player_damage
            play_sword_clang()
            typewriter_effect(f"\033[32mYou hit the {enemy.name} with your {player.weapon.name}. It causes {player_damage} damage.\033[0m")


            # Check enemy's HP
            if enemy.hp <= 0:
                enemy.alive = False
                typewriter_effect(f"\033[31mThe {enemy.name} has been defeated!\033[0m")
                lootbody(enemy)
                break

            # Enemy's turn
            enemy_damage = enemy.weapon.damage
            player.hp -= enemy_damage
            play_mace_clang()
            typewriter_effect(f"\033[31mThe {enemy.name} hits you with its {enemy.weapon.name}. It causes {enemy_damage} damage.\033[0m")
            showhpbar()

            # Check player's HP
            checkhp()

        if player.hp <= 0:
            typewriter_effect("\033[31mYou have been defeated! Game Over.\033[0m")
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
    # Print player information in a separate colored section
    print(Fore.YELLOW + "+-------------------------+")
    print("|", f" {player.name}'s Inventory ", "|")
    print("| HP:", player.hp, " " * (20 - len(str(player.hp))), "|")
    print("+-------------------------+")
    print(Style.RESET_ALL)

    # Print the inventory items in a separate colored section
    if player.inventory:
        print(Fore.CYAN + "You are carrying:")
        for item in player.inventory:
            print(f"- {item.name}")
        print(Style.RESET_ALL)
    else:
        print(Fore.CYAN + "Your inventory is empty.")
        print(Style.RESET_ALL)


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
                    showhpbar()
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
    # Print room name in bold and a different color
    print(Fore.CYAN + Style.BRIGHT + player.currentroom.name + Style.RESET_ALL)
    # Print room description in a different color and default style
    print(Fore.WHITE + player.currentroom.description)
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
    elif action_input.lower().startswith("fight "):
        enemy_name = action_input[6:]
        fight(enemy_name)
    else:
        print("You can't do that.")
