import sqlite3
import xml.dom.minidom as minidom

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Guests")
rows = cursor.fetchall()

doc = minidom.Document()
guests = doc.createElement("guests")
doc.appendChild(guests)

for row in rows:
    guest = doc.createElement("guest")
    guests.appendChild(guest)

    guest_id = doc.createElement("id")
    guest_id.appendChild(doc.createTextNode(str(row[0])))
    guest.appendChild(guest_id)

    name = doc.createElement("name")
    name.appendChild(doc.createTextNode(str(row[1])))
    guest.appendChild(name)

    email = doc.createElement("email")
    email.appendChild(doc.createTextNode(str(row[2]))) 
    guest.appendChild(email)

with open("guests.xml", "w", encoding="utf-8") as f:
    doc.writexml(f, indent="\t", newl="\n", addindent="\t", encoding="utf-8")

conn.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')
