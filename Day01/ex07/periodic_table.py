import sys

def generate_periodic_table(file_name):

	periodic_table = {}
	with open(file_name, 'r') as file:
		for line in file:
			parts = line.split('=')
			name = parts[0].strip()
			info = parts[1].strip()
			attributes = info.split(',')
			element = {}
			for attribute in attributes:
				kv = attribute.split(':')
				key = kv[0].strip()
				value = kv[1].strip()
				element[key] = value
			position = element['position']
			number = element['number']
			periodic_table[name] = {"position": position, "number": number, "data": element}
	html = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Periodic Table</title>\n<style>\ntable { border-collapse: collapse; }\ntd { border: 1px solid #ccc;width: 150px;height: 120px; vertical-align: top;padding: 6px;}\nh4 { margin: 0 0 5px; font-size: 14px; }\nul { margin: 0; padding-left: 16px; font-size: 12px; }\n</style>\n</head>\n<body>\n'
	html += "<table>\n"
	html += "  <tr>\n"
	col = 0
	for el in periodic_table:
		pos = int(periodic_table[el]['position'])
		while col < pos:
			html += "<td></td>"
			col += 1
		data = periodic_table[el]['data']
		html += "<td><h4>{name}</h4><ul><li>Number: {number}</li><li>Small: {small}</li><li>Molar: {molar}</li><li>Electron: {electron}</li></ul></td>\n".format(name=el, number=data['number'], small=data['small'], molar=data['molar'], electron=data['electron'])
		col = pos + 1
		if col > 17:
			html += "  </tr>\n  <tr>\n"
			col = 0

	html += "</tr>\n</table>\n</body>\n</html>"
	return html


if __name__ == "__main__":
	if len(sys.argv) == 2:
		periodic_table = generate_periodic_table(sys.argv[1])
		with open('periodic_table.html', 'w') as f:
			f.write(periodic_table)