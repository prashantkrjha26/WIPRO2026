class A:
    def showA(self):
        print("A")

class B:
    def showB(self):
        print("B")

    def showA(self):
        print("A from Class B")

class C(B,A):         # python follow method resolution order which method name is first it will take that method in case of same method name
    pass

c=C()
c.showA()
c.showB()