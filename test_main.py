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
