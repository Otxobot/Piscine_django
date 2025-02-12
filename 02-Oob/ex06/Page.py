from elem import Elem
from elements import *

class Some(str):
    def __init__(self):
        super().__init__

class Page(Elem):
    def __init__(self, elem_instance):
        if not isinstance(elem_instance, Elem):
            raise Elem.ValidationError()
        self.elem_instance = elem_instance

    def __str__(self):
        result = ""
        if isinstance(self.elem_instance, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem_instance)
        return result
    
    def write_to_file(self, path: str):
        file = open(path, "w")
        file.write(self.__str__())

    def is_valid(self):
        return self._check(self.elem_instance)
    
    def _check(self, elem_instance):
        if not (isinstance(elem_instance, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(elem_instance) == Text):
            return False
        if type(elem_instance) == Text or isinstance(elem_instance, Meta):
            return True
        if isinstance(elem_instance, Html):
            content = elem_instance.content
            if len(content) == 2:
                if type(content[0]) == Head and type(content[1]) == Body:
                    if (all(self._check(el) for el in content)):
                        return True
        elif isinstance(elem_instance, Head):
            content = elem_instance.content
            if [isinstance(el, Title) for el in content].count(True) == 1:
                if (all(self._check(el) for el in content)):
                    return True
        elif isinstance(elem_instance, (Body, Div)):
            allowed_types = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            content = elem_instance.content
            if all(isinstance(el, allowed_types) for el in content):
                if all(self._check(el) for el in content):
                    return True
        elif isinstance(elem_instance, (Title, H1, H2, Li, Th, Td)):
            content = elem_instance.content
            if len(content) == 1 and type(content[0]) == Text:
                return True
        elif isinstance(elem_instance, P):
            content = elem_instance.content
            if all([isinstance(el, Text) for el in content]):
                return True
        elif isinstance(elem_instance, Span):
            if all([isinstance(el, (Text, P)) for el in elem_instance.content]):
                if (all(self._check(el) for el in elem_instance.content)):
                    return True
        elif isinstance(elem_instance, (Ol, Ul)) and len(elem_instance.content) > 0 and \
            all([isinstance(el, Li) for el in elem_instance.content]):
                if (all(self._check(el) for el in elem_instance.content)):
                    return True
        elif isinstance(elem_instance, Tr) and len(elem_instance.content) > 0 and \
            all([isinstance(el, (Th, Td)) for el in elem_instance.content]) and \
                all([type(el) == type(elem_instance.content[0]) for el in elem_instance.content]):
                    return True
        elif isinstance(elem_instance, Table) and \
            all([isinstance(el, Tr) for el in elem_instance.content]):
                return True
        return False

                

def __print_test(target: Page, expected: bool):
    print("\n================START===============")
    print(str(target))
    print("===============IS_VALID=============")
    result = target.is_valid()
    print(f"Expected: {expected}, Got: {result}")
    assert result == expected
    print("=================END================")


def __test_Table():
    print("\n===== Testing Table =====")
    __print_test(Page(Table()), True)
    __print_test(Page(Table([Tr()])), True)
    __print_test(Page(Table([H1(Text("Hello World!"))])), False)


def __test_Tr():
    print("\n===== Testing Tr =====")
    __print_test(Page(Tr()), False)
    __print_test(Page(Tr([Th(Text("Title"))] * 5)), True)
    __print_test(Page(Tr([Td(Text("Content"))] * 6)), True)
    __print_test(Page(Tr([Th(Text("Title")), Td(Text("Content"))])), False)


def __test_Ul_Ol():
    print("\n===== Testing Ul and Ol =====")
    __print_test(Page(Ul()), False)
    __print_test(Page(Ol()), False)
    __print_test(Page(Ul(Li(Text('Test')))), True)
    __print_test(Page(Ol(Li(Text('Test')))), True)
    __print_test(Page(Ul([Li(Text('Test')), Li(Text('Another Test'))])), True)
    __print_test(Page(Ol([Li(Text('Test')), H1(Text('Invalid'))])), False)


def __test_Span():
    print("\n===== Testing Span =====")
    __print_test(Page(Span()), True)
    __print_test(Page(Span([Text("Hello?"), P(Text("World!"))])), True)
    __print_test(Page(Span([H1(Text("Invalid"))])), False)


def __test_P():
    print("\n===== Testing P =====")
    __print_test(Page(P()), True)
    __print_test(Page(P(Text("Hello?"))), True)
    __print_test(Page(P(H1(Text("Invalid")))), False)


def __test_Title_H1_H2_Li_Th_Td():
    print("\n===== Testing Title, H1, H2, Li, Th, Td =====")
    for elem in [H1, H2, Li, Th, Td]:
        __print_test(Page(elem()), False)
        __print_test(Page(elem(Text("Valid"))), True)
        __print_test(Page(elem([Text("Valid"), Text("Extra Text")])), False)


def __test_Body_Div():
    print("\n===== Testing Body and Div =====")
    for elem in [Body, Div]:
        __print_test(Page(elem()), True)
        __print_test(Page(elem(Text("Hello"))), True)
        __print_test(Page(elem([Text("Hello"), Span()])), True)
        __print_test(Page(elem([Html(), elem()])), False)


def __test_Title():
    print("\n===== Testing Title =====")
    __print_test(Page(Title()), False)
    __print_test(Page(Title(Text("Valid Title"))), True)
    __print_test(Page(Title([Text("Valid"), Text("Extra")])), False)


def __test_Html():
    print("\n===== Testing Html =====")
    __print_test(Page(Html()), False)
    __print_test(Page(Html([Head(Title(Text("Page Title"))), Body(H1(Text("Content")))])), True)
    __print_test(Page(Html(Div())), False)


def __test_Elem():
    print("\n===== Testing Elem =====")
    __print_test(Page(Elem()), False)


def __test_write_to_file(target: Page, path: str):
    print("\n================START===============")
    print(str(target))
    print("==========WRITE_TO_FILE=============")
    target.write_to_file(path)
    print(f"Written to: {path}")
    print("=================END================")


def __test():
    __test_Table()
    __test_Tr()
    __test_Ul_Ol()
    __test_Span()
    __test_P()
    __test_Title_H1_H2_Li_Th_Td()
    __test_Body_Div()
    __test_Html()
    __test_Elem()
    __test_write_to_file(
        Page(Html([Head(Title(Text("hello world"))), Body(H1(Text("HELLO WORLD!")))])),
        "__test_write_to_file.html"
    )


if __name__ == '__main__':
    __test()
