class Enemy:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return f"{self.name} attacks with power {self.attack_power}!"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        else:
            return f"{self.name} takes {damage} damage and has {self.health} health left."
    
    def get_type_of_enemy(self):
        return "Generic Enemy"
    
    def talk(self):
        return f"{self.name} is a enemy."
    
    def walk_forward(self):
        return f"{self.name} walks forward."