from Weapon import *

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon : Weapon = None

    def equip_weapon(self):
        
        self.attack_damage += self.weapon.attack_increase
        if not self.is_weapon_equipped:
            self.is_weapon_equipped = True
            return "Weapon equipped."
        else:
            return "Weapon is already equipped."
        
        