import sqlite3


class DBConn:
    def __init__(self, db_name) -> None:
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the db connection
        """
        print("enter")
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closing the connection"""
        print("exit")
        self.conn.close()
        if exc_val:
            raise


if __name__ == "__main__":
    db = "test.db"
    with DBConn(db) as conn:
        cursor = conn.cursor()
