from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def inc_conn():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):

    name = client.recv(BUFSIZ).decode("utf8") #магическое BUFSIZ
    welcome = 'Welcome %s! Type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    sending(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            sending(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            sending(bytes("%s has left the chat." % name, "utf8"))
            break


def sending(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection")
    ACCEPT_THREAD = Thread(target=inc_conn)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
