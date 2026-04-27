from Oops_concepts.demoA import A
from Oops_concepts.demoB import B

class C(B, A):
    def __init__(self, n1, n2, msg):
        A.__init__(self, n1, n2)
        B.__init__(self, msg)

    def display(self):
        print('done')

    def final(self):
        A.display(self)
        B.display(self)