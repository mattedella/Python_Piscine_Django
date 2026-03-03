import sys, os, re

def render(file_name):

	if not os.path.isfile(file_name):
		return "File not found"
	settings_file = os.path.join(os.path.dirname(__file__), 'settings.py')

	if not os.path.isfile(settings_file):
		return "Settings file not found"
	replace = open(settings_file, 'r').read()
	words = {}

	for line in replace.splitlines():
		parts = line.split('=')
		if len(parts) != 2:
			continue
		key = parts[0].strip()
		value = parts[1].strip().strip('"').strip("'")
		words[key] = value

	with open(file_name, 'r') as file:
		content = file.read()
		for key, value in words.items():
			content = content.replace('{' + key + '}', value)

	with open('render.html', 'w') as file:
		replaced_content = '<!DOCTYPE html>\n<html>\n<head>\n<title>Rendered Page</title>\n</head>\n' + content + '\n</html>'
		file.write(replaced_content)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		render(sys.argv[1])