class employee:
    def __init__(self,name):
        self.name = name
        print("Constructor is Called")

    def __del__(self):
        print("Deconstructor is Called")

e=employee("prashant")