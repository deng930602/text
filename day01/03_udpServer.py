import socket

# 创建套接字
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind(('0.0.0.0',8888))
print('正在等待客户端链接')
# 收消息
while True:
    data,addr = server.recvfrom(1024)
    if not data:
        break
    print("客户端对服务器说",data.decode())
    server.sendto('服务器收到'.encode(),addr)
server.close()