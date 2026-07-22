class Calculator:
    def calculate(self):
        try:
            num1 = float(input("enter num1: "))
            opr = input("enter operator: ")
            num2 = float(input("enter num2: "))

            if opr == '+':
                return num1 + num2
            elif opr == '-':
                return num1 - num2
            elif opr == '*':
                return num1 * num2
            elif opr == '/':
                return num1 / num2
            else:
                return "Invalid operator!"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
        except ValueError:
            return "Error: Invalid number input!"

calc = Calculator()
print(calc.calculate())