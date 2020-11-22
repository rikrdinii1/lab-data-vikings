
# Soldier
class Soldier:
	# Resuelto, sin errores
	def __init__(self, strength,health,attack):
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength

	def receiveDamage(self,damage):
		self.health=self.health-damage

# Viking
class Viking:
# Resuelto. Sin errores

	def __init__(self,name, health,strength):
		self.name = name
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength
		
	def receiveDamage(self,health):
		if self.health == health:
			return str(self.name + ' has died in act of combat')
		elif health - self.health:
			self.health = self.health - health
			return str(self.name +' has received '+str(health)+ ' points of damage')
	
	def battleCry(self):
		return str('Odin Owns You All!')	
		
# Saxon
class Saxon:
# Resuelto. Sin errores	
	def __init__(self,health,strength):
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength
		
	def receiveDamage(self,health):
		if self.health == health:
			return str('A Saxon has died in combat')
		elif health - self.health:
			self.health = self.health - health
			return str('A Saxon has received '+str(health)+' points of damage') 

# War
class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        import random
        randSax=random.choice(self.saxonArmy)
        randViking=random.choice(self.vikingArmy)
        message=randSax.receiveDamage(randViking.strength)
        if randSax.health<=0:
            self.saxonArmy.remove(randSax)
        return message
    
    def saxonAttack(self):
        import random
        randSax=random.choice(self.saxonArmy)
        randViking=random.choice(self.vikingArmy)
        message=randViking.receiveDamage(randSax.strength)
        if randViking.health<=0:
            self.vikingArmy.remove(randViking)
        return message
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return("Vikings have won the war of the century!")
        elif len(self.vikingArmy)==0:
            return("Saxons have fought for their lives and survive another day...")
        else: 
            return("Vikings and Saxons are still in the thick of battle.")
    

