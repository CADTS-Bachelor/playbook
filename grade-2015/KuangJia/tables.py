# encoding:utf8
# Python使用ORM框架操作数据库
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Scene(Base):
    __tablename__ = 'scene'      # 表名

    id = Column(Integer, primary_key=True)      # 表结构
    name = Column(String(20), unique=True)
    create_time = Column(DateTime())
    destory_time = Column(DateTime())

# 初始化数据库连接:('数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名)
engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/test')
DB_Session = sessionmaker(bind = engine)  # 创建DBSession类型:

# 增
session = DB_Session()  # 创建session对象:
scene = Scene(id=1, name = 'xilming', create_time = '2015-12-21 12:20:21',destory_time = '2015-12-21 12:20:54')  # 创建新Scene对象:
session.add(scene)  # 添加到session:
session.commit()  # 提交即保存到数据库:
session.close()  # 关闭session:

# 查,  destory_time = '2015-12-21 12:20:54'
session = DB_Session()
scene_info = session.query(Scene).filter(Scene.id == 1).one()
print(scene_info.name)
session.close()
'''# 改
session = DB_Session()
session.query(Scene).filter(Scene.id == 1).update({'name': 'xinxin'})
session.commit()
session.close()

# # 删
session = DB_Session()
session.query(Scene).filter(Scene.id == 1).delete()
session.commit()
session.close()
'''
