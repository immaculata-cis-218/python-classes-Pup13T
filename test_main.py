"""
Testing program, Teachers higher tenure with salary
"""

from main import Teachers

def Test_Teachers():
    test_teachers1 = Teachers("John Doe", 25, "English")
    introduce = test_teacher.introduce
    assert "John Doe" in introduce
