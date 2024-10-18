
def get_input(number):
    is_valid1 = False
    while not is_valid1:
        try:
            num = input(f"Enter your first num {number}: ")
            num = float(num)
            is_valid1 = True
            return num
        except Exception as e:
            print(f"Enter a valid number {e}: ")
            continue

def add(num1, num2):
    return num1 + num2 
def substract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def modulous(num1, num2):
    return num1 % num2

def start():

    num1 = get_input(1)
    num2 = get_input(2)
    
    while True:
        sign = input("Enter the operation you want to do (+, - , *, /, %): ")
        if sign not in ['+','-','*','/','%']:
            print("invalid sign!")
            continue
        break
    
    if sign == '+':
        print(add(num1,num2))
    if sign == '-':
        print(substract(num1,num2))
    if sign == '*':
        print(multiply(num1,num2))
    if sign == '/':
        if num2 == 0:
            print("The dominator can't be zero!")
            print("Starting over!")
        
        else:print(divide(num1,num2))
        start()
    if sign == '%':
        print(modulous(num1,num2))
if __name__=="__main__":
    print("Hello to my simple calculator(\"\")! ")
    while True:
        user = input("Type Exit to exit the calculator or press anything to use the calculator: ").lower()
        if user == 'exit':
            break
        start()
        

