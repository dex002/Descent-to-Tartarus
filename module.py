"""Code for my project."""
import random
import time

def intro():
    """starts the game with a cinematic intro""" 
    print("The breeze of the River Styx sends a chill down your spine...")
    time.sleep(1.5)
    print("You look far across the land but see nothing but darkness...")
    time.sleep(1.5)
    print("You look into the River Styx catching a glimpse of your reflection...")
    time.sleep(1.5)
    print("Who do you see...?\n")

def calculate_damage(attacker, target, multiplier=1):
    """Calculate damage dealt from attacker to target after defense reduction.

    Parameters
    ----------
    attacker : object
        The character dealing damage.
    target : object
        The character recieving damage.
    multiplier : int or float
        Damage multiplier for certain skills, default value of 1.

    Returns
    -------
    damage : int or float
        The final damage after multipliers and damage reduction from defense, a minimum value of 0.
    """
    
    damage = (attacker.damage * multiplier) - target.defense
    if damage < 0:
        damage = 0
        
    return damage


class Aphros():
    """A healer class hero based on Aphrodite."""
    
    def __init__(self, name):
        self.name = name
        self.damage = 3
        self.hp = 10
        self.speed = 3
        self.defense = 0
        self.max_hp = 15
        self.skills = ["Alluring Kiss", "Heartbreak", "Hyperfixation"]

    def alluring_kiss(self, target):
        """Heals the target."""
        
        target.hp += 2
        if target.hp > target.max_hp:
            target.hp = target.max_hp 
        print(self.name + " used Alluring Kiss!")
        print(target.name + " healed 2 HP!")
    
    def heartbreak(self, target):
        """Deals damage to the target."""
        
        true_damage = calculate_damage(self, target)
        target.hp -= true_damage
        print(self.name + " used heartbreak!")
        print(target.name + " takes " + str(true_damage) + " damage")

    def hyperfixation(self, target):
        """Reduces the target's damage."""
        
        target.damage -= 1
        print(self.name + " used hyperfixation!")
        print(target.name + " reduced " + target.name +"'s attack by 1")
        

class Aspirda():
    """A tank class hero based on Hephaestus."""
    
    def __init__(self, name):
        self.name = name
        self.damage = 4
        self.hp = 15
        self.speed = 1
        self.defense = 2
        self.max_hp = 20
        self.skills = ["Bulwark", "Defender", "Bloodhound"]

    def bulwark(self):
        """Increases own defense."""
        
        if self.defense < 10: 
            self.defense += 3
            print(self.name + " used Bulwark!")
            print(self.name + "'s defense increased by 3!")
        else:
            print(self.name + " used Bulwark!")
            print(self.name + "'s defense is already maxed!")

    def defender(self, target):
        """Increases target's defense."""
        
        if self.defense < 10:
            target.defense += 2 
            print(self.name + " used Defender!")
            print(target.name + " gained 2 defense!")
        else:
            print(self.name + " used Defender!")
            print(target.name + "'s defense is already maxed!")            

    def bloodhound(self, target):
        """Reduces target's speed."""
        
        target.speed -= 2
        print(self.name + " used Bloodhound!")
        print(target.name + "'s speed reduced by 2!")
        

class Doros():
    """An assassin class hero based on Ares."""
    
    def __init__(self, name):
        self.name = name
        self.damage = 3
        self.hp = 8
        self.speed = 5
        self.defense = 0
        self.max_hp = 15
        self.skills = ["Deathbound", "Sly", "Dominance"]

    def deathbound(self, target):
        """Deals great damage to the target."""
        
        true_damage = calculate_damage(self, target, 3)
        target.hp -= true_damage
        print(self.name + " used Deathbound!")
        print(target.name + " takes " + str(true_damage) + " damage!")

    def sly(self, target):
        """Deals damage to a target and heals for that much."""
        
        true_damage = calculate_damage(self, target)
        target.hp -= true_damage
        self.hp += true_damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(self.name + " used Sly!")
        print(self.name + " stole " + str(true_damage) + " HP from " + target.name + "!")

    def dominance(self, target):
        """Deals small damage to target and inreases own defense."""
        
        target.hp -= (self.damage - 2)
        if self.defense < 10:
            self.defense += 2
        print(self.name + " used Dominance!")
        print(self.name + " deals " + str((self.damage - 2)) + " damage and gains 2 defense!")

    
