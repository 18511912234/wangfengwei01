import sys,re,time,requests,MySQLdb
from random import choice
#卖家和买家接口测试用例报告

HOSTNAME = '192.168.215.55'

#读取当天的接口bug
def buyer_readAPIbug():
    sql='select * from zt_bug where zt_bug.product=1 and data(openedDate)=curdate();'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        #打印出bug标题和重现步骤

        #print(buyercaseid(bug_list[0][0])+""+bug_list[0][1]))
        print(buyercaseid(case_list[0][0]+''+case_list[0][1]))
    coon.commit()
    cursor.close()
    coon.close()

#读取测试用例的接口id
def buyercaseid(results):
    global buyerid
    global buyertitle

    regx=r'(\d+)_'

    regx2=u"([\u4e00-\u9fa5]+)"

    pm=re.search(regx,results)
    pm2=re.search(regx2,results)

    if pm:
        buyerid=pm.group(1).encode("utf-8")
    if pm2:
        buyertitle=pm2.group(1)
    return buyerid+''+buyertitle

#读取接口总数
def buyer_interface_total():
    sql='......................'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取测试用例总数
def buyer_case_total():
    sql='...................'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取pass测试用例总数
def buyer_case_pass():
    sql='......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取未执行的测试用例总数
def buyer_case_skip():
    skipcase=buyer_case_total()-buyer_case_pass()-buyer_case_fail()
    return skipcase

#读取失败测试用例总数
def buyer_case_fail():
    sql='......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取流程类测试用例总数
def buyer_flow_total():
    sql='..........'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取流程类通过测试用例总数
def buyer_flow_pass():
    sql='...............'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取流程类跳过测试用例总数
def buyer_flow_skip():
    sql='...............'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取流程类失败测试用例总数
def buyer_flow_fail():
    sql='...............'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取卖家的bug
def biz_readAPIbug():
    sql='...............'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        bug_list=[]
        bug_list.append(ii)
        print(bizcaseid(bug_list[0][0]+''+bug_list[0][1]))
    coon.commit()
    cursor.close()
    coon.close()

#正则匹配用例id和标题
def bizcaseid(results):
    global bizid
    global biztitle
    regx = r'(\d+)_'

    regx2 = u"([\u4e00-\u9fa5]+)"

    pm = re.search(regx, results)
    pm2 = re.search(regx2, results)

    if pm:
        bizid = pm.group(1).encode("utf-8")
    if pm2:
        biztitle = pm2.group(1)
    return bizid + '' + biztitle

#读取卖家接口总数
def biz_interface_total():
    sql='......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取卖家用例总数
def biz_case_total():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()


#读取pass用例总数
def biz_case_pass():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取失败用例总数
def biz_case_fail():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取跳过未执行用例总数
def biz_case_skip():
    skipcase=biz_case_total()-biz_case_pass()-biz_case_fail()


#读取卖家流程用例总数
def biz_flow_total():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取卖家流程pass用例总数
def biz_flow_pass():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取卖家流程失败用例总数
def biz_flow_fail():
    sql = '......'
    coon = MySQLdb.connect(user='root', passwd='123456', db='zentao', port='3306', host='192.168.58.23',
                           charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    return info[0][0]
    coon.commit()
    cursor.close()
    coon.close()

#读取跳过未执行用例总数
def biz_case_skip():
    skipcase=biz_flow_total()-biz_flow_pass()-biz_flow_fail()
    return skipcase


if __name__ == '__main__':
    print("接口自动化测试报告")

    print("买家")
    print("接口总数"+str(buyer_interface_total()))
    print("独立用例总数"+str(buyer_case_total())+"通过数"+str(str(buyer_case_pass()))+"跳过数"+str(buyer_case_skip())+"失败数"+str(buyer_case_fail()))
    print("流程用例总数"+str(buyer_flow_total())+"通过数"+str(str(buyer_flow_pass()))+"跳过数"+str(buyer_flow_skip())+"失败数"+str(buyer_flow_fail()))
    print('今天运行的接口错误详情如下')
    buyer_readAPIbug()

    print("卖家")
    print("接口总数" + str(biz_interface_total()))
    print("独立用例总数" + str(biz_case_total()) + "通过数" + str(biz_case_pass()) + "跳过数" + str(biz_case_skip()) + "失败数" + str(biz_case_fail()))
    print("流程用例总数" + str(biz_flow_total()) + "通过数" + str(biz_flow_pass()) + "跳过数" + str(biz_case_skip()) + "失败数" + str(biz_flow_fail()))
    print('今天运行的接口错误详情如下')
    biz_readAPIbug()
    print("Done")





