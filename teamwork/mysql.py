import pymssql
import json
import time
import random
def connect():
    flag = pymssql.connect(host='localhost', server='LAPTOP-14UCF6FH\SQL2012', port='51430', user='sa', password='123456',
                           database='Account', charset="utf8")
    if flag:
        print("连接成功")
    return flag



def select():
    conn=connect()
    if conn:
        cursor=conn.cursor()#创建游标对象
        sql='select username from account'
        cursor.execute(sql)
        data=cursor.fetchall()
        para = []
        for i in data:

            text = {'name': str(i[0]).strip()}
            print(text)
            para.append(text)
        cursor.close()  # 关闭游标
        conn.close()
        return json.dumps(para, ensure_ascii=False, indent=4)

def zc(user,password,jwaccount):
    conn=connect()
    if conn:
        cursor = conn.cursor()  # 创建游标对象
        try:
            sql = "insert into account values('%s','%s','%s')  insert into data values('','','','','%s')"%(user,password,jwaccount,jwaccount)
            flag='1000'
            cursor.execute(sql)
            conn.commit()  # 提交修改，不然数据库上不会更新
        except pymssql.IntegrityError:
            flag='4001'

        cursor.close()  # 关闭游标
        conn.close()
    else:
        flag='2001'
    return flag
def relogin(user,password):
    conn = connect()
    if conn:
        cursor = conn.cursor()  # 创建游标对象
        sql = 'select username,passwd,jwaccount from account'
        cursor.execute(sql)
        data = cursor.fetchall()
        username = []
        passwd=[]
        jwaccount=[]
        for i in data:
            username.append( str(i[0]).strip())
            passwd.append(str(i[1]).strip())
            jwaccount.append(str(i[2]).strip())
        return username,passwd,jwaccount

def redata(accountname,room,qq,weixin,jwac):
    conn=connect()
    if conn:
        try:
            cursor=conn.cursor()
            sql="update data set accountname='%s',room='%s',qq='%s',weixin='%s' where jwaccount='%s'"%(accountname,room,qq,weixin,jwac)
            cursor.execute(sql)
            conn.commit()
            flag='1000'
        except pymssql.IntegrityError:
            flag = '4001'
    else:
        flag='2001'
    return flag

def finddata(jwac):
    conn=connect()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "select accountname,room,qq,weixin from data where jwaccount='%s'"%jwac
            cursor.execute(sql)
            data = cursor.fetchone()
            text={
                'accountname': str(data[0]).strip(),
                'room':str(data[1]).strip(),
                'qq':str(data[2]).strip(),
                'weixin':str(data[3]).strip()
            }

            return json.dumps(text, ensure_ascii=False)
        except pymssql.IntegrityError:
            pass

def forget(user,jwac):
    conn=connect()
    if conn:
        try:
            cursor=conn.cursor()
            sql="select passwd from account where jwaccount='%s' and username='%s'"%(jwac,user)
            cursor.execute(sql)
            data=cursor.fetchone()
            passwd=str(data[0]).strip()
            return passwd
        except pymssql.IntegrityError:
            flag='4001'
            return flag
def puttask(jwac,tno,title,label,content,method):
    conn=connect()
    if conn:
        try:
            cursor=conn.cursor()
            if method=='insert':
                sql0 = "select accountname from data where jwaccount='%s'" % jwac  # 查询用户名
                cursor.execute(sql0)
                data = cursor.fetchone()
                username = str(data[0])
                print(username)
                tno=time.strftime("%d%H%M%S", time.localtime())+str(random.randint(10,99))#任务号生成
                sql="insert into task values('%s','%s','%s','%s','%s','%s')"%(jwac,tno,title,content,label,username)
                cursor.execute(sql)
                conn.commit()
                flag='1000'
                return flag
            elif method=='update':#只能修改内容
                sql="update task set content='%s' where tno='%s'"%(content,tno)
                cursor.execute(sql)
                conn.commit()
                flag = '1000'
                return flag
            elif method=='delete':
                sql="delete from task where tno='%s'"%tno
                cursor.execute(sql)
                conn.commit()
                flag = '1000'
                return flag
            elif method=='findtno':
                sql = "select tno from task where jwaccount='%s'"%jwac
                cursor.execute(sql)#后面不能有conn.commit()，否则提交后无法查询
                data = cursor.fetchall()
                task=[]
                for i in data:
                    task.append(str(i[0]).strip())
                return task
            elif method=='find':
                sql = "select title,label,content from task where tno='%s'"%tno
                cursor.execute(sql)
                data = cursor.fetchone()
                text = {
                    'title': str(data[0]).strip(),
                    'tabel': str(data[1]).strip(),
                    'content': str(data[2]).strip(),
                }

                return json.dumps(text, ensure_ascii=False)

        except pymssql.IntegrityError:
                flag = '4001'
                return flag

