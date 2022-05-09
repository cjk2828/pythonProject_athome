import socket

host = '192.168.0.2'
port = 12283
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}".format(server_address[0], server_address[1]))
sock.connect(server_address)

message = input("vsftp : ")
gp,message = message.split(' ')

while True:
    try:
        sock.sendall(gp.encode())
        sock.sendall(message.encode())

        if gp.upper() == 'quit':
            break;
        elif gp == 'get':
            data = sock.recv(BUFF_SIZE)
            if data.decode() == "NOT FOUND":
                print("{}".format(data.decode()))
            else:
                filename = message
                accessMode = "w"
                myfile = open(filename, accessMode)
                while True:
                    print("{}".format(data.decode()), end="")
                    myfile.write(data.decode())
                    data = sock.recv(BUFF_SIZE)
                    if (data.decode() == ""):
                        myfile.close()
                        break;
        elif gp == 'put':
            filename = message
            accessMode = "r"
            myfile = open(filename, accessMode)
            for line in myfile:
                sock.sendall(line.encode())
            myfile.close()
    except Exception as e:
        print("Exception : {}".format(e))
sock.close()