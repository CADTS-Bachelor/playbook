#date 2017-1-8
#author bird

import re
import datetime
import sqlite3
import sys

conn = sqlite3.connect(sys.argv[2])
cur = conn.cursor()
createtb_sql = """CREATE TABLE log (
	id INTEGER AUTO_INCREMENT,
	s_datetime DATETIME,
	site_name VARCHAR(255),
	site_ip VARCHAR(255),
	http_method VARCHAR(32),
	uri_path VARCHAR(1024),
	site_port INTETER,
	client_ip VARCHAR(255),
	user_agent VARCHAR(255),
	http_code INTEGER
);"""
cur.execute(createtb_sql)

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

i = 1
a2 = re.compile('[0-9-\s:]+')
a3 = re.compile('[A-Z]+[A-Z0-9]+')
a4 = re.compile('([0-9]+\.){3}[0-9]+')
a5 = re.compile('GET|POST|HEAD')
a6 = re.compile('(?<= /)[\/\.a-zA-Z0-9]+(?= -)')
a7 = re.compile('(?<=- )[0-9]+(?= -)')
a8 = re.compile('(?<=- )([0-9]+\.){3}[0-9]+')
a9 = re.compile('Mozilla.+?(?=\s)')
a10 = re.compile('(?<=\s)[0-9]+(?=\s[0-9]+\s[0-9]+)')
for line in lines :
    try :
        id = i
        s_datetime = a2.search(line).group(0)
        site_name = a3.search(line).group(0)
        site_ip = a4.search(line).group(0)
        http_method = a5.search(line).group(0)
        uri_path = a6.search(line).group(0)
        site_port = a7.search(line).group(0)
        client_ip = a8.search(line).group(0)
        user_agent = a9.search(line).group(0)
        http_code = a10.search(line).group(0)
        insert_sql = 'insert into log values(?,?,?,?,?,?,?,?,?,?)'
        vals = [id, s_datetime, site_name, site_ip, http_method, uri_path, site_port, client_ip, user_agent, http_code]
        cur.execute(insert_sql, vals)
        i = i + 1
    except :
        continue
conn.commit()

cur.close()
conn.close()
