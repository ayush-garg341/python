from subprocess import check_output

"""
    This function will output 'ls' where it has been used i.e. where this python file has been run, not where it is defined.
"""


def print_contents_of_cwd():
    return check_output(['ls']).split()

# print(print_contents_of_cwd())