def square(x):
    return x*x

def cubes(x):
    return x*x*x

"""
    Taking function as an argument
"""

def my_map(fun, args_list):
    result = []
    for num in args_list:
        result.append(fun(num))
    return result

result = my_map(square, [1, 2, 3, 4, 5])
print(result)

"""
    Returning function from another fun.
"""

def logger(msg):
    def log_msg():
        print("Log: ", msg)
    
    return log_msg

log = logger("Hi!")
log()



def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text

print_h1 = html_tag("h1")
print_h1("Test Headline !")
print_h1("Another Headline !")


print_p = html_tag("p")
print_p("Test Paragraph!")
