import redis

#一些命令这里找：http://redis.cn/commands.html

#连接redis服务器
connect=redis.StrictRedis(host="localhost",port=6379,password="wangfengwei")

#方法1,g根据数据类型的不同，调用相应的方法
#写
connect.set("key1","value1")
#读
res=connect.get("key1")
print(res)

#方法2
#写 pipline： 缓冲多条命令，然后依次执行，可以有效减少服务器到客户端的TCP数据包
pipe=connect.pipeline()
pipe.set("key1","value1")
pipe.set("key2","value2")
pipe.set("key3","value3")
#这样才是真正的写进数据库里面
pipe.execute()
