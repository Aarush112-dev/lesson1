#Inheritance

class Animal:
    def __init__(self,name,typeofanimal):
        self.name = name
        self.typeofanimal = typeofanimal

    def print_details(self):
        print("I am {} and I am a {}".format(self.name,self.typeofanimal))

class Dog(Animal):
    def __init__(self, name, typeofanimal,food):
        super().__init__(name, typeofanimal)
        self.food = food

    def print_details(self):
        print("I am {} and I am a {} and I eat {}".format(self.name,self.typeofanimal,self.food)) #polymorphism

class Smalldog(Dog):
    def __init__(self, name, typeofanimal, food,size):
        super().__init__(name,typeofanimal,food)
        self.size = size

    def print_details(self):
        print("I am {} and I am a {} {} and I eat {}".format(self.name,self.size,self.typeofanimal,self.food))


animal1 = Animal("Zebra","herbivor")
animal1.print_details()
dog1 = Dog("dog","carnivore","meat")
dog1.print_details()
smalldog1 = Smalldog("smalldog","omnivore","anything","small")
smalldog1.print_details()

