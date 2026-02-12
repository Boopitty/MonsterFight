from skills import FireBreath, ClawSwipe, TailWhip

class Monster():

    def __init__(self, name, health, durability, spirit, speed):
        self.name = name
        self.health = health
        self.durability = durability
        self.spirit = spirit
        self.speed = speed
        self.alive = True
        self.abilities = []

    def attack(self, target):
        # Select an ability to use and call other functions to calculate damage
        print(f"{self.name} is attacking {target.name}!")
        print(f"{self.name} has the following abilities:")
        for i, ability in enumerate(self.abilities):
            print(f"  {i + 1}. {ability.name}")
        
        choice = input("Choose an ability to use (enter the number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.abilities):
            ability = self.abilities[int(choice) - 1]
            print(f"{self.name} uses {ability.name}!")
            self.deal_damage(ability, target)
        else:
            print("Invalid choice. No ability used.")
        return
    
    def get_ability(self, index):
        if 0 <= index < len(self.abilities):
            return self.abilities[index]
        return None
    
    def deal_damage(self, ability, target):
        # Damage calculation can be more complex, but for now it's just the attack stat
        damage = ability.power - target.durability
        if damage < 0:
            damage = 0
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
        # Check if the monster is still alive after taking damage
        if self.is_alive():
            print(f"{self.name} has {self.health} health remaining.")
        else:
            self.alive = False
            print(f"{self.name} has been defeated!")

    def is_alive(self):
        return self.health > 0

class Dragon(Monster):
    def __init__(self):
        super().__init__(name="Dragon", health=15, durability=4, spirit=15, speed=4)
        self.summary = "A powerful and durable monster, but not very fast."
        self.abilities = [FireBreath(), ClawSwipe(), TailWhip()]

class Golem(Monster):
    def __init__(self):
        super().__init__(name="Golem", health=20, durability=4, spirit=10, speed=3)
        self.summary = "A very durable monster, but not very fast."
        self.abilities = [ClawSwipe(), TailWhip()]

class Unicorn(Monster):
    def __init__(self):
        super().__init__(name="Unicorn", health=15, durability=5, spirit=10, speed=8)
        self.summary = "A fast and agile monster with moderate durability. Has a special ability to heal itself."
        self.abilities = [ClawSwipe(), TailWhip()]

class Automaton(Monster):
    def __init__(self):
        super().__init__(name="Automaton", health=13, durability=5, spirit=5, speed=6)
        self.summary = "A balanced monster with moderate stats in all areas. Can temporarily overcharge itself."
        self.abilities = [ClawSwipe(), TailWhip()]

class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime", health=35, durability=1, spirit=1, speed=1)
        self.summary = "Low offence, durability and speed. However, it can regenerate its already massive health pool."
        self.abilities = [ClawSwipe(), TailWhip()]

class Phoenix(Monster):
    def __init__(self):
        super().__init__(name="Phoenix", health=10, durability=2, spirit=7, speed=10)
        self.summary = "A very fast monster with low health and durability. Can resurrect itself once per battle."
        self.abilities = [ClawSwipe(), TailWhip()]