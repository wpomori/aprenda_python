import sys 

class DoMath:


    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        
    def add(self):

        return f"O valor da soma é: {self.a + self.b}"
    
    def subs(self):

        return f"O valor da subtração é: {self.a - self.b}"
    
    def multi(self):

        return f"O valor da multiplicação é: {self.a * self.b}"

    def func_do_math(self, func):
        
        self.func = 'self.'+func
        return eval(self.func)()
    

c = DoMath(1, 3)
print(c.func_do_math(sys.argv[1]))



