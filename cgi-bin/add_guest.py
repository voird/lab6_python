import cgi
import sqlite3

form = cgi.FieldStorage()

name = form.getfirst("name")
email = form.getfirst("email")

db = sqlite3.connect("hotel.db")
cur = db.cursor()
if(all((name, email))):
    in_data = f"INSERT INTO Guests (name, email) VALUES ('{name}','{email}')"
    cur.execute(in_data)
    db.commit()

db.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')