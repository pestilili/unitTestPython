def sum(x, y):
    return x + y

def  substract(x, y):
    return x -y

def  multiply(x, y):
    return x * y

def  divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "0-vál nem lehet osztani"

#print(sum(2,3))
#print(substract(2,3))
#print(multiply(2,3))
#print(divide(2,0))