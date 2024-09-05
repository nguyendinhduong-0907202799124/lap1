class Hero:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def defend(self,defends):
        self.defends=defends
        self.health = self.health - self.defends
        self.check()
    def heal(self,heals):
        self.heals=heals
        self.health = self.health + self.heals
        self.check()
    def check(self):
        if self.health <= 0:
            print('Duong was defend')
        else:
            print('None')
hero = Hero('Duong',100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
        
        