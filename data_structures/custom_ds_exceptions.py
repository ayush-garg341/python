class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class LinkedListEmptyException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return f"{self.msg}"
