
# Soldier
class Soldier:
	def __init__(self, strength,health,attack):
		self.health = health
		self.strength = strength
		self.attack = attack

	def attack(self):
		return self.strength

	def receiveDamage(self,health,attack):
		if self.health == health:
			return True


		
		

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
    
    def __init__(self,saxonArmy,vikingArmy):
    	self.saxonArmy = saxonArmy
    	self.vikingArmy = vikingArmy
    	

    

