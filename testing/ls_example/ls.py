from subprocess import check_output

"""
    This function will output 'ls' where it has been used i.e. where this python file has been run, not where it is defined.
"""

class LsContent:

    def __init__(self) -> None:
        pass

    def add(self):
        print("here === addd")
        return 5 + 5       

    def calc(self):
        print("here === calc")
        res = self.add()
        self.res = res

        return self.res