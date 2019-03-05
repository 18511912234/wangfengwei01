import requests,MySQLdb,re,time

#卖家订单发货流程接口


HOSTNAME = '192.168.215.55'
#读取禅道中的测试用例
def readSQLcase():
    sql = "select * from zt_case......................"
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        interfaceTest(case_list)
    coon.commit()
    cursor.close()
    coon.close()

#循环读取接口测试用例
def interfaceTest(case_list):
    res_flags = []
    request_url = []
    responses = []

    #判断参数中如果有('{storename}')，则在代码中取值，对应作为整个店铺名称
    storenameinfo = re.compile('{storename}')

    #作为预提交订单号
    preorderinfo = re.compile('{preOrderSN}')

    #作为订单编号
    orderinfo = re.compile('{ordersn}')

    #作为交易号
    tradeinfo=re.compile('{tradeno}')

    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[3]
            param = case[2]
            url = case[5]
            res_check = case[4]
        except Exception:
            return "用例格式不正确"
        #判断测试为空或null
        if param=='' or param=='null':
            new_url = "http://" + HOSTNAME + url
        else:
            #如果有动态关联参数'{storename}'，返回传给店铺名称
            param=storenameinfo.sub('{storename}',param)
            #传给预提交订单号
            param=preorderinfo.sub('{preOrderSN}',param)
            #传给订单号
            param=orderinfo.sub('{ordersn}',param)
            #传给交易号
            param=tradeinfo.sub('{tradeno}',param)

            #如果接口有参数,接口url设置为hostname+url+param
            new_url = "http://" + HOSTNAME + url + '?' + urlParam(param)
            #把接口url添加到列表
            request_url.append(new_url)

        #如果是get请求则读取get请求和反回值，否则当作post请求处理
        if method.upper()=="GET":
            print(str(case_id) + new_url)
            # 设置请求头
            headers = {'host': HOSTNAME,
                       'Connection': 'keep-alive',
                       'token': token,
                       'Content_type': 'application/json',
                       'User-Agent': 'Apache-HttpClient/4.2.6(java1.5)'
                       }

            data = None
            results=requests.get(url=url,data=data,headers=headers).text
            responses.append(results)

            #
            res=readRes(results,res_check)
            #校验请求的返回数据
            print(results)
            if "pass"==res:
                #写结果为pass并关联到用例id
                writeResult(case_id, 'pass')
                #如果结果为pass，则变更订单状态
                modifyOrderStatus('{tradeno}')

                #如果结果为pass，则变更订单状态2
                modifyOrderStatus2('{tradeno}')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)
        #如果不是get就读取post请求和响应
        else:
            print(str(case_id) + new_url)

            headers = {'host': HOSTNAME,
                       'Connection': 'keep-alive',
                       'token': token,
                       'Content_type': 'application/json',
                       'User-Agent': 'Apache-HttpClient/4.2.6(java1.5)'
                       }

            data = None
            results = requests.get(url=url, data=data, headers=headers).text

            #发送post请求，得到响应数据
            responses.append(results)
            res=readRes(results,res_check)
            print(results)

            if "pass"==res:
                writeResult(case_id,"pass")
                res_flags.append("pass")
            else:
                res_flags.append("fail")
                writeResult(case_id,"fail")

                #如果接口响应异常，用这种方法处理bug
                if reserror(results):
                    writeBug(case_id, interface_name, new_url, "接口响应错误", res_check)
                else:
                    writeBug(case_id, interface_name, new_url, results, res_check)

            #分别获取token，订单编号，交易编号并分别作为参数传递
            try:
                GetToken.token(results)
            except:
                print("ok1")
            try:
                preOrderSN(results)
            except:
                print("ok2")
            try:
                ordersn(results)
            except:
                print("ok3")
            try:
                tradeno(results)
            except:
                print("ok4")

#参数值的替换方法
def urlParam(param):
    param1 = param.replace('*', '&')
    return param1.replace('&quot;', '\"')

#校验结果是否一致的方法
def readRes(res,res_check):
    res = res.replace("':'", "=").replace("':',", "=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return "返回参数与预期结果不一致"
    return 'pass'

#获取登陆接口中的token值
def token(results):
    global token
    regx='.*"token":"(.*)","ud"'
    pm=re.search(regx,results)
    if pm:
        token=pm.group(1).encode("utf-8")
        print(token)
        return True
    return False

#获取预提交订单号方法
def preOrderSN(results):
    global preOrderSN
    regx = '.*"preOrderSN":"(.*)","toHome"'
    pm = re.search(regx, results)
    if pm:
        preOrderSN = pm.group(1).encode("utf-8")
        return preOrderSN
    return False

#获取订单号方法
def ordersn(results):
    global ordersn
    regx = '.*"tradeNo":"(.*)"}'
    pm = re.search(regx, results)
    if pm:
        ordersn = pm.group(1).encode("utf-8")
        return ordersn
    return False

#获取交易号方法
def tradeno(results):
    global tradeno
    regx = '.*"brief":"(.*)"tradeno":"2016'
    pm = re.search(regx, results)
    if pm:
        tradeno = pm.group(1).encode("utf-8")
        return tradeno
    return False

#根据交易号，修改数据库的值
def modifyOrderStatus(tradeno):
    sql='update t_order set order_status=20,sync_step=10 where order_sn=%s;'
    param=tradeno
    coon = MySQLdb.connect(user='root', passwd='123456', db='trade', port='18806', host='192.168.21.22',charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql,param)
    coon.commit()
    cursor.close()
    coon.close()


def modifyOrderStatus2(tradeno):
    sql = 'update t_order set order_status=30,sync_step=10 where order_sn=%s;'
    param = tradeno
    coon = MySQLdb.connect(user='root', passwd='123456', db='trade', port='18806', host='192.168.21.22', charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql,param)
    coon.commit()
    cursor.close()
    coon.close()


def reserror(results):
    global html
    regx = 'html'
    pm = re.search(regx, results)
    if pm:
        return regx
    return False

#防止店铺名称重复，设置动态参数
def storename(param):
    global storename
    storename='test'+str(time.time())
    return storename

def writeResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "update zt_testrun set value1=value2 where .."
    param = (result, now, case_id)
    print(result)
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql, param)
    coon.commit()
    cursor.close()
    coon.close()


def writeBug(bug_id, interface_name, request,response, res_check):
    interface_name = interface_name.encode('utf-8')
    res_check = res_check.encode('utf-8')
    response = response.encode('utf-8')
    request = request.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    bug_title = str(bug_id) + '_' + interface_name + '_错误'
    step = '[请求报文]' + request + '<br/>' + '[预期结果]' + res_check + '<br/>' + '[响应报文]' + response

    # 写bug操作步骤到数据库
    sql = 'insert into zt_bug values('');' % (now, now, now, bug_title, step, now, now)
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.215.55',
                           charset='utf8')
    cursor = coon.cursor()
    cursor.execute(sql)
    coon.commit()
    cursor.close()
    coon.close()

 #把token定义静态方法，如果正则匹配到返回token
class GetToken(object):
    @staticmethod
    def token(results):
        global token
        regx = '.*"token":"(.*)","ud"'
        pm = re.search(regx, results)
        if pm:
            token = pm.group(1).encode("utf-8")
            print(token)
            return True
        return False

if __name__ == '__main__':
    readSQLcase()
    print("Done")
    time.sleep()

