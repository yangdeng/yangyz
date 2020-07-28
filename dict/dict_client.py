
from socket import *
from getpass import getpass #运行使用终端

HOST = '127.0.0.1'
PORT = 8000
ADDR= (HOST,PORT)

#搭建客户单网罗
def main():
    s = socket()
    s.connect(ADDR)
    while True:
        print("""
        =================welcome===========
        1.注册　　　２.登录　　　　　３.退出
        ===================================
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        else:
            print("请输入正确选项")
