class Parent:
    def __init__(self, x=0):  # Default constructor with default value for x
        self.x = x
        print("Parent constructor called with x =", x)

class Child(Parent):
    def __init__(self, y, x=10):  # Child constructor with y and optional x
        super().__init__(x)  # Call parent constructor with x
        self.y = y
        print("Child constructor called with y =", y)

# Create a child object
child = Child(20, 5)  # Calls child constructor with y=20 and x=5

print(child.x)
print(child.y)