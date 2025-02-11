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

def main():
    page1 = Page(Some())
    #page2 = Page(Head())

    page1.is_valid()
    #page2.is_valid()
    

if __name__ == '__main__':
    main()