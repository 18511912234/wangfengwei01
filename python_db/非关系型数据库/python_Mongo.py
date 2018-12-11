from pymongo import MongoClient

#连接数据库
conn=MongoClient("localhost",27017)

#连接数据库 mydb 是自己定义的数据库名字
db=conn.mydb

#获取集合 students是自己创建的集合名字
collection=db.students

#增加一个文档
#collection.insert({"name":"王凤伟","age":28,"address":"北京市昌平区","isDelete":0})
#添加多个文档
#collection.insert([{"name":"关晓彤","age":28,"address":"北京市昌平区","isDelete":0},{"name":"范冰冰","age":28,"address":"北京市昌平区","isDelete":0}])

#查询文档
#1.查询年龄大于18的人
# res=collection.find({"age":{"$gt":18}})
# for i in res:
#     print(i)

#2.查询所有文档
# res=collection.find()
# for i in res:
#     print(i)
#3.查询年龄大于18的有多少个,统计查询
#res=collection.find({"age":{"$gt":18}}).count()

#4.根据id查询 要引入这个包
#form bson.objectid import ObjectId
#res=collection.find({"__id":ObjectId("ID值")})

#5.排序
import pymongo
#res=collection.find().sort("age",pymongo.DESCENDING) #降序
# res=collection.find().sort("age",1) #升序
# for i in res:
#     print(i)

#6.分页查询,跳过2条取2条
# res=collection.find().skip(2).limit(2)
# for i in res:
#     print(i)

#更新文档,把名字是王凤伟的年龄设置成23
#collection.update({"name":"王凤伟"},{"$set":{"age":23}})

#删除,不写条件全部删除
#collection.remove({"name":"王凤伟"})

#断开
conn.close()