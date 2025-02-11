from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')
    
class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')
    
class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='simple')

def test1():
    return Html([Head(), Body()])

def test2():
    return Html([Head([Meta(), ]), Title(Text('This is the title'))])

def test3():
    return P(Text('This text'))

def test4():
    return Img(attr={'src': 'path/to/image'})

def main():
    tests = [test1, test2, test3, test4]
    for test in tests:
        print("===============")
        print(test())
    print("===============")
    print("Example html:")
    print("===============")
    print( Html([ Head([Title(content=Text('"Hello ground!"'))]), Body([H1(content=Text('"Oh no, not again!"')), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]))

if __name__ == '__main__':
    main()