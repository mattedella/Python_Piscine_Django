from elem import Elem


# Root structure
class Html(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('html', attr, content)


class Head(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('head', attr, content)


class Body(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('body', attr, content)


# Metadata
class Title(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('title', attr, content)


class Meta(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('meta', attr, content, tag_type='simple')


# Media
class Img(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('img', attr, content, tag_type='simple')


# Tables
class Table(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('table', attr, content)


class Th(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('th', attr, content)


class Tr(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('tr', attr, content)


class Td(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('td', attr, content)


# Lists
class Ul(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('ul', attr, content)


class Ol(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('ol', attr, content)


class Li(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('li', attr, content)


# Headings
class H1(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('h1', attr, content)


class H2(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('h2', attr, content)


# Text structure
class P(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('p', attr, content)


class Div(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('div', attr, content)


class Span(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('span', attr, content)


# Self-closing
class Hr(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('hr', attr, content, tag_type='simple')


class Br(Elem):
    def __init__(self, attr=None, content=None):
        super().__init__('br', attr, content, tag_type='simple')