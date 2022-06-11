import rebirth

def same():
    print("The result is the same number")

def dif():
    print("This is not the same number")

a = 2 + 2
b = 5 - 1

rebirth.check_response(a, b, same, dif)