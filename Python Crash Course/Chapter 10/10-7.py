while True:
    num1 = input("Please enter number 1: ")
    num2 = input("Please enter number 2: ")
    try:
        print(int(num1) +int(num2))
        break
    except ValueError:
        continue