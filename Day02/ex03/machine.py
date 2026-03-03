import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class BrokenMachineException(Exception):
	def __init__(self, message="This coffee machine has to be repaired."):
		self.message = message
		super().__init__(self.message)


class CoffeMachine:
	def __init__(self, broken=False):
		self.broken = broken
		self.served_drink = 0
	
	def repair(self):
		self.broken = False

	def serve(self, beverage):

		to_serve = HotBeverage()
		if isinstance(beverage, Coffee):
			to_serve = Coffee()
		elif isinstance(beverage, Tea):
			to_serve = Tea()
		elif isinstance(beverage, Chocolate):
			to_serve = Chocolate()
		elif isinstance(beverage, Cappuccino):
			to_serve = Cappuccino()
		
		self.served_drink += 1
		if self.served_drink > 10:
			self.served_drink = 0
			self.broken = True
		
		if self.broken == True:
			raise BrokenMachineException()
		
		if random.randint(0, 5) == 0:
			return EmptyCup()
		
		return to_serve


class EmptyCup(HotBeverage):
	def __init__(self):
			super().__init__(name="empty cup", price=0.90)
	
	def description(self):
		return "An empty cup?! Gimme my money back!"

	

if __name__ == "__main__":
	machine = CoffeMachine()
	try:
		for _ in range(3):
			print(machine.serve(Coffee()))
		for _ in range(3):
			print(machine.serve(Tea()))
		for _ in range(3):
			print(machine.serve(Chocolate()))
		for _ in range(3):
			print(machine.serve(Cappuccino()))
	except BrokenMachineException as e:
		print(e)
	
	machine.repair()
	
	try:
		for _ in range(3):
			print(machine.serve(Coffee()))
		for _ in range(3):
			print(machine.serve(Tea()))
		for _ in range(3):
			print(machine.serve(Chocolate()))
		for _ in range(3):
			print(machine.serve(Cappuccino()))
	except BrokenMachineException as e:
		print(e)