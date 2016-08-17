import sqlite3 as lite
from datetime import date
import sys

conn = None
cursor = None
database = 'myrtle.db'


def open_connection():
	global cursor, conn, cursor
	print "Opening connection to {}".format(database);
	conn = lite.connect(database)
	conn.row_factory = lite.Row
	cursor = conn.cursor()


def close_connection():
	global conn
	conn.close()


def add_entry(hooker, hookee, reason):
	current_year = str(date.timetuple(date.today())[0])
	cursor.execute('INSERT INTO hookups VALUES (NULL, ?, ?, ?, ?)', (hooker, hookee, reason, current_year))
	conn.commit()


def get_current_list():
	currentyear = str(date.timetuple(date.today())[0])
	cursor.execute('SELECT * from hookups WHERE year=?', (currentyear,))
	results = cursor.fetchall()
	ret_json = []
	for row in results:
		item = {}
		item['hooker'] = row['hooker']
		item['hookee'] = row['hookee']
		item['why'] = row['reason']
		ret_json.append(item)
	return ret_json


if __name__=='__main__':
	open_connection()
	for item in get_current_list():
		print item
	close_connection()
