import requests,re,xlrd,MySQLdb,time,sys

HOSTNAME = '192.168.215.55'

#卖家接口集合
def readSQLcase():
    sql = "select * from zt_case"
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        GetToken()
        interfaceTest(case_list)
    coon.commit()
    cursor.close()
    coon.close()


def GetToken():
    global token
    global token
    url = "http://" + HOSTNAME + 'buyer/user/login.do'
    params = {'phone': '18511912234',
              'pwd': '******'}
    request=requests.post(url=url,data=params,)
    response=request.text
    data=response.read()
    regx='.*"token":"(.*),"ud"'
    pm=re.search(regx,data)
    token=pm.group(1)

    regy=r'"state":(\d+)}'
    pn=re.search(regy,data)
    state=pn.group(1)
    if state=='0':
        return True
    return False

def interfaceTest(case_list):
    res_flags=[]
    request_url=[]
    responses=[]
    storenameinfo=re.compile('{storename}')#店铺名称
    storetagnameinfo=re.compile('{storetagname}')#标签名称
    deltagidinfo=re.compile('{deltagid}')#标签id
    deltagnameinfo=re.compile('{deltagname}')#标签名字

    for case in case_list:
        try:
            case_id=case[0]
            interface_name=case[1]
            method=case[3]
            param=case[2]
            url=case[5]
            res_check=case[4]
        except Exception:
            return "用例格式不正确"

        if param=="" or param=="null":
            new_url="http://"+HOSTNAME+url
        else:
            #如果有动态关联参数storename，则用值替换变量参数名，就是把返回值传给店铺名字
            param=storenameinfo.sub('{storename}',param)
            #如果有动态关联参数storetagname，则用值替换变量参数名，就是把返回值传给店铺标签
            param=storetagnameinfo.sub('{storetagname}',param)
            #
            param=deltagidinfo.sub('{deltagid}',param)
            #
            param=deltagnameinfo.sub('{deltagname}',param)
            #如果接口有参数，则url是这样的
            new_url = "http://" + HOSTNAME + url + '?' + urlParam(param)
            request_url.append(new_url)

        if method.upper=="GET":
            print(str(case_id) + new_url)
            # 设置请求头
            headers = {'host': HOSTNAME,
                       'Connection': 'keep-alive',
                       'token': token,
                       'Content_type': 'application/json',
                       'User-Agent': 'Apache-HttpClient/4.2.6(java1.5)'
                       }

            data=None
            # 发送请求并得到响应数据
            results = requests.get(url=new_url, data=data,headers=headers).text
            responses.append(results)

            # 调用判断响应的方法
            res = readRes(results, res_check)

            # 对返回数据进行校验
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)

        else:
            headers = {
                "host": HOSTNAME,
                "Connection": "keep-alive",
                "token": token,
                "Connect-Type": "application/json",
                "User-Agent": "Apache-HttpClient"
            }

            data = None
            results = requests.post(url=url, data=data, headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)
            print(results)

            if "pass" == res:
                writeResult(case_id, "pass")
                res_flags.append("pass")
                if JFIF(results):
                    results='JFIF ok'
                else:
                    print("接口名称:"+interface_name)
                    print("接口地址:"+new_url)
                    print("响应数据:"+results)
                    print(str(case_id)+'----------'+"sucess"+"----------")
                    continue
                print("接口名称:" + interface_name)
                print("接口地址:" + new_url)
                print("响应数据:" + results)
                print(str(case_id) + '----------' + "sucess" + "----------")

            else:
                res_flags.append("fail")
                writeResult(case_id, "fail")
                if reserror(results):
                    writeBug(case_id, interface_name, new_url, "接口响应错误", res_check)
                else:
                    writeBug(case_id, interface_name, new_url, results, res_check)
                print("接口名称:" + interface_name)
                print("接口地址:" + new_url)
                print("响应数据:" + results)
                print(str(case_id) + '----------' + "fail" + "----------")

#检验结果的方法（对响应数据进行断言）
def readRes(res,res_check):
    res=res.replace("':'","=").replace("':',","=")
    res_check=res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return "返回参数与预期结果不一致"
    return 'pass'

def urlParam(param):
    param1 = param.replace('*', '&')
    param2 = param.replace('&quot;', '\"')
    return param2.replace(';', '&')

#没有响应时的方法
def reserror(results):
    global html
    regx='html'
    pm=re.search(regx,results)
    if pm:
        return regx
    return False


#返回图片的方法
def JFIF(results):
    global JFIF
    regx= 'JFIF'
    pm = re.search(regx, results)
    if pm:
        return regx
    return False

#写测试结果到数据库
def writeResult(case_id,result):
    result=result.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    sql="update zt_testrun set value1=value2 where .."
    param=(result,now,case_id)
    print(result)
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql,param)
    coon.commit()
    cursor.close()
    coon.close()

#写bug到禅道
def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name=interface_name.encode('utf-8')
    res_check=res_check.encode('utf-8')
    response=response.encode('utf-8')
    request=request.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    bug_title=str(bug_id)+'_'+interface_name+'_错误'
    step='[请求报文]'+request+'<br/>'+'[预期结果]'+res_check+'<br/>'+'[响应报文]'+response

    #写bug操作步骤到数据库
    sql='insert into zt_bug values('');'%(now,now,now,bug_title,step,now,now)
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql)
    coon.commit()
    cursor.close()
    coon.close()

#动态店铺名
def storename(param):
    global storename
    storename='tstore'+str(int(time.time()))
    return storename
#店铺标签名字
def storetagname(param):
    global storetagname
    storetagname=".join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range()8])"
    return storetagname

def deltagid(param):
    sql="select id from t_tag_info where shopid=1000169 and status=1"
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        id_list = []
        id_list.append(ii)
    return str(id_list[0][0])
    coon.commit()
    cursor.close()
    coon.close()

def deltagname(param):
    sql="select tagname from t_tag_info where shopid=1000169 and  status=1"
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        name_list = []
        name_list.append(ii)
    return str(name_list[0][0])
    coon.commit()
    cursor.close()
    coon.close()

if __name__ == '__main__':
    readSQLcase()



