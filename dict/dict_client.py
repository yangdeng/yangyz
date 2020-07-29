
from socket import *
from getpass import getpass #运行使用终端

HOST = '127.0.0.1'
PORT = 8000
ADDR= (HOST,PORT)
s = socket()
s.connect(ADDR)

#查历史记录
def do_hist(name):
    msg = "H " + name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")

#查单词
def do_query(name):
    while True:
        word = input("单词：")
        if word == '##':#结束单词查询
            break
        msg = "Q %s %s" %(name,word)
        s.send(msg.encode())#发送请求
        data = s.recv(2048).decode()
        print(data)


def login(name):
    while True:
        print("""
        =================Query============
        1.查单词　　　２.历史记录　　３.注销
        ===================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确选项")


#注册函数
def do_register():
    while True:
        name = input("User:")
        passwd = getpass
        passwd1 = getpass('Again:')
        if passwd != passwd1:
            print("两次密码不一致！")
            continue
        if ' ' in name or ' ' in passwd:
            print("用户名，密码不能有空格")
            continue
        msg = 'R %s %s' % (name,passwd)
        s.send(msg.encode())#发送给客户
        data = s.recv(128).decode() #接受结果
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("祖册失败")
        return



def do_login():
    """
    登录
    :return:
    """
    name = input("User:")
    passwd = getpass()
    msg = "L %s %s" %(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        print("登录成功")
        login(name)
    else:
        print("登录失败")
    return


#搭建客户单网罗
def main():
    while True:
        print("""
        =================welcome===========
        1.注册　　　２.登录　　　　　３.退出
        ===================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()



