import re
import sys
import sqlite3

#conn = sqlite3.connect('test.db')
#print "Opened database successfully";

#conn.execute('''CREATE TABLE log
#         (id INTEGER AUTO_INCREMENT,
#         s_datatime DATETIME,
#         site_name VARCHAR(255),
#         site_ip VARCHAR(255),
#         http_method VARCHAR(32),
#         uri_path VARCHAR(1024),
#         site_port INTEGER,
#         client_ip VARCHAR(255),
#         user_agent VARCHAR(255),
#         http_code INTEGER
#         );''')
#print "Table created successfully";

#conn.close()

conn = sqlite3.connect('test.db')
i = 0
f = open("ex150618.log","r")
lines = f.readlines()
for line in lines:
    if line.startswith('#'):
        continue
    t = []
    i += 1
    t.append(i)
    time = re.compile(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}')
    time = time.findall(line)
    t.append(time[0])

    sitename = re.compile(r'[\(A-Z)\d\(A-Z)\(A-Z)\(A-Z)]{5}\d')
    sitename = sitename.findall(line)
    t.append(sitename[0])

    ipaddress = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    ipaddress = ipaddress.findall(line)
    ip1 = ipaddress[0]
    ip2 = ipaddress[1]
    t.append(ipaddress[0])

    httpmethod = re.compile(r'[GET]{3}|[POST]{4}|[HEAD]{4}|[TRACE]{5}|[PUT]{3}|[DELETE]{6}|[OPTIONS]{7}|[CONNECT]{7}')
    httpmethod = httpmethod.findall(line)
    t.append(httpmethod[0])

    uripath = re.compile(r'\/\w+[.]+\S+[a-z A-Z]')
    uripath = uripath.findall(line)
    path = uripath[0]
    agent = uripath[1]
    t.append(uripath[0])

    siteport = re.compile(r'\s\d{2}\s')
    siteport = siteport.findall(line)
    t.append(siteport[0])
    t.append(ipaddress[1])
    t.append(uripath[1])

    httpcode = re.compile(r'\s\d{3}\s')
    httpcode = httpcode.findall(line)
    t.append(httpcode[0])
    m = tuple(t)
    print m
    conn.execute("insert into log values (?,?,?,?,?,?,?,?,?,?)",m)
    conn.commit()


