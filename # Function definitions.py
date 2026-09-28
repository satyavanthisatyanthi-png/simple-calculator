# Function definitions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

# Main program loop
while True:
    print("--- simple calculator ---")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        a = int(input("Enter first no: "))
        b = int(input("Enter second no: "))
        print("Result: ", add(a, b))
        
    elif choice == 2:
        a = int(input("Enter first no: "))
        b = int(input("Enter second no: "))
        print("Result: ", sub(a, b))
        
    elif choice == 3:
        a = int(input("Enter first no: "))
        b = int(input("Enter second no: "))
        print("Result: ", multi(a, b))
        
    elif choice == 4:
        print("Result: quitting")
        break
        
    else:
        print("Invalid choice")
        