class Calculator:
    def add (self , a , b):
        return a + b
    def sub (self , a , b):
        return a - b
    def mul (self , a , b):
        return a * b
    def div (self , a , b):
        if b != 0:
            return a / b
        else:
            return "Error: Disivion by zero"
Calculator = Calculator()

result_add = Calculator.add(10, 20) 
result_sub = Calculator.sub(10, 20)
result_mul = Calculator.mul(10, 20)
result_div = Calculator.div(10, 20)

print(f"addition is {result_add}")
print(f"subtraction is {result_sub}")
print(f"multiplication is {result_mul}")
print(f"division is {result_div}")
