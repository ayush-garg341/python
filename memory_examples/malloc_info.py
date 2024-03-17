import ctypes


class MallInfo(ctypes.Structure):
    _fields_ = [
        (name, ctypes.c_int)
        for name in (
            "arena",
            "ordblks",
            "smblks",
            "hblks",
            "hblkhd",
            "usmblks",
            "fsmblks",
            "uordblks",
            "fordblks",
            "keepcost",
        )
    ]


libc = ctypes.CDLL("libc.so.6")
mallinfo = libc.mallinfo
mallinfo.argtypes = []
mallinfo.restype = MallInfo

info = mallinfo()
fields = [(name, getattr(info, name)) for name, _ in info._fields_]
print("Malloc info:")
for name, value in fields:
    print(f"- {name}: {value}")
