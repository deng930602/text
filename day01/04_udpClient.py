import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    content = input('你想说：')
    if not content:
        break
    client.sendto(content.encode(),('127.0.0.1',8888))
    data ,addr= client.recvfrom(1024)
    print(data.decode())
client.close()