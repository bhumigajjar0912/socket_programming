import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_add = ("127.0.0.1", 9999)

while True:  
    user_data = input("Enter your message:-")

    # conver data in ascii as it will only accept data in bytes
    new_data= user_data.encode('ascii')
    s.sendto(new_data, recv_add)
    time.sleep(2)
    print("your msg has been sent")
    # waiting for reply
    print(s.recvfrom(10))
