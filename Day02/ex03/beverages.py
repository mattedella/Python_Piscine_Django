class HotBeverage:
		def __init__(self, name="hot beverage", price=0.30):
				self.name = name
				self.price = price

		def description(self):
				return "Just some hot water in a cup."

		def __str__(self):
				return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description()}"

class Coffee(HotBeverage):
		def __init__(self, name="coffee", price=0.40):
				super().__init__(name, price)

		def description(self):
				return "A coffee, to stay awake."
		
class Tea(HotBeverage):
		def __init__(self, name="tea"):
				super().__init__(name)

class Chocolate(HotBeverage):
		def __init__(self, name="chocolate", price=0.50):
				super().__init__(name, price)

		def description(self):
				return "Chocolate, sweet chocolate..."

class Cappuccino(Coffee):
		def __init__(self, name="cappuccino", price=0.45):
				super().__init__(name, price)

		def description(self):
				return "Un po’ di Italia nella sua tazza!"
	

if __name__ == "__main__":
	hot_beverage = HotBeverage()
	print(hot_beverage)
	coffee = Coffee()
	print(coffee)
	tea = Tea()
	print(tea)
	chocolate = Chocolate()
	print(chocolate)
	cappuccino = Cappuccino()
	print(cappuccino)