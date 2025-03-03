
# Soldier
import random

class Soldier:

    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strenght):
        self.name=name
        self.health=health
        self.strength=strenght
   
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"
    
            

# Saxon


class Saxon(Soldier):
    
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
            

# War


class War(Soldier): 

    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking) 

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon) 

    def vikingAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        Saxon.receiveDamage(Viking.strength)
        if Saxon.health <= 0:
            self.saxonArmy.remove(Saxon)
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {Viking.strength} points of damage"
    

    def saxonAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        Viking.receiveDamage(Saxon.strength)
        if Viking.health <= 0:
            self.vikingArmy.remove(Viking)
            return f"{Viking.name} has died in act of combat"
        else:
            return f"{Viking.name} has received {Saxon.strength} points of damage"
    
    def showStatus(self):
        if self.saxonArmy == []:
            return f"Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."
    

        


