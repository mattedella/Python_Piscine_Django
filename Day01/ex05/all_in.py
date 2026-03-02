import sys

def all_in(state):

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

	lower_state = state.lower()
	for key in states:
		if key.lower() == lower_state:
			state_found = states[key]
			for key2 in capital_cities:
				if key2 == state_found:
					return "{} is the capital of {}".format(capital_cities[key2], key)
				
	for key, value in capital_cities.items():
		if value == state:
			for key2, value2 in states.items():
				if value2 == key:
					return "{} is the capital of {}".format(value, key2)
	return "{} is neither a capital city nor a state".format(lower_state)
	

if __name__ == "__main__":
	if len(sys.argv) == 2:
		list = sys.argv[1].split(',')
		for item in list:
			item = item.strip()
			item = item.capitalize()
			if item == "":
				continue
			capital = all_in(item)
			print(capital)