def putdeal(jwac,dno,title2,label2,content2,method2):
    conn=connect()
    if conn:
        try:
            cursor=conn.cursor()
            if method2=='insert':
                dno=time.strftime("%d%H%M%S", time.localtime())+str(random.randint(10,99))#任务号生成
                sql0="select accountname from data where jwaccount='%s'"%jwac#查询用户名
                cursor.execute(sql0)
                data = cursor.fetchone()
                username=str(data[0])

                sql="insert into deal values('%s','%s','%s','%s','%s','%s')"%(jwac,dno,title2,content2,label2,username)
                cursor.execute(sql)
                conn.commit()
                flag='1000'
                return flag
            elif method2=='update':#只能修改内容
                sql="update deal set content='%s' where dno='%s'"%(content2,dno)
                cursor.execute(sql)
                conn.commit()
                flag = '1000'
                return flag
            elif method2=='delete':
                sql="delete from deal where dno='%s'"%dno
                cursor.execute(sql)
                conn.commit()
                flag = '1000'
                return flag
            elif method2=='finddno':
                sql = "select dno from deal where jwaccount='%s'"%jwac
                cursor.execute(sql)#后面不能有conn.commit()，否则提交后无法查询
                data = cursor.fetchall()
                task=[]
                for i in data:
                    task.append(str(i[0]).strip())
                return task
            elif method2=='find':
                sql = "select title,label,content from deal where tno='%s'"%dno
                cursor.execute(sql)
                data = cursor.fetchone()
                text = {
                    'title': str(data[0]).strip(),
                    'tabel': str(data[1]).strip(),
                    'content': str(data[2]).strip(),
                }

                return json.dumps(text, ensure_ascii=False)

        except pymssql.IntegrityError:
                flag = '4001'
                return flag
def prepos(jwac,xno,type):
    conn=connect()
    if conn:
        try:
            flag='4001'
            cursor = conn.cursor()
            if type=='tno':
                tno = time.strftime("%d%H%M%S", time.localtime()) + str(random.randint(10, 99))  # 任务号生成
                sql = "update task set tno='%s' where tno='%s' and jwaccount='%s'" % (tno,xno,jwac)
                cursor.execute(sql)
                conn.commit()
                flag = '1000'

            elif type=='dno':
                dno = time.strftime("%d%H%M%S", time.localtime()) + str(random.randint(10, 99))  # 任务号生成
                sql = "update task set dno='%s' where dno='%s' and jwaccount='%s'" % (dno,xno,jwac)
                cursor.execute(sql)
                conn.commit()
                flag = '1000'
            #else错误处理（缺）
            return flag
        except pymssql.IntegrityError:
                flag = '4001'
                return flag

def findtask(label):
    conn=connect()
    if conn:
        cursor=conn.cursor()
        try:
            if label!='':
                sql="select title,jwaccount from task where label='%s' order by tno*1 desc"%label  #tno*1 可以将tno转成int型
                cursor.execute(sql)  # 后面不能有conn.commit()，否则提交后无法查询
                data = cursor.fetchall()
                title = []
                jwac=[]
                for i in data:
                    title.append(str(i[0]).strip())
                    jwac.append(str(i[1]).strip())
                print(title, jwac)
                return title,jwac
            else:
                sql = "select title,accountname from task order by tno*1 desc"  # tno*1 可以将tno转成int型
                cursor.execute(sql)  # 后面不能有conn.commit()，否则提交后无法查询
                data = cursor.fetchall()
                title = []
                jwac = []
                for i in data:
                    title.append(str(i[0]).strip())
                    jwac.append(str(i[1]).strip())
                print(title,jwac)
                return title, jwac
        except pymssql.IntegrityError:
            flag = '4001'
            return flag


if __name__ == '__main__':

    select()
    zc('rain88','123456')