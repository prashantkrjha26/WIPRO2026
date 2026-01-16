from abc import ABC,abstractmethod
class BANK(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(BANK):
    def interest(self):
            print("intrest is 6 %")
    def loan(self):
        print("loan is avilable")

s=SBI()
s.interest()
s.loan()