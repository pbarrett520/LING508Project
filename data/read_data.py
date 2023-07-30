# This also has some issues. Has trouble parsing cetain entries in the .txt file that ostensibly seems correct. Only 8 data points successfully added to db, many are incomplete. Need more time to debug.
import mysql.connector

config = {
    'user': 'root',
    'host': 'localhost',
    'database': 'ChinesePronunciations'
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
# Clear data so we don't append duplicates while testing
cursor.execute("DELETE FROM Pronunciations")

insert_query = """
INSERT INTO Pronunciations 
(chinese_character, Mandarin, Cantonese, Hakka, Wu, Xiang, MinNan, Jin, Gan) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Read the file and insert data
with open('pronunciations1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 10):
        chinese_character = lines[i].strip().replace(':', '')

        # Check if the first line of the block is a single character for debugging
        if len(chinese_character) != 1:
            print(f"Unexpected character length for: {chinese_character}. Skipping...")
            continue

        pronunciations = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in lines[i + 1:i + 9] if
                          ':' in line}     # My intuition is that this dictionary comprehension may be problematic and causing issues

        record = (
            chinese_character,
            pronunciations.get('Mandarin', None),
            pronunciations.get('Cantonese', None),
            pronunciations.get('Hakka', None),
            pronunciations.get('Wu', None),
            pronunciations.get('Xiang', None),
            pronunciations.get('Min Nan', None),
            pronunciations.get('Jin', None),
            pronunciations.get('Gan', None)
        )

        try:    # for debugging
            cursor.execute(insert_query, record)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Failed record: {record}")

# Commit the changes and close the connection
cnx.commit()

cursor.execute("SELECT * FROM Pronunciations;")
entries = cursor.fetchall()
print(entries)
print(len(entries))

cursor.close()
cnx.close()
