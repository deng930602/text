'''多进程TCP并发客户端实现'''

import socket
import os   
import sys

# 创建TCP套接字
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 获取命令行参数,sys.args是列表
if len(sys.argv) < 3:
    print("参数错误")
# python3 07_forClient.py 127.0.0.1 888
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDRESS = (HOST,PORT)
# 建立链接
client.connect(ADDRESS)
while True:
    content = input("你想说:")
    client.send(content.encode())
    if not content:
        break
    data = client.recv(1024)
    print('服务器说:',data.decode())
# 关闭
client.close()

