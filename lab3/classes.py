# 1

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())


# 2

class Shape:
    def area(self):
        print(0)  


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


# 3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


# 4

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Coordinates moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance


# 5

class Account:
    def __init__(self, owner, balance=0): 
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
             print("Withdrawal amount must be positive.")



# 6

def is_prime(n): 
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    """Filters prime numbers from a list using the filter function and a lambda."""
    return list(filter(lambda x: is_prime(x), numbers))  



if __name__ == "__main__":  

    # 1
    string_manipulator = StringManipulator()
    string_manipulator.getString()
    string_manipulator.printString()

    # 2
    square = Square(5)
    square.area()
    rectangle = Rectangle(4, 6)
    rectangle.area()
    shape = Shape()
    shape.area()

    # 2
    point1 = Point(3, 4)
    point1.show()
    point1.move(1, 1)
    point2 = Point(0, 0)
    distance = point1.dist(point2)
    print(f"Distance between point1 and point2: {distance}")

    #3
    account = Account("Alice", 100)
    account.deposit(50)
    account.withdraw(20)
    account.withdraw(200)  
    account.withdraw(-10) 


    # 4
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    prime_numbers = filter_primes(numbers)
    print(f"Prime numbers in {numbers}: {prime_numbers}")