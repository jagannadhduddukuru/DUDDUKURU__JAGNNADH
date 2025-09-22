# problem-1 : simple calculator using class
class calculator:
    def __init__(self,a,b):
        self.a = float(a)
        self.b = float(b)

    def opreate(self,opreation):
        if opreation == "add":
            return self.a + self.b
        elif opreation == "sub":
            return self.a - self.b
        elif opreation == "mul":
            return self.a * self.b
        elif opreation == "div":
            #handling division by zero
            return self.a / self.b if self.b != 0 else " division by zero not allowed"
        else:
            return "invalid opreation" 
    # output
a = float(input("enter first number : "))
b = float(input("enter secound number : "))
opreation = input("enter opreation (add, sub, mul, div): ")


calc = calculator(a,b)
print("Result:",calc.opreate(opreation)) 