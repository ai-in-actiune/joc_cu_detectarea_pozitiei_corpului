import sqlite3
import hashlib

class DatabaseHandler:
    def __init__(self, db_file):
        self.db_file = db_file

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def create_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, hashed_password))

    # Add more database operations as needed

# Instantiate the database handler
db_handler = DatabaseHandler("userdata.db")
