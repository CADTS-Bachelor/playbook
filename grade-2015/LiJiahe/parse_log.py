#IIS日志解析
#by hijack
#2017.1.6
'''解析文件“data/ex150618.log”文件，识别出里面的发生时间
（日期+时间，解析为datetime类型）、网站名称、网站IP、HTT
P METHOD、URI路径、网站端口（解析为int）、客户端IP、客户
端User-Agent（可以先解析为字符串）、返回的HTTP CODE
'''

import re
import sqlite3

class Logentry:
    def init(self,t,site_name,site_ip,http_method,uri_path,site_port,client_ip,ua,http_code):
        self.t = t
        self.site_name = site_name
        self.site_ip = site_ip
        self.http_method = http_method
        self.uri_path = uri_path
        self.site_port = site_port
        self.client_ip = client_ip
        self.ua = ua
        self.http_code = http_code

def parse(line):
    entry = Logentry()
    time = re.search('[^\s]+\s[^\s]+',line).group(0)
    name = re.search('[a-zA-z]+[0-9a-zA-Z]+',line).group(0)
    ip1 = re.search('([0-9]+\.)+[0-9]',line).group(0)
    method = re.search('GET|POST|HEAD',line).group(0)
    path = re.search('\/[^\s]+',line).group(0)
    port = re.search('(?<=\s)([0-9])+(?=\s)',line).group(0)
    ip2 = re.search('([0-9]+\.)+[0-9]{2}',line).group(0)
    ua = re.search('Mozilla.+?(?=\s)',line).group(0)
    code = re.search(r'((?<=\s)([0-9])+(?=\s[0-9]))',line).group(0)
    entry.init(time,name,ip1,method,path,port,ip2,ua,code)
    return entry

def parse_log(log_filename):
    result = []
    with open(log_filename,'r') as f:
        for line in f:
            try:
                log_entry = parse(line)
            except:
                continue
            result.append(log_entry)
    return result

def save_log_sqlite3(log_entries,db_filename):
    con = sqlite3.connect(db_filename)
    try:
        con.execute('''CREATE TABLE log (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	s_datetime DATETIME,
	site_name VARCHAR(255),
	site_ip VARCHAR(255),
	http_method VARCHAR(32),
	uri_path VARCHAR(1024),
	site_port INTETER,
	client_ip VARCHAR(255),
	user_agent VARCHAR(255),
	http_code INTETER);''');
    except:
        pass
    for i in log_entries:
        con.execute("INSERT INTO log VALUES (NULL,?,?,?,?,?,?,?,?,?)",(i.t,i.site_name,i.site_ip,i.http_method,i.uri_path,i.site_port,i.client_ip,i.ua,i.http_code));
    con.commit()
    con.close

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
	    print('USAGE: {0} <LOG_FILE> <DB_FILE>'.format(sys.argv[0]))
	    sys.exit(1)
    log_entries = parse_log(sys.argv[1])
    save_log_sqlite3(log_entries, sys.argv[2])






            
            
