#!/usr/bin/python3
import socket
import threading

class EchoThread(threading.Thread):
    def __init__(self,socket,address):
        threading.Thread.__init__(self)
        self.ip,self.port = address
        self.csocket = socket
        print("[+] New service thread started for {}".format(self.ip))

    def run(self):

        thread_count = threading.active_count()
        print("{} threads are running...".format(thread_count))
        while True:
            data = self.csocket.recv(2048)
            if data:
                self.csocket.sendall(data)
            else:
                break
        print("[-] Service thread terminated for {} ".format(self.ip))
        thread_count = threading.active_count()
        print("{} threads are running...".format(thread_count-1))

host = ''
port = 10000
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
conn_sock.bind((host,port))
conn_sock.listen(BACKLOG)

while True:
    print("listening for incoming requests...")
    data_sock, client_address = conn_sock.accept()
    serviceThread = EchoThread(data_sock,client_address)
    serviceThread.setDaemon(True)
    serviceThread.start()