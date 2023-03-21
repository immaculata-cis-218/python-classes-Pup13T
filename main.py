"""
Create a Class for week 8 through week 10
By Joe Davis
"""

class Teachers:
    """
    Teachers class for name, age, subject:math,english,ect.
    """
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduce(self):
        """
        Return person name,age,subject
        """
        return f"Hi, my name is {self.name} and  I teach {self.subject}."
if __name__== "__main__":
    john = Teachers("John Doe", subject)
    print(john.name)
    print(john.introduce())
