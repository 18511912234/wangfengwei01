#取消订单流程接口
import requests,re,xlrd,MySQLdb,time,sys

HOSTNAME = '192.168.215.55'


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


# 循环读取测试用例一次读取一条
def interfaceTest(case_list):
    res_flags = []
    request_url = []
    responses = []
    # 判断参数中如果有动态参数preOrderSN，则在代码中取值作为订单号
    strinfo = re.compile('{preOrderSN}')
    orderinfo = re.compile('{OrderSN}')

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

        if param == "" or param == "null":
            new_url = "http://" + HOSTNAME + url
        else:
            param = strinfo.sub(preOrderSN, param)
            param = orderinfo.sub(OrderSN, param)
            new_url = "http://" + HOSTNAME + url + '?' + urlParam(param)
            request_url.append(new_url)
        # 上面代码已经组装了新的url路径，接下来判断是post请求或get请求

        if method.upper == 'GET':
            print(str(case_id) + new_url)
            # 设置请求头
            headers = {'host': HOSTNAME,
                       'Connection': 'keep-alive',
                       'token': token,
                       'Content_type': 'application/json',
                       'User-Agent': 'Apache-HttpClient/4.2.6(java1.5)'
                       }

            # data=None
            # 发送请求并得到响应数据
            results = requests.get(url=new_url, headers=headers).text
            responses.append(results)

            # 调用判断响应的方法
            res = readRes(results, res_check)

            # 对返回数据进行校验
            print(results)
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)

        else:
            print(case_id) + '' + new_url
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

            else:
                res_flags.append("fail")
                writeResult(case_id, "fail")
                if reserror(results):
                    writeBug(case_id, interface_name, new_url, "接口响应错误", res_check)
                else:
                    writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                preOrderSN(results)
            except:
                print("ok")

            try:
                OrderSN(results)
            except:
                print("ok")


def readRes(res,res_check):
    res = res.replace("':'", "=").replace("':',", "=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return "返回参数与预期结果不一致"+str(s)
    return 'pass'

def urlParam(param):
    param1 = param.replace('*', '&')
    return param1.replace('&quot;', '\"')

def GetToken():
    global token
    url = "http://" + HOSTNAME + 'buyer/user/login.do'
    params = {'phone': '18511912234',
              'pwd': '******'}
    request = requests.get(url=url, data=params)
    response = request.text
    data = response.read()
    regx = '.*"token":"(.*)","ud"'

    pm = re.search(regx, data)
    token = pm.group(1)
    regy = r'"state":(\d+)}'
    pn = re.search(regy, data)
    state = pn.group(1)
    if state == '0':
        return True
    return False

#提交订单，参数取动态值
def preOrderSN(results):
    global preOrderSN
    regx='.*"preOrderSN":"(.*)","toHome"'
    pm=re.search(regx,results)
    if pm:
        preOrderSN=pm.group(1).encode("utf-8")
        return preOrderSN
    return False


#取消订单
def OrderSN(results):
    global OrderSN
    regx='.*"tradeNo":"(.*)"}'
    pm = re.search(regx, results)
    if pm:
        OrderSN = pm.group(1).encode("utf-8")
        return OrderSN
    return False


def reserror(results):
    global html
    regx = 'html'
    pm = re.search(regx, results)
    if pm:
        return regx
    return False

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

def writeBug(bug_id,interface_name,request,response,res_check):
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

if __name__ == '__main__':
    readSQLcase()
    print("Done")
    time.sleep(60)

