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
        return f"Hi, my name is {self.name} and I am {self.age}. I teach {self.subject}."
if __name__== "__main__":
    john = Teachers("John Doe")
    print(john.introduce())
    jane = Teachers("Jane Doe", 28, subject= "Math")
    print(jane.introduce())
