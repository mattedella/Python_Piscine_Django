from elements import Html, Head, Body, Title, H1, P
from elem import Text

if __name__ == "__main__":

	page = Html(content=[
	    Head(content=Title(content=Text("My Page"))),
	    Body(content=[
	        H1(content=Text("Welcome")),
	        P(content=Text("Hello world"))
	    ])
	])
	
	print(page)