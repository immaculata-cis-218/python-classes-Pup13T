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

    def __repr__(self):
        """
        Returns a complete representation of the object
         """
        return f"Teacher(name='{self.name}', age={self.age}, subject='{self.subject}')"

    def __str__(self):
        """
        Returns a human readable string
         """
        return f"{self.name} {self.subject} teacher."

    def __eq__(self, other):
        """
        Age and Name are same
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.age == other.age and self.name == other.name

    def __lt__(self, other):
        """
        Age is less than other
        """
        return self.age < other.age

    def __gt__(self, other):
        """
        Age is greater than or equal to other
        """
        return self.age >= other.age

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

    def __eq__(self, other):
        """
        Equal
        """
        if isinstance(other, Hightenure):
            return self.tenure == other.tenure and self.age == other.age
        else:
            return False

    def __lt__(self, other):
        """
        tenure less than other
        """
        return self.tenure < other.tenure

    def __gt__(self, other):
        """
        tenure greater than or equal to other
        """
        return self.tenure >= other.tenure

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
    print(repr(john))
    print(str(john))

    jane = Teachers("Jane Doe", age=28, subject= "Math")
    print(jane.introduce())
    print(str(jane))

    patrick = Hightenure("Patrick Star", age=30, subject="English")
    print(patrick.introduce())

    sarah = Salaryrate("Sarah Scott", age=33, subject="Science", salary=70000)
    print(sarah.introduce())
