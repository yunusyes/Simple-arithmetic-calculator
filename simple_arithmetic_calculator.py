class Calculator():
    def add(self, n1, n2):
        return n1 + n2
        
    def subtract(self, n1, n2):
        return n1 - n2
        
    def multiply(self, n1, n2):
        return n1 * n2
        
    def divide(self, n1, n2):
        return n1 / n2
    
Calculator = Calculator()  
        
def main():
    operator = input("Enter the operation ([+], [-], [/], [*]) you want to perform, enter the operation sign only: ")
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("You didn't type a valid number") 
        return  
    if operator == "+":
        print(Calculator.add(n1, n2))
    elif operator == "-":
        print(Calculator.subtract(n1, n2))
    elif operator == "*":
        print(Calculator.multiply(n1, n2))
    elif operator == "/":
        try:
            print(Calculator.divide(n1, n2))
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation, try again")
        
        
if __name__ == "__main__":
    main()