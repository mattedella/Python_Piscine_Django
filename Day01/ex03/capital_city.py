import sys

def find_capital(state):

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

	for key in states:
		if key == state:
			state_found = states[key]
			for key in capital_cities:
				if key == state_found:
					return capital_cities[key]
	return "Unknown state"

if __name__ == "__main__":
	if len(sys.argv) == 2:
		state = sys.argv[1]
		capital = find_capital(state)
		print(capital)
