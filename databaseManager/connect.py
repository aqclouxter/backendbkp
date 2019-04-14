import mysql.connector

print("starting...")

mydb = mysql.connector.connect(
  host="192.168.33.1",
  user="alejandro",
  passwd="Sunshine3",
  database="CPA",
  port=3360,
  buffered=True
)