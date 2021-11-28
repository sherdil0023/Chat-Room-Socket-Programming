import socket
from _thread import *
from colorama import Fore,Back
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 127
srvr.bind(('', port))

print("Socket successfully created at port : ",port)
print("Server Is Up And Running ! !")
clients = []
srvr.listen()
print("Socket is Listening...")

welcome_string = " Welcome to The Chatroom ! ! "


def Client_Thread(client, address):    
    while True:
        try:
            msg = client.recv(3072).decode()
            if msg:
                msg_sent = Fore.GREEN + "From: " + str(address[0]) + ':' + str(address[1]) + '\n' + Fore.YELLOW +  "Message: " + str(msg) + Fore.RESET
                print(msg_sent)
                sendtoall(msg_sent, client)
            else:
                RemoveFromList(client)
                client_left = Back.WHITE + Fore.BLACK + str(address[0]) + ':' + str(
                    address[1]) + " Left The Chatroom ! !" + Back.RESET+ Fore.RESET
                print('\n',client_left,'\n')
                sendtoall(client_left,client)
                return
        except:
            continue


def sendtoall(msg, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(msg.encode())
            except:
                client.close()
                RemoveFromList(client)


def RemoveFromList(client):
    if client in clients:
        clients.remove(client)


while True:
    client, address = srvr.accept()
    print(Back.WHITE,Fore.BLACK,f"New User Joined {address[0]}:{address[1]}\n\n",Back.RESET,Fore.RESET)
    welcome = Back.WHITE + Fore.BLACK + str(address[0]) + " : " + str(address[1]) + welcome_string + Back.RESET + Fore.RESET
    user_joined = Back.WHITE + Fore.BLACK + str(address[0]) + " : " + str(address[1]) + " Just Joined The Chatroom ! !" + Back.RESET + Fore.RESET
    sendtoall(user_joined, client)
    client.send(welcome.encode())
    clients.append(client)
    start_new_thread(Client_Thread, (client, address))

