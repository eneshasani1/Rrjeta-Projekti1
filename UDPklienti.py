# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:11:04 2021

@author: HP
"""

from socket import *

var = input("Shtypni 1 per te caktuar portin dhe IP Adresen default per server, cafredo karakteri tjeter per te caktuar ate manualisht : ")


if var== '1' :
    serverName = '127.0.0.1'
    serverPort = 14000
else : 
    serverName = input("Shtypni IP Adresen e serverit : ")
    serverPort = int(input("Shtypni porten e serverit : "))



while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, PRIM, FIBONACCI, KONVERTO_VALUTA)?')
    try :
        clientSocket.sendto(message.encode(),(serverName, serverPort))                  #gjun exception 
        pergjiegjja, serverAddress = clientSocket.recvfrom(2048)                        #gjun exception
    except socket.error as e:
        print(str(e))
        clientSocket.close()
        break
    print("Pergjiegjja nga serveri : "+pergjiegjja.decode())
    hapiIArdhshem = input("Shtypni 0 per te mbyllur, cfaredo karakteri per nje kerkese tjeter : ")
    if hapiIArdhshem=='0':
        clientSocket.close()
        break
    else :
        clientSocket.close()
        