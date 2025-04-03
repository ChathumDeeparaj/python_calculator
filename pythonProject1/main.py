# These functions should cover Task 2
def Add(a, b):
    return a + b


def Subtract(a, b):
    return a - b


def Multiply(a, b):
    return a * b


def Divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)


def Power(a, b):
    return a ** b


def Remainder(a, b):
    return a % b


# -------------------------------------
# This function covers Task 1 (Section 2) and Task 3
def select_op(choice):
    if (choice == '#'):
        return -1
    elif (choice == '$'):
        return 0
    elif (choice in ('+', '-', '*', '/', '^', '%')):
        while (True):
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        while (True):
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1

            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number, please enter again")
                continue

        if choice == '+':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", Subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", Multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", Divide(num1, num2))

        elif choice == '^':
            print(num1, "^", num2, "=", Power(num1, num2))

        elif choice == '%':
            print(num1, "%", num2, "=", Remainder(num1, num2))

        else:
            print("Something Went Wrong")

    else:
        print("Unrecognized operation")


# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()