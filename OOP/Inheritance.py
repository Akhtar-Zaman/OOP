class Person:
    def __init__(self, Name, Age, DOB):
        self.__name = Name
        self.age = Age
        self.dob = DOB

    def get_name(self):
        return self.__name

    def setName(self, New_Name):
        self.name = New_Name

    def get_summery(self):
        return f" Name: {self.__name}, Age: {self.age}, Date of Birth: {self.dob}"


class Student(Person):
    def __init__(self, Name, Age, DOB, Student_id, Student_roll):
        super().__init__(Name, Age, DOB)
        self.id = Student_id
        self.roll= Student_roll


    def get_summery(self):
        return f" Name: {self.get_name()} \n Student Id: {self.id} \n Student Roll: {self.roll} \n Age: {self.age} \n Date of Birth: {self.dob}"
        #print('Student Name: '+ self.name, 'Student id: '+ str(self.id), 'Stundent Roll: ' + str(self.roll), sep='\n', end='')

a = Student('Akhtaruzzaman Khan', 1, 10, 20, 30)
print(a.get_summery())