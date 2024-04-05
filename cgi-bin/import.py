#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import xml.dom.minidom as minidom
import sqlite3
import os

print("Content-type: text/html\n")

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

def get_text(node):
    text = ""
    for child in node.childNodes:
        if child.nodeType == child.TEXT_NODE:
            text += child.data
    return text.strip()

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "guests.xml")

try:
    doc = minidom.parse(file_path)
    guests = doc.getElementsByTagName('guest')
    for guest in guests:
        name = get_text(guest.getElementsByTagName('name')[0])
        email = get_text(guest.getElementsByTagName('email')[0])
        cursor.execute("INSERT INTO Guests (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("<p>Данные успешно импортированы в базу данных.</p>")
except Exception as e:
    print('<script>alert("Ошибка при импорте данных из XML: {}");</script>'.format(str(e)))

conn.close()

print('<meta http-equiv="refresh" content="0; url=/index.html">')
