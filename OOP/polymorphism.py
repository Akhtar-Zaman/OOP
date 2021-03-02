# Polymorphism 
#######################################################################################

class Person2:
    def __init__(self, Name, Age, DOB):
        self.__name = Name
        self.age = Age
        self.dob = DOB

    def get_name(self):
        return self.__name

    def setName(self, New_Name):
        self.__name = New_Name

    def get_summery(self):
        return f"Name: {self.__name}, \nAge: {self.age}, \nDate of Birth: {self.dob}"

person_name = Person2("Akhtaruzzaman Khan", 23, "18 september")
person_name.setName("Akhtaruzzamannnnnnnnnnnnnnnnnnnn Khan")
#print(person_name.name)
print(person_name.get_summery())

# person_details2 =[
#                     Person2("Akhtaruzzaman Khan", 23, "18 september"),
#                     Person2("Abdul Latif Khan", 65, "18 september"),
#                     Person2("Abid Khan", 35, "18 september")                    
#                 ]

# for person2 in person_details2:
#     if person2.age>25:
#         print(person2.age)
