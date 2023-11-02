import mysql.connector

config = {
    'user': 'root',
    'password': 'Bertinho123321+',
    'host': 'localhost',
    'charset': 'utf8',
    'database': 'crash_course'
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

try:
    if db.is_connected():
        print('OK')
except mysql.connector.Error as err:
    print(f'Bad {err}')