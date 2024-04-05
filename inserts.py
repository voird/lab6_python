import sqlite3

conn = sqlite3.connect('hotel.db')
cur = conn.cursor()

rooms_data = [
    (101, 'Стандартный', 100.00),
    (102, 'Стандартный', 100.00),
    (103, 'Делюкс', 150.00),
    (104, 'Делюкс', 150.00)
]
cur.executemany("INSERT OR REPLACE INTO Rooms (room_number, room_type, rate) VALUES (?, ?, ?)", rooms_data)

guests_data = [
    ('Доктор Рацио', 'drgenious@example.com'),
    ('Вергилий', 'iamastormthatisapproaching@example.com'),
    ('Данте', 'devilmaycry@example.com')
]
cur.executemany("INSERT OR REPLACE INTO Guests (name, email) VALUES (?, ?)", guests_data)


bookings_data = [
    (1, 1, 101, '2024-04-01', '2024-04-05', 1),
    (2, 2, 103, '2024-04-02', '2024-04-04', 2),
    (3, 3, 102, '2024-04-03', '2024-04-06', 1)
]
cur.executemany("INSERT OR REPLACE INTO Bookings (booking_id, guest_id, room_number, check_in_date, check_out_date, employee_id) VALUES (?, ?, ?, ?, ?, ?)", bookings_data)

services_data = [
    ('Завтрак', 10.00),
    ('Ужин', 20.00),
    ('Бассейн и сауна', 15.00)
]
cur.executemany("INSERT OR REPLACE INTO Services (service_name, price) VALUES (?, ?)", services_data)

payments_data = [
    (1, 1, 40.00, '2024-04-01'),
    (1, 3, 30.00, '2024-04-03'),
    (2, 2, 40.00, '2024-04-02')
]
cur.executemany("INSERT OR REPLACE INTO Payments (booking_id, service_id, amount, payment_date) VALUES (?, ?, ?, ?)", payments_data)

employees_data = [
    ('Андрей Дьяченко', 'Администратор', 2000.00),
    ('Артем Прасол', 'Менеджер', 1500.00),
    ('Дмитрий Дементьев', 'Официант', 1800.00),
    ('Даниил Некрасов', 'белл-бой', 1800.00)
]
cur.executemany("INSERT OR REPLACE INTO Employees (name, position, salary) VALUES (?, ?, ?)", employees_data)

conn.commit()
conn.close()
