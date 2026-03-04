from elem import Text
from elements import *
from Page import Page


# ---------- VALID PAGE ----------
page = Page(
    Html(content=[
        Head(content=[
            Title(content=Text("My page"))
        ]),
        Body(content=[
            H1(content=Text("Welcome")),
            Div(content=[
                P(content=Text("Paragraph"))
            ])
        ])
    ])
)

print(page)
print("Valid:", page.is_valid())  # True


# ---------- INVALID PAGE (No Head) ----------
bad_page = Page(
    Html(content=[
        Body(content=[])
    ])
)

print("Invalid:", bad_page.is_valid())  # False


# ---------- INVALID UL ----------
bad_ul = Page(
    Html(content=[
        Head(content=Title(content=Text("X"))),
        Body(content=[
            Ul(content=[])  # must contain at least one Li
        ])
    ])
)

print("Invalid UL:", bad_ul.is_valid())  # False


# ---------- TABLE VALID ----------
table_page = Page(
    Html(content=[
        Head(content=Title(content=Text("Table"))),
        Body(content=[
            Table(content=[
                Tr(content=[
                    Td(content=Text("A")),
                    Td(content=Text("B"))
                ])
            ])
        ])
    ])
)

print("Table valid:", table_page.is_valid())  # True