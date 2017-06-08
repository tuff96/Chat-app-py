import sys,socket
from time import sleep
import threading

HOST=input('Give ip: ')
PORT=int(input('Give port'))
#HOST=''
#PORT=

USER=input('Give user')

def conectsock():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except ConnectionError:
        print('Socket error on connection')
        exit()
    
    print('\nConnected to {}:{}'.format(HOST, PORT))
    print("Type message, enter to send, 'q' to quit")
    return sock

def closesock():
    sock.close() 
    exit()


def trimite(sock,m):
    msg='[['+USER+']]:'+m
    try:
        sock.send(msg.encode())
    except ConnectionError:
        print('Socket error during communication')
        sock.close()
        print('Closed connection to server\n')

def primeste(sock):
    return sock.recv(4048).decode()
   
#interfata
from tkinter import *
root = Tk()
root.geometry("500x600")
sock=conectsock()

def printu():
    trimite(sock,eBox.get())
    eBox.delete(0,END)

def timuriu(d):
    d.insert(INSERT,'\n'+primeste(sock))
    sleep(1)
    timuriu(d)
    
btn1 = Button(root,text="Scrie", command=printu)
btn1.pack(side="top")
btn2 = Button(root,text="quit", command=closesock)
btn2.pack(side="top")

eBox = Entry(root)
eBox.pack()
T = Text(root, height=30, width=30)
S = Scrollbar(T)
S.pack(side=RIGHT, fill=Y)
S.config(command=T.yview)
T.pack(fill=BOTH, expand=YES)
myThread = threading.Thread(target=timuriu,args=[T], daemon=True)
myThread.start()
root.mainloop()

