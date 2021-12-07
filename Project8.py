import random

class Bird:

    species = "Bird"
    kingdom = "Animalia"
    phylum = "Chordata"
    speciesClass = "Aves"

    def __init__(self, name, birdType = "Woodpecker"):
        self.name = name
        self.birdType = birdType

    def squawk(self):
        print("Squawk! my name is", self.name)

    def fly(self):
        choice = random.randint(1,3)
        if choice == 1:
            print(self.name, "is flying straight down!")
        elif choice == 2:
            print(self.name, "is turning right!")
        elif choice == 3:
            print(self.name, " just crashed!")
        else:
            print(self.name, "is not flying")

x = -1
b1 = input("Please enter the name of bird 1: ")
b2 = input("Please enter the name of bird 2: ")

bird1 = Bird(b1)
bird2 = Bird(b2)
while x == -1:
    try:
        yORn = int(input("Do you want to specifiy the bird types? Type 1 for yes, and 0 for no."))
    except:
        print("Enter whole integer values only please")
        continue

    if yORn == 0:
        break
    elif yORn == 1:
        option = int(input("Please enter 1 for bird 1, or 2 for bird 2:"))
        if option == 1:
            bird1.birdType = input("Enter name:")
        elif option == 2:
            bird2.birdType = input("Enter name:")
        else:
            print("Not an option, try again")
            continue
    else:
        print("Not an option, try again")
        continue

bird1.squawk(), print(bird1.name, "is a", bird1.birdType)
bird2.squawk(), print(bird2.name, "is a", bird2.birdType)

method_list = [method for method in dir(bird1) if method.startswith('__') is False]
method_list2 = [method for method in dir(bird2) if method.startswith('__') is False]

print("Bird1:", bird1.__dict__)
print("Bird1:", method_list)
print("Bird2:", bird2.__dict__)
print("Bird2:", method_list2)
print("Bird Class:", dir(Bird))

flying = input("Type 1 if you want to fly!")
if flying == "1":
    bird1.fly()

