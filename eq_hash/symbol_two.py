class Symbol:

    symbols = {}

    def __init__(self, value):
        self.value = value

    @staticmethod
    def get(key):
        if key in Symbol.symbols:
            return Symbol.symbols[key]
        else:
            value = Symbol(key) # instance of symbol
            Symbol.symbols[key] = value
            return value

    def __str__(self):
        if self.isEpsilon():
            return "e"
        else:
            return str(self.value)

    def isEpsilon(self):
        if self.value == None:
            return True
        else:
            return False


if __name__ == "__main__":
    x = Symbol.get("NP") 
    y = Symbol.get("NP")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)  # True, since NP is already in dict, and hence get return/points to the same memory location.
    print(x == y)  # True
    print(len(symbols)) # 1


    """
        If there is a need to minimize memory usage, then this method is preferred, since both objects points to same 
        memory location.
    """