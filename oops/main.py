from Enemy import *
from Zombie import *
from Ogre import *

def battle(e1:Enemy, e2:Enemy):
    
    while e1.health > 0 and e2.health > 0:
        print(e1.attack())
        print(e2.take_damage(e1.attack_power))
        if e2.health <= 0:
            break
        print(e2.attack())
        print(e1.take_damage(e2.attack_power))




if __name__ == "__main__":
    ogre = Ogre("Gorg", 100, 15)
    zombie = Zombie("Zed", 80, 10)

    print("Ogre Battle:")
    battle(ogre,zombie)
    
    print("\nZombie Battle:")
    battle(zombie,ogre)