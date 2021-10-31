from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        file_obj = open(path, 'w')
        yield file_obj
    except OSError:
        print("we had an error opening the file")
    finally:
        print("Closing the file")
        file_obj.close()

if __name__=="__main__":
    with file_open("test.txt") as fobj:
        fobj.write("Hi this is Ayush Garg testing context managers")