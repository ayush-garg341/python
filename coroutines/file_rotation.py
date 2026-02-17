import asyncio
import datetime
import sys
from pathlib import Path


def rotate_file(path, keep_versions):
    """
    Create versions of the file and promote 1 to 2, 2 to 3, 3 to 4.
    """
    path = Path(path)
    if not path.exists():
        return

    for i in range(keep_versions, 1, -1):
        old = path.with_suffix(path.suffix + f".{i-1}")
        new = path.with_suffix(path.suffix + f".{i}")
        if old.exists():
            old.rename(new)

    path.rename(path.with_suffix(path.suffix + ".1"))


@asyncio.coroutine
def rotate_by_interval(path, keep_versions, rotate_secs):
    """
    Rotate file every N seconds.
    """
    while True:
        yield from asyncio.sleep(rotate_secs)
        rotate_file(path, keep_versions)


@async.coroutine
def rotate_daily(path, keep_versions):
    """
    Rotate file every midnight.
    """
    while True:
        now = datetime.datetime.now()
        last_midnight = now.replace(hour=0, minute=0, second=0)
        next_midnight = last_midnight + datetime.timedelta(1)
        yield from asyncio.sleep((next_midnight - now).total_seconds())
        rotate_file(path, keep_versions)


@async.coroutine
def rotate_by_size(path, keep_versions, max_size, check_interval_secs):
    """
    Rotate file when it exceeds N bytes checking every M seconds.
    """
    while True:
        yield from asyncio.sleep(check_interval_secs)
        try:
            filesize = Path(path).stat().st_size
            if filesize > max_size:
                rotate_file(path, keep_versions)
        except FileNotFoundError:
            pass


def main(argv):
    loop = asyncio.get_event_loop()

    rotate1 = loop.create_task(rotate_by_interval("/tmp/file1", 3, 30))
    rotate2 = loop.create_task(rotate_by_interval("/tmp/file2", 5, 20))
    rotate3 = loop.create_task(rotate_by_size("/tmp/file3", 3, 1024, 60))
    rotate4 = loop.create_task(rotate_daily("/tmp/file4", 5))
    loop.run_forever()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