class Lusios():
    """A madman class hero based on Dionysus."""
    
    def __init__(self, name):
        self.name = name
        self.damage = 4
        self.hp = 12
        self.speed = 1
        self.defense = 1
        self.hysteria_stacks = 1
        self.max_hp = 18
        self.skills = ["Sobering Realization", "Hysteria", "No Mither"]

    def sobering_realization(self, target):
        """Deals scaling damage based on the number of hysteria stacks."""
        
        true_damage = calculate_damage(self, target, self.hysteria_stacks)
        target.hp -= true_damage
        print(self.name + " used Sobering Realization!")
        print(self.name + " has " + str(self.hysteria_stacks) + " stacks of Hysteria!")
        print(target.name + " takes " + str(true_damage) + " damage!")
        self.hysteria_stacks = 1 
        print(self.name + "'s Hysteria reset to 1!")
        
    def hysteria(self):
        """Increases own hysteria stacks by 1."""
        
        self.hysteria_stacks += 1
        print(self.name + " used Hysteria!")
        print(self.name + " now has " + str(self.hysteria_stacks) + " stacks of Hysteria!")

    def no_mither(self, target):
        """Deals random damage to target or to himself"""
        
        roll = random.randint(1, 4)
        if roll == 1:
            target.hp -= 0
            print(self.name + " used No Mither!")
            print(target.name + " takes 0 damage!")
        if roll == 2:
            target.hp -= 4
            print(self.name + " used No Mither!")
            print(target.name + " takes 5 damage!")
        if roll == 3:
            target.hp -= 8
            print(self.name + " used No Mither!")
            print(target.name + " takes 10 damage!")
        if roll == 4:
            self.hp -= 2
            print(self.name + " used No Mither!")
            print(self.name + " takes 2 damage!")


class Enemy():
    """An enemy combatant encountered in the dungeon."""
    
    def __init__(self, name, damage, hp, speed, defense):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.speed = speed
        self.defense = defense

def random_enemy():
    """Selects a random enemy from a list of predetermined enemies."""
    
    enemies = [Enemy("Skeleton", 2, 10, 2, 0),
               Enemy("Goblin", 2, 8, 4, 0),
               Enemy("Cultist", 3, 8, 2, 0),
               Enemy("Stone Golem", 1, 15, 1, 2),
               Enemy("Harpy", 3, 8, 5, 0),
               Enemy("Satyr", 2, 10, 3, 1),
               Enemy("Shade", 2, 9, 4, 0),
               Enemy("Cyclops", 3, 12, 1, 1)]
    return random.choice(enemies)
    

def boss_enemy():
    """Selects a random boss from a list of predetermined bosses."""
    
    bosses = [Enemy("Hades", 4, 20, 2, 3),
              Enemy("Chronos", 6, 14, 5, 1),
              Enemy("The Sphinx", 3, 18, 2, 5),
              Enemy("Koalemos", 2, 12, 1, 1),
              Enemy("The Siren", 5, 13, 5, 1),
              Enemy("Crystal Hydra", 3, 20, 2, 3),
              Enemy("Bone Hydra", 5, 15, 3, 1),
              Enemy("Obsidian Hydra", 4, 18, 2, 3),
              Enemy("The Minotaur", 6, 16, 2, 2),
              Enemy("The Chimaera", 5, 14, 4, 1),
              Enemy("Medusa", 3, 16, 3, 2),
              Enemy("Typhon", 100, 100, 100, 100)]
    return random.choice(bosses)


