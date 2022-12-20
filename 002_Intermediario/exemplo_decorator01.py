#!/usr/bin/env python3

class DoMath:


    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        
    def add(self):

        return f"The sum is: {self.a + self.b}"
    
    def subs(self):

        return f"The subtraction value is: {self.a - self.b}"
    
    def multi(self):

        return f"The multiplication value is: {self.a * self.b}"

    def func_do_math(self, func):
        
        self.func = 'self.'+func
        return eval(self.func)()
    

def do_math(func, a: float, b: float):
    return func(a, b)
    
def add(a: float, b: float):
    return f"The sum is: {a + b}"

def subtract(a: float, b: float):
    return f"The subtraction value is: {a - b}"
    
def multiply(a: float, b: float):
    return f"The multiplication value is: {a * b}"

def divide(a: float, b: float):
    return f"The division value is: {a * b}"


def math_decorator(func):
    def inner_function(*args, **kwarg):
        print('Here I can do anything')
        f, a, b = args
        if f == divide and b == 0:
            raise Exception('It is not possible to divide by zero. {ZeroDivisionError}')
        result = func(*args, **kwarg)
        return result
    return inner_function    

@math_decorator
def do_math_with_decorator(func, a: float, b: float):
    return func(a, b)
    
     
if __name__ == '__main__':
    with_class = DoMath(1, 3)
    print('Using class:\n', with_class.func_do_math('add'))
    
    with_func = do_math(add, 1, 2)
    print('Using function:\n', with_func)
    
    with_decorator = do_math_with_decorator(divide, 5, 0)
    print('Using decorator:\n', with_decorator)
