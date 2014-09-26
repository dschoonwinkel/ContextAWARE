import sqlite3
import pandas.io.sql as sql
import os

file_list = list()

for root, dirs, files in os.walk("./dbs"):
    for file in files:
        if file.endswith(".db"):
             file_list.append(file)

print file_list

for filename in file_list:
	table_name = filename.rstrip('.db')
	print 'Working on: ' + table_name
	con = sqlite3.connect('./dbs/' + filename)
	table = sql.read_sql('select * from %s' % table_name, con)
	table.to_csv('./csv/%s.csv' % table_name)
