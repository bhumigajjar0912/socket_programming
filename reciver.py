import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                   ipv4            udp

s.bind(("127.0.0.1", 9999))
# you can also write 'localhost' in place of 127.0.0.1
while True:    
    data_recv = s.recvfrom(100)
    print(data_recv)
    reply="Thanks for connecting"
    s.sendto(reply.encode('ascii'),data_recv[1])