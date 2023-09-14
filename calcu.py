def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x//y


def main():
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("When you add both numbers, you get:",add(x,y))
    print("When you subtract both numbers, you get:",subtract(x,y))
    print("When you multiply both numbers, you get:",multiply(x,y))
    print("When you divide both numbers, you get:",divide(x,y))
    
          
z=10
z=z+5
print(z)