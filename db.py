import sqlite3

conn = sqlite3.connect('hotel.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                room_number INTEGER PRIMARY KEY,
                room_type TEXT,
                rate REAL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Guests (
                guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_id INTEGER,
                room_number INTEGER,
                check_in_date DATE,
                check_out_date DATE,
                employee_id INTEGER,
                FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
                FOREIGN KEY (room_number) REFERENCES Rooms(room_number),
                FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Services (
                service_id INTEGER PRIMARY KEY,
                service_name TEXT,
                price REAL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER,
                service_id INTEGER,
                amount REAL,
                payment_date DATE,
                FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),
                FOREIGN KEY (service_id) REFERENCES Services(service_id)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                salary REAL
            )''')

conn.commit()
conn.close()
