
from socket import *
from getpass import getpass #运行使用终端

HOST = '127.0.0.1'
PORT = 8000
ADDR= (HOST,PORT)
s = socket()
s.connect(ADDR)

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
        else:
            print("祖册失败")
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
            pass
        elif cmd == '3':
            pass
        else:
            print("请输入正确选项")










if __name__ == '__main__':
    main()