def pick_classes():
    """Prompts the player to pick two classes for the party."""
    
    party = []
    
    print("——— Who do you see? ———")
    print("1. Aphros —— The Healer —— Excels in " + \
          "sustaining the team and lowering the enemy's attack.")
    print("2. Aspirda —— The Tank —— Fortifies the team by " + \
          "increasing defense while slowing the enemy.")
    print("3. Doros —— The Assassin —— High self-sustain " + \
          "with massive damage, lifesteal, and growing defense.")
    print("4. Lusios —— The Madman —— Excels in longer battles with " + \
          "chance-based skills and ramping damage.")
    choice1 = input("Pick your first hero (1-4): ")
    time.sleep(1)
    print("You look at the reflection next to you, who do you see?")
    time.sleep(1)
    choice2 = input("Pick your second hero (1-4): ")

    if choice1 == choice2:
        print("\nThe gods do not smile upon your egocentrism.\n")
        time.sleep(2)
        return pick_classes()

    for choice in [choice1, choice2]:
        if choice == "1":
            time.sleep(0.5)
            name = input("Enter a name for the Aphros: ")
            party.append(Aphros(name))
        elif choice == "2":
            time.sleep(0.5)
            name = input("Enter a name for the Aspirda: ")
            party.append(Aspirda(name))
        elif choice == "3":
            time.sleep(0.5)
            name = input("Enter a name for the Doros: ")
            party.append(Doros(name))
        elif choice == "4":
            time.sleep(0.5)
            name = input("Enter a name for the Lusios: ")
            party.append(Lusios(name))
        else:
            time.sleep(0.5)
            print("\nThe River Styx does not recognize that soul.\n")
            return pick_classes()

    print("Your party:")
    for hero in party:
        print("- " + hero.name + " the " + hero.__class__.__name__)
    return party


