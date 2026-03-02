def numbers():
	file = open("numbers.txt", "r")
	lines = file.read().split(',')
	print(lines)
	for i in range(len(lines)):
		print(lines[i])
	file.close()

if __name__ == "__main__":
	numbers()