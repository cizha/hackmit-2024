import sqlite3
from urllib import request
import json
import random
import os

class SequenceManager:
    def __init__(self, db_path='sequences.db'):
        self.eois_id = None
        self.eois_res = None
        self.eois_values = None
        self.eois_offset = None
        self.eois_name = None

        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    ################################ EOIS ################################

    def set_random_eois(self):
        self.eois_id = 'A' + str(random.randint(1,376183)).zfill(6)

    def set_eois_id(self, eois_id):
        self.eois_id = eois_id

        url = f'https://oeis.org/search?q=id:{self.eois_id}&fmt=json'
        res = request.urlopen(url)
        self.eois_res = json.loads(res.read().decode())['results'][0]

        self.update_eois_value()
        self.generate_sequence()

    def update_eois_value(self):
        self.eois_values = [int(value) for value in self.eois_res['data'].split(',')]
        self.eois_name = self.eois_res['name']
        self.eois_offset = int(self.eois_res['offset'].split(',')[0])

    ################################ SQL ################################

    def create_database(self):
        """Create SQLite database and sequences table."""
        # Remove the existing database file if it exists
        if os.path.exists(self.db_path):
            return

        # Connect to SQLite (creates the database if it doesn't exist)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        # Create a table for storing sequences with a UNIQUE constraint on (name, value)
        self.cursor.execute('''
            CREATE TABLE sequences (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                value INTEGER NOT NULL,
                UNIQUE(name, value)
            )
        ''')

        # Commit and close the connection
        self.conn.commit()

    def verify_number(self, n):
        try:
            self.cursor.execute('''
                SELECT 1 FROM sequences
                WHERE oeis_id = ? AND value = ?
                LIMIT 1
            ''', (self.eois_id, n))
            result = self.cursor.fetchone()
            return result is not None # Returns True if the number is found
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False

    def insert_value(self, val, n):
        try:
            self.cursor.execute('''
            INSERT INTO sequences (oeis_id, oeis_name, n, value) 
            VALUES (?, ?, ?, ?)
        ''', (self.eois_id, self.eois_name, n, val))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Failed to insert ({self.eois_id}, {val}) due to uniqueness constraint.")

    def generate_sequence(self):
        for (n, value) in enumerate(self.eois_values, start=self.eois_offset):
            self.insert_value(value, n)
        # TODO Basically check if the sequence is already generated
        # TODO If it is not then add the eois sequence to the database
            # You can add things to the data base by looking at the values giving
            # If that isn't that amazing you can try running their python code (hopefully have their dependencies)
            # Basically look for import statements and then checking if that exists within your repository
            # Then tell the user to include that in your repository
            # Also the fun part is if you can dynamically look at other functions defined within the database


if __name__ == '__main__':
    try:
        sequence_manager = SequenceManager()
        sequence_manager.set_eois_id('A000001')
        print(sequence_manager.verify_number('1'))
    finally:
        sequence_manager.close_connection()
