import pymysql

class OperationDatabase():
    #连接mysql的参数
    def __init__(self,Ip,User,PassWd,DBname):
        self.ip=Ip
        self.user=User
        self.passwd=PassWd
        self.dbname=DBname
    #连接mysql
    def ConnectDatabase(self):
        self.db = pymysql.connect(self.ip,self.user,self.passwd,self.dbname)
        self.cursor = self.db.cursor()
    #查询
    def SelectDatabase(self,sql):
        self.ConnectDatabase()

        result=()
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchall()#获取全部数据
        except:
            print("查询失败")
        return result

        self.CloseDataBase()

    def SelectDatabase_Row(self,sql):
        self.ConnectDatabase()

        result=None
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchone()#获取单条数据
            #print(result)
        except:
            print("查询失败")
        return result

        self.CloseDataBase()
    #插入
    def InsertDatabase(self,sql):
        return self.__edit(sql)
    #修改
    def UpdateDatabase(self,sql):
        return self.__edit(sql)
    #删除
    def DeleteDatabase(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        self.ConnectDatabase()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print("提交失败")
            self.db.rollback()

        self.CloseDataBase()
    #关闭数据库
    def CloseDataBase(self):
        self.cursor.close()
        self.db.close()

#例如
sql="SELECT * from db_p2p.t_users_info where id=6214771006504961;"
c=OperationDatabase("数据库服务器ip", "用户名", "密码", "数据库名字")
c.SelectDatabase(sql)