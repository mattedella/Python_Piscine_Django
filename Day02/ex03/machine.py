import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	class BrokenMachineException(Exception):
		def __init__(self, message="This coffee machine has to be repaired."):
			self.message = message
			super().__init__(self.message)
	
	class EmptyCup(HotBeverage):
		def __init__(self):
			super().__init__(name="empty cup", price=0.90)
		def description(self):
			return "An empty cup?! Gimme my money back!"

	def __init__(self, broken=False):
		self.broken = broken
		self.served_drink = 0
	
	def repair(self):
		self.served_drink = 0
		self.broken = False

	def serve(self, beverage):

		if self.broken == True:
			raise self.BrokenMachineException()
		
		self.served_drink += 1
		if self.served_drink > 10:
			self.broken = True
			raise self.BrokenMachineException()
		
		
		if random.choice([True, False]):
			return self.EmptyCup()
		else:
			return beverage


# if __name__ == "__main__":
# 	coffee_machine = CoffeeMachine()
# 	for i in range(12):
# 		try:
# 			print(coffee_machine.serve(Coffee()))
# 		except Exception as e:
# 			print(e)
# 	coffee_machine.repair()
# 	print(coffee_machine.serve(Tea()))