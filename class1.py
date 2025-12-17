class Child:
    def __init__(self, name, age, favcolour):
        self.name = name
        self.age = age
        self.favcolour = favcolour

    def info(self):
        print("My name is", self.name )
        print("I am", self.age, "years old")
        print("I love all the colours but by favourite is", self.favcolour) 
child1 = Child("Amie", 3, "pink")
child2 = Child("James", 9, "orange")
child1.info()
child2.info()