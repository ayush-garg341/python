# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""

    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""

    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""

    pass


class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")


"""
    try except are used to handle the error gracefully, so that our code does not break and we can return proper error
    response to the application.
    
    Without try except code will throw error and will break. Try removing try except from below code and notice.
"""

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    try:
        raise SalaryNotInRangeError(salary)
    except SalaryNotInRangeError as sal:
        print(sal)
