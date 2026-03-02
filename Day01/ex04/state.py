import sys

def find_state(capital_city):

	states =  {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for key, value in capital_cities.items():
		if value == capital_city:
			for key2, value2 in states.items():
				if value2 == key:
					return key2
	return "Unknown capital city"

if __name__ == "__main__":
	if len(sys.argv) == 2:
		capital_city = sys.argv[1]
		state = find_state(capital_city)
		print(state)