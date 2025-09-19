
def add (n1, n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1 ,n2):
    return n1*n2
def divide(n1 ,n2):
    return n1/n2

operations = { "+ " : add ,
              "-": sub,
              "*": multiply,
              "/": divide,}


# print(operations["*"](n1:4, n2:8))
def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number"))
    while should_accumulate :
        
        for symbol in operations:
            print(symbol)
        operator = input(  "Pick an operation: \n")
        num2 = float(input("What is the next number:"))
        answer = operations[operator](num1,num2)
        print(f"{num1}{operator}{num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer} , or type 'n' to start a new calculation")
        if choice == "y":
            num1 = {answer}
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
            
calculator()          
        






