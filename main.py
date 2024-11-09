class Students:
    def __init__(self,name,age,subjects,class_name):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.class_name = class_name
    
    def print_details(self): #geter method - accesses data and makes it available
        print(self.name)
        print(self.age)
        print(self.subjects)
        print(self.class_name)

    def change_details(self):
        self.name = input("What's your name?")
        print("Name is changed successfully")

student1 = Students("Aarush","14","Maths","10G1")
student1.change_details()
student1.print_details()