def pick_skill(hero, party, enemies):
    """Displays the skills a hero can use and lets player pick one to use.

    Parameters
    ----------
    hero : object
        the hero whose turn it is.
    party : list
        the list of the all heros in the party.
    enemies : list
        the list of all the enemies in combat.

    Returns
    -------
    none
    """
    
    print("\n" + hero.name + "'s turn!")
    print("Skills:")
    if isinstance(hero, Aphros):
        print("1. " + hero.skills[0] + " — Aphrodite's blessing. " + \
              "Restores a small amount of HP to either an ally or themselves.")
        print("2. " + hero.skills[1] + " — Even emotional wounds bleed. " + \
              "Deals small damage to target.")
        print("3. " + hero.skills[2] + " — Enamour the enemy. " + \
              "Slightly reduces enemy attack.")
    elif isinstance(hero, Aspirda):
        print("1. " + hero.skills[0] + " — Forge the body into iron. " + \
              "Greatly increases " + hero.name + "'s defense.")
        print("2. " + hero.skills[1] + " — A good offense needs a good defense. " + \
              "Slightly increases an ally's defense.")
        print("3. " + hero.skills[2] + " — Track the prey, slow the hunt. " + \
              "Slightly reduces enemy speed.")
    elif isinstance(hero, Doros):
        print("1. " + hero.skills[0] + " — 'I'm always one step ahead'. " + \
              "Deal massive damage to target.")
        print("2. " + hero.skills[1] + " — 'Survival of the fittest'. " + \
              "Deal damage and recover the same amount of damage dealt.")
        print("3. " + hero.skills[2] + " — 'I'm a one man army'." + \
              "Deal small damage and gain defense. ")
    elif isinstance(hero, Lusios):
        print("1. " + hero.skills[0] + " — Ignorance is bliss, knowledge is power. " + \
              "Deals extra damage based on hysteria stacks.")
        print("2. " + hero.skills[1] + " — 'More... more!'. " + \
              "a buff that increases Sobering Realization's damage per stack.")
        print("3. " + hero.skills[2] + " — 'Pfft, whatever'. " + \
              "May deal 0, 5, or 10 damage, or backfire for 2 self damage.")

    living_enemies = []
    for e in enemies:
        if e.hp > 0:
            living_enemies.append(e)
    living_allies = []
    for a in party:
        if a.hp > 0:
            living_allies.append(a)

    while True:
        choice = input("Pick a skill (1-3): ")
        if isinstance(hero, Aphros):
            if choice == "1":
                if len(living_allies) == 2:
                    print("Allies:")
                    print("1. " + living_allies[0].name + " HP: " + str(living_allies[0].hp))
                    print("2. " + living_allies[1].name + " HP: " + str(living_allies[1].hp))
                    while True:
                        ally_choice = input("Pick an ally: ")
                        if ally_choice == "1":
                            ally_target = living_allies[0]
                            break
                        elif ally_choice == "2":
                            ally_target = living_allies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    ally_target = living_allies[0]       
                hero.alluring_kiss(ally_target) 
                break
            elif choice == "2":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]       
                hero.heartbreak(enemy_target)  
                break
            elif choice == "3":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " Damage: " + str(living_enemies[0].damage))
                    print("2. " + living_enemies[1].name + " Damage: " + str(living_enemies[1].damage))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]                   
                hero.hyperfixation(enemy_target)  
                break
        elif isinstance(hero, Aspirda):
            if choice == "1":
                hero.bulwark() 
                break
            elif choice == "2":
                if len(living_allies) == 2:
                    print("Allies:")
                    print("1. " + living_allies[0].name + " HP: " + str(living_allies[0].hp))
                    print("2. " + living_allies[1].name + " HP: " + str(living_allies[1].hp))
                    while True:
                        ally_choice = input("Pick an ally: ")
                        if ally_choice == "1":
                            ally_target = living_allies[0]
                            break
                        elif ally_choice == "2":
                            ally_target = living_allies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    ally_target = living_allies[0]       
                hero.defender(ally_target)  
                break
            elif choice == "3":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " Speed: " + str(living_enemies[0].speed))
                    print("2. " + living_enemies[1].name + " Speed: " + str(living_enemies[1].speed))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]                 
                hero.bloodhound(enemy_target)
                break
        elif isinstance(hero, Doros):
            if choice == "1":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]              
                hero.deathbound(enemy_target)
                break
            elif choice == "2":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]  
                hero.sly(enemy_target)  
                break
            elif choice == "3":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]  
                hero.dominance(enemy_target)
                break
        elif isinstance(hero, Lusios):
            if choice == "1":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]  
                hero.sobering_realization(enemy_target)
                break
            elif choice == "2":
                hero.hysteria()
                break
            elif choice == "3":
                if len(living_enemies) == 2:
                    print("Enemies:")
                    print("1. " + living_enemies[0].name + " HP: " + str(living_enemies[0].hp))
                    print("2. " + living_enemies[1].name + " HP: " + str(living_enemies[1].hp))
                    while True:
                        enemy_choice = input("Pick an enemy: ")
                        if enemy_choice == "1":
                            enemy_target = living_enemies[0]
                            break
                        elif enemy_choice == "2":
                            enemy_target = living_enemies[1]
                            break
                        else:
                            print("that is not a valid target!")
                else:
                    enemy_target = living_enemies[0]  
                hero.no_mither(enemy_target)
                break    
        else:
            print("Invalid skill, pick 1, 2, or 3")

    
