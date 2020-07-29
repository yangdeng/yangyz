"""
数据库处理模块
思路：
将数据库操作封装成一个类
"""
import pymysql
import hashlib

SALT = "#&Aid_" # 盐

class Database:
    def __init__(self,host='localhost',port=3306,
                 user='root',passwd='123456',charset='utf8',databas=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = databas
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host=self.host,port=self.port,user=self.user,
                                  passwd=self.passwd,database=self.database,charset=self.charset)

    def close(self):
        self.db.close()

    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select * from user where name='%s'"%name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False

        hash1 = hashlib.md5((name + SALT).encode())#加盐
        hash1.update(passwd.encode()) #算法加密
        passwd = hash1.hexdigest() #加密后的密码

        sql = "insert into user (name,passwd) values(%s,%s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return  True
        except Exception:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        hash1 = hashlib.md5((name + SALT).encode())  # 加盐
        hash1.update(passwd.encode())  # 算法加密
        passwd = hash1.hexdigest()  # 加密后的密码

        sql = "select * from where name='%s' and passwd='%s'"%(name,passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    #查单词
    def query(self,word):
        sql = "select mean from words where word = '%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]

    #插入历史记录
    def insert_hist(self,name,word):
        sql = "insert into hist (name,word) values(%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    #历史记录查询
    def history(self,name):
        sql = "select name,word,time from hist where name = '%s' order by time desc limit 10"% name
        self.cur.execute(sql)
        return self.cur.fetchall()






















