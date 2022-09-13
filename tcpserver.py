from socket import *

s_ip = 'localhost'
s_port = 8888
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(s_addr)
s_sock.listen(2)

print('클라이언트의 요청을 기다리는 중...')
client, c_addr = s_sock.accept()
print(c_addr, 'is connected')

data1 = 'Thank you for connecting'
client.send(data1.encode('utf-8'))

client.close()
s_sock.close()