#!/usr/bin/python3
import os
import errno
import signal
import socket
import sys;

BACKLOG = 5
BUFF_SIZE = 128
host = ""
port = 12283

def collect_zombie(signum,frame):
    while True:
        try:
            pid, status = os.waitpid(-1,os.WNOHANG)
            if pid == 0:
                break
        except:
            break

def do_echo(sock):
    while True:
        mess = sock.recv(1024)
        if mess:
            while True:
                print("\nwaiting for request... ")
                data_sock, address = conn_sock.accept()
                print("echo request from {} port {}".format(address[0], address[1]))
                gp = data_sock.recv(BUFF_SIZE)
                message = data_sock.recv(BUFF_SIZE)
                print("{} {}".format(gp.decode(), message.decode()))

                if gp.decode() == 'get':
                    if message:
                        filename = message.decode()
                        accessMode = "r"
                        try:
                            myfile = open(filename, accessMode)
                        except FileNotFoundError:
                            data_sock.sendall("NOT FOUND".encode())
                            print("NOT FOUND")
                            data_sock.close()
                            sys.exit()
                        for line in myfile:
                            data_sock.sendall(line.encode())
                elif gp.decode() == 'put':
                    data = data_sock.recv(BUFF_SIZE)
                    filename = message.decode()
                    accessMode = "w"
                    myfile = open(filename, accessMode)
                    while True:
                        print("{}".format(data.decode()), end="")
                        myfile.write(data.decode())
                        data = data_sock.recv(BUFF_SIZE)
                        if (data.decode() == ""):
                            myfile.close()
                            break;
        else:
            return

signal.signal(signal.SIGCHLD,collect_zombie)

conn_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conn_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
conn_sock.bind((host,port))
conn_sock.listen(BACKLOG)

print('Listening on port %d ...'% port)

while True:
    try:
        print("accept success")
        data_sock,client_address = conn_sock.accept()
    except IOError as e:
        code,msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        conn_sock.close()
        do_echo(data_sock)
        os._exit(0)

    data_sock.close()