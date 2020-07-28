-

from socket import *
from multiprocessing import Process
import signal,sys

#全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR= (HOST,PORT)

def request(c):
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),':', data)


#搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #循环等待客户端链接
    print("Listen the port 8000")

    while True:
        try:
            c,addr = s.accept()
            print("connect From", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务端退出')
        except Exception as e:
            print(e)
            continue


        #为客户段创建子进程
        p = Process(target=request,args=(c,))
        p.daemon = True
        p.start()



if __name__ == '__main__':
    #main()