from enum import Enum

class SkillType(Enum):
    ATTACK = 1
    HEAL = 2
    UTILITY = 3

class skill():
    def __init__(self, name, physical, power, cooldown):
        self.name = name
        self.physical = physical
        self.power = power
        self.current_cooldown = 0
        self.cooldown = cooldown
    
    def start_cooldown(self):
        self.current_cooldown = self.cooldown
    
    def reduce_cooldown(self, user_monster=None):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
    
    def is_available(self, user_name=None):
        # If user_name is provided, print a message about the skill being used or on cooldown
        if self.current_cooldown > 0:
            if user_name:
                print(f"{self.name} is on cooldown for {self.current_cooldown} more turns.")
            return False
        if user_name:
            print(f"{user_name} uses {self.name}!")
        return True
    
    def use(self, user=None, target=None):
        self.start_cooldown()

        match self.SkillType.name:
            case "ATTACK":
                # Calculate damage if the skill is an attack
                damage = self.get_damage(target)

            case "HEAL":
                # The healing amount of a move is its power
                return self.power
            
            case "UTILITY":
                # Apply the utiliy move's unique effect
                self.use_utility(user, target)
                return 0
        return damage

    def get_damage(self, target):
        if self.physical:
            damage = self.power - target.durability
        else:
            damage = self.power - target.spirit
        return damage

    def use_utility(self, user, target=None):
        # Placeholder for utility skill effects 
        return 0
        
        
###### Attack skills ######
class Tackle(skill):
    def __init__(self):
        super().__init__(name="Tackle", physical=True, power=5, cooldown=0)
        self.SkillType = SkillType.ATTACK

class FireBreath(skill):
    def __init__(self):
        super().__init__(name="Fire Breath", physical=False, power=10, cooldown=3)
        self.SkillType = SkillType.ATTACK

class ClawSwipe(skill):
    def __init__(self):
        super().__init__(name="Claw Swipe", physical=True, power=6, cooldown=2)
        self.SkillType = SkillType.ATTACK

class TailWhip(skill):
    def __init__(self):
        super().__init__(name="Tail Whip", physical=True, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK

class MagicBolt(skill):
    def __init__(self):
        super().__init__(name="Magic Bolt", physical=False, power=7, cooldown=2)
        self.SkillType = SkillType.ATTACK

class Slam(skill):
    def __init__(self):
        super().__init__(name="Slam", physical=True, power=8, cooldown=3)
        self.SkillType = SkillType.ATTACK

class Splat(skill):
    def __init__(self):
        super().__init__(name="Splat", physical=True, power=4, cooldown=0)
        self.SkillType = SkillType.ATTACK

###### Heal skills ######
class Heal(skill):
    def __init__(self):
        super().__init__(name="Heal", physical=False, power=5, cooldown=3)
        self.SkillType = SkillType.HEAL

###### Utility skills ######
class Overdrive(skill):
    def __init__(self):
        super().__init__(name="Overdrive", physical=False, power=0, cooldown=5)
        self.SkillType = SkillType.UTILITY
        self.duration = 3

    def use_utility(self, user, target):
        print(f"{user.name} is in Overdrive! Speed and power increased for 3 turns!")
        
        user.speed += 3
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power += 3
    
    def end_utility(self, user):
        print(f"{user.name}'s Overdrive has ended. Speed and power returned to normal.")

        user.speed -= 3
        for ability in user.abilities:
            if ability.SkillType == SkillType.ATTACK:
                ability.power -= 3
        
    def reduce_cooldown(self, user_monster):
        super().reduce_cooldown(user_monster)
        
        # The duration of a utility move's effect is tied to it's cooldown
        if self.current_cooldown == self.cooldown - self.duration:
            self.end_utility(user_monster)

class Barrier(skill):
    def __init__(self):
        super().__init__(name="Barrier", physical=False, power=0, cooldown=5)
        self.SkillType = SkillType.UTILITY
    
    def use_utility(self, user, target):
        print(f"{user.name} uses Barrier! Durability increased for 3 turns!")
        user.durability += 3
        user.spirit += 3
    
    def end_utility(self, user):
        print(f"{user.name}'s Barrier has ended. Durability returned to normal.")
        user.durability -= 3
        user.spirit -= 3
    
    def reduce_cooldown(self, user_monster):
        super().reduce_cooldown(user_monster)
        if self.current_cooldown == self.cooldown - 3:
            self.end_utility(user_monster)