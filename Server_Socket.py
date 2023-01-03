import socket 
import sys
import time

LOCAL_IP_ADDR = "localhost"
LOCAL_PORT_NUM = 5000
bufsize = 1024
INIT_SERVER_MSG = "Hello Client, UDP connection is established".encode()

def set_bufsize(num):
    bufsize = num

def set_init_message(msg):
    INIT_SERVER_MSG = msg

def set_server_port_num(n):
    LOCAL_PORT_NUM = n

def set_server_ip(ip):
    LOCAL_IP_ADDR = ip

def udp_server_socket(message):
    #CREATE DATAGRAM SOCKET
    ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #BIND SOCKET TO ADDR AND IP
    ss.bind((LOCAL_IP_ADDR,LOCAL_PORT_NUM))
    print("UDP server is binded and now listening")
    while True:  #NOW LISTEN FOR INCOMING DATAGRAMS
        recv_data = ss.recvfrom(bufsize)
        msg = recv_data[0]
        addr = recv_data[1]
        ss.sendto(INIT_SERVER_MSG)#SEND MESSAGE BACK TO CLIENT

def create_socket():
    try:
        s = socket.socket()
        return s
    except socket.error as e:
        return -1

if __name__ == "__main__":
    sock = create_socket()
    sock.bind(('',LOCAL_PORT_NUM))
    sock.listen(10)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("The data received from the user is: "+data)
        conn.send("Connection has been established".encode())
    conn.close()
    