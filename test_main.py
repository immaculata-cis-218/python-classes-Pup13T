"""
Testing program, Teachers higher tenure with salary
"""

from main import Teachers, Hightenure, Salaryrate

def test_teachers():
    """
    Test Teachers class
    """
    test_teachers1 = Teachers("John Doe", 25, "English")
    introduce = test_teachers1.introduce()
    assert "John Doe" in introduce
    test_teachers2 = Teachers("Jane Doe", 28, "Math")
    introduce = test_teachers2.introduce()
    assert "Jane Doe" in introduce

def test_repr():
    """
    Test repr function
    """
    test_teachers1 = Teachers("John Doe", 25, "English")
    assert repr(test_teachers1) == "Teacher(name='John Doe', age=25, subject='English')"

def test_str():
    """
    Test str function
    """
    test_teachers1 = Teachers("John Doe", 25, "English")
    assert str(test_teachers1) == "John Doe English teacher."

def test_eq():
    """
    Test equal function
    """
    test_teacher1 = Teachers("John Doe", 25, "English")
    test_teacher2 = Teachers("John Doe", 25, "English")
    assert test_teacher1 == test_teacher2

def test_lt():
    """
    Test less than function
    """
    test_teacher1 = Teachers("John Doe", 25, "English")
    test_teacher2 = Teachers("Jane Doe", 28, "Math")
    assert test_teacher1 < test_teacher2

def test_gt():
    """
    Test greater than function
    """
    test_teacher1 = Teachers("John Doe", 25, "English")
    test_teacher2 = Teachers("Jane Doe", 28, "Math")
    assert test_teacher2 > test_teacher1

def test_hightenure():
    """
    Test high tenure
    """
    testhightenure1 = Hightenure("Patrick Star", 30, "English", "higher tenure")
    introduce = testhightenure1.introduce()
    assert "Patrick Star" in introduce
    assert "higher tenure" in introduce

def test_salaryrate():
    """
    Test salary
    """
    testsalaryrate1 = Salaryrate("Sarah Scott", 33, "Science", 70000)
    introduce = testsalaryrate1.introduce()
    assert "Sarah Scott" in introduce
    assert "70000" in introduce
