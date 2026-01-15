from Enemy import *

class Ogre(Enemy):

    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)    

    def talk(self):
        return f"{self.name} is an ogre and slam hands all around!"