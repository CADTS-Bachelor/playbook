# 规则

- 每个人创建一个以自己名字命名的目录，例如张萌对应的目录就是ZhangMeng；
- 个人的所有代码都放到对应的目录下。

## 注意事项

- 每个脚本不要在运行后通过raw_input()或input()等控制台输入函数接受输入，而应该通过sys.argv获取命令行传入的参数；如果命令行参数不符合预期则直接输入错误然后使用sys.exit(1)退出程序即可。

## 任务

### 01. 单词计数

发布时间：2016年12月07日

#### 要求
输入任一个英文的纯文本文件，统计其中的单词出现的个数，效果是执行脚本count.py \<txt\_file\>，输出若干行，每一行是单词及其出现次数，输出顺序按次数从大到小、相同的按单词字典序排列。

### 02. 解析日志文件

发布时间：2016年12月22日

#### 要求

parse\_log.py \<log\_file\> \<sqlite_file\>

文件主要包含2个函数，一个是日志解析函数，一个是数据库存储函数。

```python
def parse_log(log_filename):
	result = []
	with open(log_filename, 'r') as f:
		for line in f:
			log_entry = PARSE(line)
			result.append(log_entry)
	return result
	
	
def save_log_sqlite3(entries, db_filename):
	# create tables if not exists
	# insert log entries
	
	
def __name__ == '__main__':
	import sys
	if len(sys.argv) != 3:
		print('USAGE: {0} <LOG_FILE> <DB_FILE>'.format(sys.argv[0]))
		sys.exit(1)
		
	log_entries = parse_log(sys.argv[1])
	save_log_sqlite3(log_entries, sys.argv[2])
```

解析文件“data/ex150618.log”文件，识别出里面的发生时间（日期+时间，解析为datetime类型）、网站名称、网站IP、HTTP METHOD、URI路径、网站端口（解析为int）、客户端IP、客户端User-Agent（可以先解析为字符串）、返回的HTTP CODE。每条记录一个对象，类定义大致如下：

```python
class LogEntry:
	def __init__(self, t, site_name, site_ip, ...):
		self.t = t
		self.site_name = site_name
		# ...
```

存储解析好的日志条目到Sqlite3数据库，数据库表定义如下：

```sql
CREATE TABLE log (
	id INTEGER AUTO_INCREMENT;
	s_datetime DATETIME;
	site_name VARCHAR(255);
	site_ip VARCHAR(255);
	http_method VARCHAR(32);
	uri_path VARCHAR(1024);
	site_port INTETER;
	client_ip VARCHAR(255);
	user_agent VARCHAR(255);
	http_code INTEGER;
);
```

## 检查脚本

- checkers/check_count.py: 检查脚本count.py的运行时间，其中第一个是李睿写的参考实现。
