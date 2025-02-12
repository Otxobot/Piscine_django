from elem import Elem
from elements import *

class Some(str):
    def __init__(self):
        super().__init__

class Page(Elem):
    def __init__(self, elem_instance):
        # if not isinstance(elem_instance, Elem):
        #     raise Elem.ValidationError()
        self.elem_instance = elem_instance

    def is_valid(self):
        return_value = self._check(self.elem_instance)
        return return_value
    
    def _check(self, elem_instance):
        if not (isinstance(elem_instance, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(elem_instance) == Text):
            return False
        if type(elem_instance) == Text or isinstance(elem_instance, Meta):
            return True
        if isinstance(elem_instance, Html):
            content = elem_instance.content
            if len(content) == 2:
                if type(content[0], Head) and type(children[1], Body):
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
            if all([isinstance(el, (Text, P) for el in elem_instance.content)]):
                if (all(self._check(el) for el in elem_instance.content)):
                    return True
        elif isinstance(elem_instance, (Ol, Ul)) and len(elem.content) > 0 and \
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

                

def main():
    page1 = Page(Some())
    #page2 = Page(Head())

    page1.is_valid()
    #page2.is_valid()
    

if __name__ == '__main__':
    main()