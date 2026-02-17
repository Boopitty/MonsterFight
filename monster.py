from unittest import case
from skills import FireBreath, ClawSwipe, TailWhip, MagicBolt, Slam, Splat, Tackle, Heal, Overdrive, Barrier
import random

class Monster():

    def __init__(self, name, health, durability, spirit, speed):
        self.name = name
        self.base_health = health
        self.health = health

        self.base_durability = durability
        self.durability = durability

        self.base_spirit = spirit
        self.spirit = spirit

        self.base_speed = speed
        self.speed = speed

        self.alive = True
        self.abilities = []

    def attack(self, target):
        # Select an ability to use and call other functions to calculate damage
        print(f"{self.name} has the following abilities:")
        for i, ability in enumerate(self.abilities):
            print(f"  {i + 1}. {ability.name}")
        
        # Get user input for which ability to use
        while True:
            choice = input("Choose an ability to use (enter the number): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.abilities):
                # Get the ability and use it on the target
                ability = self.abilities[int(choice) - 1]
                if ability.is_available(self.name):
                    match ability.SkillType.name:
                        case "ATTACK":
                            damage = ability.use(user = self, target = target)
                            if damage >= 0:
                                target.take_damage(damage)
                        case "HEAL":
                            heal_amount = ability.use(user = self)
                            if heal_amount > 0:
                                self.heal(heal_amount)
                        case "UTILITY":
                            # Utility skills do not affect target health
                            ability.use(user = self, target = target)
                    break
                
            else:
                choice = input("Invalid input. Please enter a valid number: ")
    
    def random_attack(self, target):
        while True:
            ability = random.choice(self.abilities)
            if ability.is_available(self.name):
                match ability.SkillType.name:
                    case "ATTACK":
                        damage = ability.use(user = self, target = target)
                        if damage >= 0:
                            target.take_damage(damage)
                    case "HEAL":
                        heal_amount = ability.use(user = self)
                        if heal_amount > 0:
                            self.heal(heal_amount)
                    case "UTILITY":
                        # Utility skills do not affect target health
                        ability.use(user = self, target = target)
                break
    
    def get_ability(self, index):
        if 0 <= index < len(self.abilities):
            return self.abilities[index]
        return None
    
    def print_summary(self):
        print(f"\n{self.summary}\n")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

        print(f"{self.name} takes {damage} damage!")
        # Check if the monster is still alive after taking damage
        if self.alive:
            print(f"{self.name} has {self.health} hp remaining.")
        else:
            self.alive = False
            print(f"{self.name} has been defeated!")

    def full_revive(self):
        if not self.alive:
            self.health = self.base_health
            self.alive = True
            print(f"{self.name} has been fully revived with {self.health} hp!")
        else:
            print(f"{self.name} is already alive and cannot be revived.")

    def revive(self):
        if not self.alive:
            self.health = 1
            self.alive = True
            print(f"{self.name} has been revived with {self.health} hp!")
        else:
            print(f"{self.name} is already alive and cannot be revived.")

    def full_heal(self):
        if self.alive:
            if self.health == self.base_health:
                print(f"{self.name} is already at full health and cannot be healed.")
                return
            self.health = self.base_health
            print(f"{self.name} has been fully healed!")
        else:
            print(f"{self.name} cannot be healed because it is defeated.")

    def heal(self, amount):
        if self.alive:
            if self.health == self.base_health:
                print(f"{self.name} is already at full health and cannot be healed.")
                return
            self.health += amount
            amount_healed = amount
            if self.health > self.base_health:
                amount_healed = self.base_health - (self.health - amount)
                self.health = self.base_health
            print(f"{self.name} recovered {amount_healed} hp and now has {self.health} hp.")
        else:
            print(f"{self.name} cannot be healed because it is defeated.")
        
    def cooldown_abilities(self):
        for ability in self.abilities:
            ability.reduce_cooldown(self)

class Dragon(Monster):
    def __init__(self):
        super().__init__(name="Dragon", health=15, durability=4, spirit=15, speed=4)
        self.summary = "A powerful and durable monster, but not very fast."
        self.abilities = [Tackle(), FireBreath(), ClawSwipe(), TailWhip()]

class Golem(Monster):
    def __init__(self):
        super().__init__(name="Golem", health=20, durability=4, spirit=10, speed=3)
        self.summary = "A very durable monster, but not very fast."
        self.abilities = [Tackle(), Slam(), Barrier()]

class Unicorn(Monster):
    def __init__(self):
        super().__init__(name="Unicorn", health=15, durability=5, spirit=10, speed=8)
        self.summary = "A fast and agile monster with moderate durability. Has a special ability to heal itself."
        self.abilities = [Tackle(), Slam(), TailWhip(), Heal()]

class Automaton(Monster):
    def __init__(self):
        super().__init__(name="Automaton", health=13, durability=5, spirit=5, speed=6)
        self.summary = "A balanced monster with moderate stats in all areas. Can temporarily overcharge itself."
        self.abilities = [Tackle(), MagicBolt(), Overdrive()]

class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime", health=35, durability=1, spirit=1, speed=1)
        self.summary = "Low offence, durability and speed. However, it can regenerate its already massive health pool."
        self.abilities = [Splat(), Heal()]

class Phoenix(Monster):
    def __init__(self):
        super().__init__(name="Phoenix", health=10, durability=2, spirit=7, speed=10)
        self.summary = "A very fast monster with low health and durability. Can resurrect itself once per battle."
        self.abilities = [Tackle(), ClawSwipe(), FireBreath()]