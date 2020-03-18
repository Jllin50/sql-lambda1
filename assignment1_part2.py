import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

DB_FILEPATH = 'buddymove_holidayiq.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)

# df.to_sql('review', connection)

cursor = connection.cursor()
query = '''SELECT COUNT(*) FROM review'''
result = cursor.execute(query).fetchall()
print('Total number of rows:')
print(result[0][0])
print()