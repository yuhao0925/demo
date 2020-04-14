

class Document(object):

    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError('1111')


class Pdf(Document):
    def show(self):
        return '呵呵呵'


class word(Document):
    def show(self):
        return '6666'

aaa = Pdf('来呀')
bbb = word('你走把')

objs = [aaa,bbb]
for o in objs:
    print(o.show())


