class Stack:
    def __init__(self) -> None:

        # stack and len are private variables, no need to expose them.
        self.__st = []
        self.__len = 0

    def push(self, elt):
        self.__st.append(elt)
        self.__len += 1

    def pop(self):
        try:
            self.__st.pop(self.__len - 1)
            self.__len -= 1
        except:
            print("List Index out of range")

    def top(self):
        try:
            top = self.__st[self.__len - 1]
            return top
        except:
            print("List is empty")

    def size(self):
        return self.__len

    def is_empty(self):
        return self.__len == 0