def combat(party, enemies):
    """Runs a full combat for the current floor.

    Parameters
    ----------
    party : list
        the list of the all heros in the party.
    enemies : list
        the list of all the enemies in combat.

    Returns
    -------
    result : bool
        True if the party wins, False if the party is defeated.
    """
    
    time.sleep(0.75)
    print("\n——— Dungeon Start———")
    time.sleep(0.75)
    while True:

        # rebuilds lists of enemies/heros to remove dead combatants
        new_enemies = []
        for e in enemies:
            if e.hp > 0:
                new_enemies.append(e)
        enemies = new_enemies

        alive_heroes = []
        for hero in party:
            if hero.hp > 0:
                alive_heroes.append(hero)
        party = alive_heroes
        
        print("\n——— STATS ———")
        for hero in party:
            print(hero.name + " HP: " + str(hero.hp) + ", Damage: " +
                  str(hero.damage) + ", Defense: " + str(hero.defense))
        for enemy in enemies:
            print(enemy.name + " HP: " + str(enemy.hp) + ", Damage: " +
                  str(enemy.damage) + ", Defense: " + str(enemy.defense))

        def get_initiative(order_tuple):
            return order_tuple[0]

        # dice roll + speed determines turn order so faster characters on average act first    
        combatants = party + enemies
        order = []
        for c in combatants:
            initiative = random.randint(1, 5) + c.speed
            order.append((initiative, c))
        order.sort(key=get_initiative, reverse=True)
        time.sleep(0.75)
        print("\n——— Turn Order ———")
        for initiative, character in order:
            print(character.name)
        time.sleep(0.75)

        for initiative, combatant in order:
            if combatant.hp <= 0:
                continue

            if combatant in party:
                pick_skill(combatant, party, enemies)
            else:
                alive_heroes = []
                for a in party:
                    if a.hp > 0:
                        alive_heroes.append(a)
                target = random.choice(alive_heroes)
                damage_dealt = calculate_damage(combatant, target)
                target.hp -= damage_dealt
                print("")
                time.sleep(0.75)
                print("Enemy turn: " + combatant.name + " attacks " +
                      target.name + " for " + str(damage_dealt) + " damage!")
                time.sleep(0.75)
                
            new_enemies = []
            for enemy in enemies:
                if enemy.hp > 0:
                    new_enemies.append(enemy)
            enemies = new_enemies
            
            if len(enemies) == 0:
                print("All enemies defeated!")
                return True
                        
            alive_heroes = []
            for hero in party:
                if hero.hp > 0:
                    alive_heroes.append(hero)
            party = alive_heroes
            
            if len(party) == 0:
                print("Your party has fallen!")
                return False

        
def dungeon(party):
    """Run the main dungeon loop advancing floors until you die.
    
       Each floor increases enemy attack and hp.
       Every 5th floor spawns a boss enemy instead of two regular enemies.

    Parameters
    ----------
    party : list
        the list of the all heros in the party.

    Returns
    -------
    none
    
    """
    floor = 1
    alive = True

    while alive:
        time.sleep(0.75)
        print("\n——— Floor " + str(floor) + " ———")
        time.sleep(0.75)

        # every 5th floor spawns a boss instead of two regular enemies
        if floor % 5 == 0:
            print("A boss approaches...")
            enemies = [boss_enemy()]
            for enemy in enemies:
                enemy.hp = int(enemy.hp * (1 + floor * 0.1))
                enemy.damage = int(enemy.damage * (1 + floor * 0.1))
            for enemy in enemies:
                if enemy.name == "Typhon":
                    print("You hear a loud roar, a roar you can never forget...")
                    time.sleep(0.75)
                    print("You know this is the end. You've made it to Tartarus, but at what cost?")
        else:
            enemies = [random_enemy(), random_enemy()]
            # enemy stats scale with floor number to maintain difficulty as player progresses
            for enemy in enemies:
                enemy.hp = int(enemy.hp * (1 + floor * 0.1))
                enemy.damage = int(enemy.damage * (1 + floor * 0.2))
            print("You encounter a " + enemies[0].name + " and a " + enemies[1].name + "!")

        won = combat(party, enemies)

        if won:
            print("You cleared floor " + str(floor) + "!")
            floor += 1
        else:
            print("Your party succumbs after fighting hard for " + str(floor) + " floors...")
            alive = False

def descend():
    """Start the game from the beginning."""
    intro()
    party = pick_classes()
    dungeon(party)