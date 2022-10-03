import serial
import MySQLdb
import time

# This function takes in a string and removes whitespace from it.
def rmspace(string):
    return string.replace(" ", "\n") # Use replace function to replace whitespaces with nothing.

host = "localhost"
dbname = "temperaturedb"
user = "root"
pwd = ""
s_port = 'COM5'

db = MySQLdb.connect(host,user,pwd,dbname) or die("Not connected!")

try:
	print("Connecting on port...", s_port)
	a = serial.Serial('COM5', 9600)
	print("Connected on port", s_port)
except Exception as e:
	print(e)

while True:
	try:
		cursor = db.cursor()
		time.sleep(2)

		data = a.readline()
		d_s = data.decode('utf-8')
		d_s = d_s.split(" ")
		humidity = d_s[0]
		temp = d_s[1]
		try:
			cursor.execute("INSERT INTO readings VALUES (DEFAULT, DEFAULT, %s, %s)", (humidity, temp))
			db.commit()
			cursor.close()
		except MySQLdb.IntegrityError:
			print("Insert failed!")
		finally:
			cursor.close()
	except Exception as e:
		print(e)