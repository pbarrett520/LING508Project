import mysql.connector

class MysqlRepository():

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'host': 'localhost',
            'database': 'ChinesePronunciations'
        }

        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()


    def get_entries(self):
        self.cursor.execute("SELECT * FROM Pronunciations;")
        entries = self.cursor.fetchall()
        print(entries)

        return entries