import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务端
ADDRESS = ('127.0.0.1',8888)
client.connect(ADDRESS)
# 发消息
content = input("我想说：")
client.send(content.encode())
# 收消息
data = client.recv(1024).decode()
print('收到客户端消息：',data)
client.close()