from elem import Elem, Text
from elements import *


class Page:

    ALLOWED_TYPES = (
        Html, Head, Body, Title, Meta, Img,
        Table, Th, Tr, Td,
        Ul, Ol, Li,
        H1, H2, P, Div, Span,
        Hr, Br, Text
    )

    def __init__(self, root):
        if not isinstance(root, Elem):
            raise TypeError("Page must be initialized with an Elem instance.")
        self.root = root

    # ==========================
    # VALIDATION ENTRY POINT
    # ==========================

    def is_valid(self):
        return self.__validate_node(self.root)

    # ==========================
    # RECURSIVE VALIDATION
    # ==========================

    def __validate_node(self, node):

        # Rule 1: Allowed types only
        if not isinstance(node, self.ALLOWED_TYPES):
            return False

        if isinstance(node, Text):
            return True

        children = node.content

        # ---------- HTML ----------
        if isinstance(node, Html):
            return (
                len(children) == 2 and
                isinstance(children[0], Head) and
                isinstance(children[1], Body) and
                all(self.__validate_node(c) for c in children)
            )

        # ---------- HEAD ----------
        if isinstance(node, Head):
            titles = [c for c in children if isinstance(c, Title)]
            return (
                len(titles) == 1 and
                all(isinstance(c, (Title, Meta)) for c in children) and
                all(self.__validate_node(c) for c in children)
            )

        # ---------- BODY / DIV ----------
        if isinstance(node, (Body, Div)):
            allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            return (
                all(isinstance(c, allowed) for c in children) and
                all(self.__validate_node(c) for c in children)
            )

        # ---------- Title / H1 / H2 / Li / Th / Td ----------
        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            return (
                len(children) == 1 and
                isinstance(children[0], Text)
            )

        # ---------- P ----------
        if isinstance(node, P):
            return all(isinstance(c, Text) for c in children)

        # ---------- Span ----------
        if isinstance(node, Span):
            return (
                all(isinstance(c, (Text, P)) for c in children) and
                all(self.__validate_node(c) for c in children)
            )

        # ---------- UL / OL ----------
        if isinstance(node, (Ul, Ol)):
            return (
                len(children) >= 1 and
                all(isinstance(c, Li) for c in children) and
                all(self.__validate_node(c) for c in children)
            )

        # ---------- TR ----------
        if isinstance(node, Tr):
            if len(children) == 0:
                return False

            if all(isinstance(c, Th) for c in children):
                return all(self.__validate_node(c) for c in children)

            if all(isinstance(c, Td) for c in children):
                return all(self.__validate_node(c) for c in children)

            return False

        # ---------- TABLE ----------
        if isinstance(node, Table):
            return (
                len(children) >= 1 and
                all(isinstance(c, Tr) for c in children) and
                all(self.__validate_node(c) for c in children)
            )

        # Self-closing or other simple tags
        return all(self.__validate_node(c) for c in children)

    # ==========================
    # STRING REPRESENTATION
    # ==========================

    def __str__(self):
        html = str(self.root)
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + html
        return html

    # ==========================
    # FILE WRITING
    # ==========================

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))