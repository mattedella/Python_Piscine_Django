

def my_var():
		a = 42
		b = "42"
		c = "quarante-deux"
		d = 42.0
		e = True
		f = [42]
		g = {"42": 42}
		h = (42,)
		i = set()
		print(a, " has type ", type(a))
		print(b, " has type:", type(b))
		print(c, " has type:", type(c))
		print(d, " has type:", type(d))
		print(e, " has type:", type(e))
		print(f, " has type:", type(f))
		print(g, " has type:", type(g))
		print(h, " has type:", type(h))
		print(i, " has type:", type(i))

if __name__ == "__main__":
		my_var()