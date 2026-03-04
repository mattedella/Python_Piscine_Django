class Text(str):

    def __new__(cls, value=""):
        return super().__new__(cls, str(value))

    def __str__(self):
        text = super().__str__()

        # Escape HTML characters
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        text = text.replace('"', "&quot;")

        # Replace newline
        text = text.replace("\n", "\n<br />\n")

        return text


class Elem:

    class ValidationError(Exception):
        def __init__(self, message="Content must be of type Elem or Text."):
            super().__init__(message)

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.tag_type = tag_type

        if content is None:
            self.content = []
        elif isinstance(content, list):
            if not all(isinstance(elem, (Elem, Text)) for elem in content):
                raise Elem.ValidationError()
            self.content = content
        elif isinstance(content, (Elem, Text)):
            self.content = [content]
        else:
            raise Elem.ValidationError()

    def __make_attr(self):
        result = ""
        for key, value in sorted(self.attr.items()):
            result += f' {key}="{value}"'
        return result

    def __render(self, indent=0):
        attrs = self.__make_attr()
        space = "  " * indent

        # Filter empty Text nodes
        valid_content = [
            elem for elem in self.content
            if not (isinstance(elem, Text) and str(elem) == "")
        ]

        if self.tag_type == 'simple':
            return f"{space}<{self.tag}{attrs} />"

        if not valid_content:
            return f"{space}<{self.tag}{attrs}></{self.tag}>"

        result = f"{space}<{self.tag}{attrs}>"

        for elem in valid_content:
            if isinstance(elem, Elem):
                result += "\n" + elem.__render(indent + 1)
            else:  # Text
                result += "\n" + "  " * (indent + 1) + str(elem)

        result += f"\n{space}</{self.tag}>"
        return result

    def __str__(self):
        return self.__render()

    def add_content(self, content):
        if isinstance(content, list):
            if not all(isinstance(elem, (Elem, Text)) for elem in content):
                raise Elem.ValidationError()
            self.content.extend(content)
        elif isinstance(content, (Elem, Text)):
            self.content.append(content)
        else:
            raise Elem.ValidationError()