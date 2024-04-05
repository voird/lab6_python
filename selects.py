import sqlite3

conn = sqlite3.connect('hotel.db')
cur = conn.cursor()

cur.execute("SELECT Payments.payment_date, Bookings.check_in_date, Bookings.check_out_date, Services.service_name, Payments.amount FROM Payments INNER JOIN Bookings ON Payments.booking_id = Bookings.booking_id INNER JOIN Services ON Payments.service_id = Services.service_id")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("SELECT Bookings.check_in_date, Bookings.check_out_date, Guests.name AS guest_name, Guests.email AS guest_email, Rooms.room_number, Rooms.room_type FROM Bookings INNER JOIN Guests ON Bookings.guest_id = Guests.guest_id INNER JOIN Rooms ON Bookings.room_number = Rooms.room_number")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("""
    SELECT Employees.name AS employee_name, Bookings.room_number
    FROM Employees
    INNER JOIN Bookings ON Employees.employee_id = Bookings.employee_id
""")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("""
    SELECT * 
    FROM Guests
""")
rows = cur.fetchall()

for row in rows:
    print(row)    
    
conn.close()
