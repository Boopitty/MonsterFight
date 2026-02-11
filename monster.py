class Monster():

    def __init__(self, name, health, defense, spirit, speed):
        self.name = name
        self.health = health
        self.defense = defense
        self.spirit = spirit
        self.speed = speed
        self.alive = True

    # Placeholder for future move implementation
    def moves(self):
        # This function will eventually return a list of moves the monster can perform
        return
    
    def attack_monster(self, other):
        # Damage calculation can be more complex, but for now it's just the attack stat
        damage = self.attack - other.defense
        if damage < 0:
            damage = 0
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

class Dragon(Monster):
    def __init__(self):
        super().__init__(name="Dragon", health=150, defense=20, spirit=15, speed=25)

class Golem(Monster):
    def __init__(self):
        super().__init__(name="Golem", health=200, defense=40, spirit=10, speed=15)

class Unicorn(Monster):
    def __init__(self):
        super().__init__(name="Unicorn", health=120, defense=15, spirit=30, speed=35)

class Automaton(Monster):
    def __init__(self):
        super().__init__(name="Automaton", health=130, defense=25, spirit=20, speed=30)

class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime", health=80, defense=10, spirit=5, speed=20)

class Phoenix(Monster):
    def __init__(self):
        super().__init__(name="Phoenix", health=110, defense=20, spirit=25, speed=40)