class Person:

    def __init__(self , name , age , city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello my name is {self.name} , I am {self.age} , I live in {self.city}")

    def is_adult(self):
         if self.age >= 18 :
             print(True)
             return  True
         else:
             print(False)
             return False


    def __str__(self):
        return (f"name :{self.name}, age: {self.age}, city: {self.city}")

person1 = Person("adil", 16, "Bishkek")
person2 = Person("DED", 64, "Bishkek")
person3 = Person("arsen", 18, "Bishkek")
person4 = Person("baby", 6, "Bishkek")

person1.introduce()

person2.is_adult()
person3.is_adult()
person4.is_adult()

print(person1)