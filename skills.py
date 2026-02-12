class skill():
    def __init__(self, name, physical, power, cooldown):
        self.name = name
        self.physical = physical
        self.power = power
        self.cooldown = cooldown

class FireBreath(skill):
    def __init__(self):
        super().__init__(name="Fire Breath", physical=False, power=10, cooldown=3)
    
class ClawSwipe(skill):
    def __init__(self):
        super().__init__(name="Claw Swipe", physical=True, power=5, cooldown=1)

class TailWhip(skill):
    def __init__(self):
        super().__init__(name="Tail Whip", physical=True, power=7, cooldown=2)