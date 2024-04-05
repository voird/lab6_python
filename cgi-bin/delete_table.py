#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import sqlite3
import os

print("Content-type: text/html\n")

# Подключение к базе данных
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM Guests")

conn.commit()
conn.close()

print('<p>Таблица Guests успешно очищена.</p>')
print('<meta http-equiv="refresh" content="0; url=/index.html">')
