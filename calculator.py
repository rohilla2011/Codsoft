print("Add")
print("Subtract")
print("Multiply")
print("Divide")
entry = input("Choose an operation: ")
if entry in ["add","subtract","multiply","divide"]:
    number1 = int(input("type a number :"))
    number2 = int(input("type a number :"))
    if entry == ("add"):
        print(number1+number2)
    elif entry ==("subtract"):
        print(number1-number2)
    elif entry == ("multiply"):
        print(number1 * number2)
    elif entry == ("divide"):
        print(number1 // number2)
else:
    print("Invalid Entry")
