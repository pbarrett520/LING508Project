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


    def get_all_entries(self):
        self.cursor.execute("SELECT * FROM Pronunciations;")
        entries = self.cursor.fetchall()
        #print(entries)
        return entries

    def get_row(self, hanzi):
        query = "SELECT * FROM Pronunciations WHERE chinese_character = %s;"
        self.cursor.execute(query, (hanzi,))
        row = self.cursor.fetchone()
        #print(row)
        return row

    def get_pronunciation(self, hanzi, dialect):
        valid_dialects = ['Mandarin', 'Cantonese', 'Hakka', 'Wu', 'Xiang', 'MinNan', 'Jin', 'Gan']
        if dialect not in valid_dialects:
            raise ValueError(f"Invalid dialect: {dialect}")

        query = f"SELECT {dialect} FROM Pronunciations WHERE chinese_character = %s;"
        self.cursor.execute(query, (hanzi,))
        result = self.cursor.fetchone()

        if result is None:
            return None
        else:
            return result[0]

