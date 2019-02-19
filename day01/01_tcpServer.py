import socket

# 套接字
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 端口复用
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 绑定地址
server.bind(('0.0.0.0',8888))
# 监听
server.listen(5)
# 等待客户端请求
print('等待客户端连接')
client,addr= server.accept()
# 接收客户端消息
data = client.recv(1024)
print(data.decode())
client.send("服务端收到".encode())
# 关闭
client.close()
server.close()