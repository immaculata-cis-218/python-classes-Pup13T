"""
Create a Class for week 8 through week 10
By Joe Davis
"""

class Teachers:
    """
    Teachers class for name, age, subject:math,english,ect.
    """
    def __init__(self, name, age=25, subject="English"):
        self.name = name
        self.age = age
        self.subject = subject
    def introduce(self):
        """
        Return person name,age,subject
        """
        return f"Hi, my name is {self.name} and I am {self.age}. I teach {self.subject}"

class Hightenure(Teachers):
    """
    tenure of teacher
    """
    def __init__(self, name, age=30, subject="English", tenure="higher tenure"):
        self.tenure = tenure
        super().__init__(name, age, subject)

    def introduce(self):
        introduce= super().introduce()
        introduce= f"{introduce} and I have {self.tenure} teaching"
        return introduce
class Salaryrate(Teachers):
    """
    Certain pay
    """
    def __init__(self, name, age, subject, salary):
        self.salary = salary
        super().__init__(name, age, subject)

    def introduce(self):
        introduce= super().introduce()
        introduce= f"{introduce} and my salary is {self.salary}"
        return introduce

if __name__== "__main__":
    john = Teachers("John Doe")
    print(john.introduce())
    jane = Teachers("Jane Doe", 28, subject= "Math")
    print(jane.introduce())

    patrick = Hightenure("Patrick Star", age=30, subject="English")
    print(patrick.introduce())

    sarah = Salaryrate("Sarah Scott", age=33, subject="Science", salary=70000)
    print(sarah.introduce())
    