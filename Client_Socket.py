import socket
import sys
import time

INIT_CLIENT_MSG = "This is the client trying to reach the server".encode()
SERVER_IP = "localhost"
SERVER_PORT_NUM = 5000
bufsize = 1024

def set_bufsize(num):
    bufsize = num

def set_init_message(msg):
    INIT_CLIENT_MSG = msg

def set_server_port_num(n):
    SERVER_PORT_NUM = n

def set_server_ip(ip):
    SERVER_IP = ip

def udp_client_socket(url,messages):
    host = socket.gethostname(url)
    port = 5000
    addr = (host,port)
    #INITIALIZE UDP SOCKET OBJECT
    udp_sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    udp_sock.settimeout(10)
    #START TIMER
    start = time.time()
    #SEND INITIAL MESSAGE TO SERVER
    udp_sock.sendto(messages, addr)
    #CHECK AND SEE IF SERVER SENDS DATA BACK
    try:
        data, server = udp_sock.recvfrom(1024)
        end = time.time()
        elapsed = end - start
    #IF NOT THEN EXCEPT ERROR
    except socket.timeout:
        print('REQUEST TIMED OUT')

def tcp_client_socket():
    host = socket.gethostname()
    port = 3000 #SOCKET SERVER PORT NUMBER
    sock = socket.socket()
    sock.connect((host,port))
     #GET DATA TO SEND TO USER
    data = input("Enter data: ").encode('utf-8')
    if data:
        sock.send(data)
        response = sock.recv(1024).decode("utf-8") 
    sock.close()

if __name__ == "__main__":
    pass


