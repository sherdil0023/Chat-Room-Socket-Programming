import socket
import sys
from _thread import *
from colorama import Fore

server = socket.socket()
port = 127
server.connect(('127.0.0.1',port))
print("Succesfully Connected to localhost:",port," ! ! ")


def checkformsg():
    while True:
        try:
            msg = server.recv(3072)
            if msg:
                print()
                print(Fore.BLUE,msg.decode(),Fore.RESET)
                print()
            else:
                print("\n" + Fore.RED + "Connection Terminated ! !"+Fore.RESET)
                server.close()
                sys.exit()
        except:
            continue

def typemsg():
    while True:
        msg = input()
        if msg: 
            server.send(msg.encode())
            print("\n" + Fore.GREEN + "From : You \n" + Fore.YELLOW + "Message:",msg,'\n',Fore.RESET)
  

start_new_thread(typemsg, ())
start_new_thread(checkformsg,())


while True:
    continue
