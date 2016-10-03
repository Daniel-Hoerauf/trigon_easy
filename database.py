import psycopg2
from datetime import date

conn = None
cursor = None


def initialize_db():
    global conn, cursor
    conn = psycopg2.connect(database='postgres',
                            user='postgres',
                            host='db',
                            port=5432
                            )
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS myrtle (
                    ID SERIAL PRIMARY KEY,
                    give text NOT NULL,
                    get text NOT NULL,
                    reason text NOT NULL,
                    year integer
                   )
                   """
                   )


def disconnect_db():
    global conn
    conn.close()


def add_entry(hooker, hookee, reason):
    current_year = str(date.timetuple(date.today())[0])
    cursor.execute('INSERT INTO myrtle (give, get, reason, year) VALUES (%s, %s, %s, %s)', (hooker, hookee, reason, current_year))
    conn.commit()


def get_current_list():
    currentyear = str(date.timetuple(date.today())[0])
    cursor.execute('SELECT * from myrtle WHERE year=%s', (currentyear,))
    results = cursor.fetchall()
    ret_json = []
    for row in results:
        item = {}
        item['hooker'] = row[1]
        item['hookee'] = row[2]
        item['why'] = row[3]
        ret_json.append(item)
    return ret_json


if __name__ == '__main__':
    initialize_db()
    add_entry('A', 'B', 'The Alphabet')
    for item in get_current_list():
        print(item)
