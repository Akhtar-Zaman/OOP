
#   Object declearation Practice

class Person:
    def __init__(self, Name, Age, DOB):
        self.name = Name
        self.age = Age
        self.dob = DOB

    def get_name(self):
        return self.name

    def setName(self, New_Name):
        self.name = New_Name

    def get_summery(self):
        return f"Name: {self.name},\nAge: {self.age},\nDate of Birth: {self.dob}"

person_details =[
                    Person("Akhtaruzzaman Khan", 23, "18 september"),
                    Person("Abdul Latif Khan", 65, "18 september"),
                    Person("Abid Khan", 35, "18 september")                    
                ]
person_name = Person("Akhtaruzzaman Khan", 23, "18 september")
person_name.setName("Akhtaruzzamannnnnnnnnnnnnnnnnnnn Khan")
#print(person_name.get_summery())

for person in person_details:
    print(person.get_summery())
    print()


