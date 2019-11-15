import pymysql #首先需要安装好pymysql模块
# 打开数据库连接
# db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# cursor=db.cursor()
# var=cursor.execute("select version()")
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
# db.close()
# db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# #获取游标
# cursor=db.cursor()
# #创建表
# sql="""create table user(
#         id bigint not null,
#         username varchar(100),
#         password varchar(30)
#
#     );"""
# cursor.execute(sql)
# db.close()
# db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# cursor = db.cursor();
# sql = """
#     insert into user values(2,"lisi","123456")
#     """
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount)
# db.close()
# db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# cursor=db.cursor()
# # sql="insert into user(id,username,password) " \
# #     "values(%s,%s,%s)" %  \
# #     (5,"joinx","234556")
# sql = "INSERT INTO user(id, \
#        username, password) \
#        VALUES (%s, %s, %s)" % \
#        (5,"username","234556")
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount)
# db.close()
#查询语句
# db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# cursor=db.cursor()
# sql="""select * from user"""
# cursor.execute(sql)
# results=cursor.fetchall()
# for query in results:
#     id=query[0]
#     username=query[1]
#     password=query[2]
#     print(id,username,password)
# db.close()
# import pymysql
# #
# # # 打开数据库连接
# # db = pymysql.connect("localhost", "root", "root", "pythontest", charset='utf8' )
# #
# # # 使用cursor()方法获取操作游标
# # cursor = db.cursor()
# #
# # # SQL 删除语句
# # sql = "DELETE FROM user WHERE id = %s" % (1)
# # try:
# #    print(sql)
# #    # 执行SQL语句
# #    cursor.execute(sql)
# #    # 提交修改
# #    db.commit()
# # except:
# #    # 发生错误时回滚
# #    print("有错误")
# #    db.rollback()
# #
# # # 关闭连接
# # db.close()
import pymysql

# 打开数据库连接
db = pymysql.connect("120.27.13.123", "root", "joinx-yang", "joinx", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句  %s 为varchar %c 为int or char
sql =  "UPDATE test SET password =1  WHERE username = '%s'" % ('yangyunnuo')
# print(sql)
# # 执行SQL语句
# cursor.execute(sql)
# # 提交修改
# db.commit()
try:
   print(sql)
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   print("有错误")
   db.rollback()

# 关闭连接
db.close()