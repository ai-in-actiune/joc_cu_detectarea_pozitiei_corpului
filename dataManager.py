import sqlite3
import hashlib

class DatabaseHandler:
    def __init__(self, db_file):
        self.db_file = db_file

    def connect(self):
        self.conn = sqlite3.connect(self.db_file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                                    uri=True)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS userdata
                           (id INTEGER PRIMARY KEY,
                           username TEXT,
                           password TEXT)''')

    def create_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, hashed_password))

# Instantiate the database handler
db_handler = DatabaseHandler("userdata.db")
db_handler.connect()
db_handler.disconnect()
