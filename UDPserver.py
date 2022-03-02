# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:16:42 2021

@author: HP
"""
import socket
import re
import math
from datetime import *
from _thread import *
import random

serverName='127.0.0.1'
serverPort = 14000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    serverSocket.bind(('127.0.0.1', serverPort))        #tentojme te startojme serverin(ngrisim)
except socket.error as e :
    print(str(e))                                   #nese ndodh ndonje gabim e printojme gabimin
    
def numeroZanore(teksti):
    numeriZanoreve=0
    for i in range(len(teksti)):
        if(re.match(r'[aeëiouyAEËIOUY]',teksti[i])):
            numeriZanoreve = numeriZanoreve + 1
    return numeriZanoreve

def countNotALetter(teksti):
    notALetterCounter=0
    for i in range(len(teksti)):
        if(re.match(r'[^\w]',teksti[i]) or re.match(r'[\d]',teksti[i])):
            notALetterCounter = notALetterCounter + 1
    return notALetterCounter


def IP(address):
    return "IP Adresa e klientit eshte: "+address[0]
def NRPORTIT(address):
    return "Klienti eshte duke perdorur portin: "+str(address[1])
def NUMERO(kerkesa_e_dekoduar):
    teksti = kerkesa_e_dekoduar.split(" ",1)[1]                                      # e ndajme tekstin ne dy pjese, ne hapsiren e pare qe gjendet,funksioni kthen vektor me dy anetare e marrim anetarin e 2 te i cili eshte teksti
    numriIZanoreve = numeroZanore(teksti)
    notALetterCounter = countNotALetter(teksti)
    numriIBashktinglloreve = len(teksti) - numriIZanoreve - notALetterCounter;
    pergjiegjja = "Teksti i pranuar permban "+str(numriIZanoreve)+" zanore dhe "+str(numriIBashktinglloreve)+" bashktingllore"
    return pergjiegjja

def ANASJELLTAS(kerkesa_e_dekoduar):
    teksti = kerkesa_e_dekoduar.split(" ",1)[1]                                      # e ndajme tekstin ne dy pjese, ne hapsiren e pare qe gjendet,funksioni kthen vektor me dy anetare e marrim anetarin e 2 te i cili eshte teksti
    tesktiPaHapsira = teksti.strip()                          #i largojme hapsirat ne mes dhe ne fund pasi qe duhet ta kthejme pa hapsira ne mes dhe ne fund
    anasjelltas = tesktiPaHapsira[::-1]
    return anasjelltas

def PALINDROM(kerkesa_e_dekoduar):
    fjalia = kerkesa_e_dekoduar.lower().split()[1:]
    tekstiRevers = fjalia[::-1]
    for i in  range(len(tekstiRevers)):
        tekstiRevers[i]=tekstiRevers[i][::-1]
    if (tekstiRevers == fjalia):
        return "Teksti i dhene eshte palindrome"
    else:
        return "Teksti i dhene nuk eshte palindrome"
    
def KOHA():
    datetime.now().strftime("%d.%m.%Y %H:%M:%S %p")

def LOJA():
    listaMeNrRastit = random.sample(range(1, 36), 5)
    listaESortuar = (sorted(listaMeNrRastit))
    pergjiegjja = str(listaESortuar)
    return pergjiegjja


def GCF(kerkesa_e_dekoduar):
    numri_i_pare = int(kerkesa_e_dekoduar.split()[1] )                 #split() e ndan kerkesen ne vektore ku si delimiter merr space, kemi vektorin ['GCF','10',20](si shembull), dmth gjith anetari 1 eshte numri i pare
    numri_i_dyte = int(kerkesa_e_dekoduar.split()[2])                #marrim numrin e dyte
    PMMP = math.gcd(numri_i_pare,numri_i_dyte)                  #kthejme pjestuesin me te madh te perbashket te ketyre dy numrave
    return str(PMMP)

def KONVERTO(kerkesa_e_dekoduar):
    opsioni = kerkesa_e_dekoduar.split()[1]                     #KONVERTO {Hapësire} Opcioni {Hapësire} Numër, anetari 1 eshte Opcion, andaj marrim opcionin
    numri = int(kerkesa_e_dekoduar.split()[2]) 
    if opsioni =='cmNeInch' :
        gajtesia_e_konvertuar = numri/2.54
        return str(gajtesia_e_konvertuar)
    elif opsioni == 'inchNeCm' :
        gajtesia_e_konvertuar=numri*2.54
        return str(gajtesia_e_konvertuar)
    elif opsioni == 'kmNeMiles' :
        gajtesia_e_konvertuar = numri/1.609
        return str(gajtesia_e_konvertuar)
    elif opsioni == 'mileNeKm' :
        gajtesia_e_konvertuar = numri*1.609
        return str(gajtesia_e_konvertuar)
def PRIM(kerkesa_e_dekoduar):
    numri = int(kerkesa_e_dekoduar.split()[1])
    if numri <= 1 :
        return "Numrat prim jane numra natyrore me te medhenje se 1, andaj numri qe shtypet nuk eshte prim"
    i = 2
    prim = True
    plotepjestuesi = 1
    while i <= numri/2 :
        if(numri%i==0):
            prim = False
            plotepjestuesi = i
            break
        i=i+1
    if prim :
        return "Numri eshte prim"
    else :
        return "Numri nuk eshte prim, plotepjestuesi natyror me i vogel i tij qe e bene ate jo te thjeshte eshte "+str(plotepjestuesi)

def FIBONACCI(kerkesa_e_dekoduar):
    numri = int(kerkesa_e_dekoduar.split()[1])
    if numri== 1 :
        return "Anetari i pare i serise furie eshte 0."
    seria_fibonacci= [0,1]
    i=2
    while i < numri :
        vlera_e_anetarit_i=seria_fibonacci[i-1] + seria_fibonacci[i-2]
        seria_fibonacci.append(vlera_e_anetarit_i) 
        i=i+1
    pergjiegjja = str(numri) +" anetaret e pare te serise fibonacci jane "+str(seria_fibonacci)+"."
    return pergjiegjja

def KONVERTO_VALUTA(kerkesa_e_dekoduar):
    opsioni = kerkesa_e_dekoduar.split()[1]                     #KONVERTO_VALUTA{Hapësire}Opcioni{Hapësire}Numër, anetari 1 eshte Opcion, andaj marrim opcionin
    numri = int(kerkesa_e_dekoduar.split()[2]) 
    if opsioni =='euroNeDollar' :
        eKonvertuar = numri*1.2
        return str(eKonvertuar)
    elif opsioni == 'dollarNeEuro' :
        eKonvertuar=numri/1.2
        return str(eKonvertuar)
    elif opsioni == 'euroNePound' :
        eKonvertuar = numri*0.87
        return str(eKonvertuar)
    elif opsioni == 'poundNeEuro' :
        eKonvertuar = numri/0.87
        return str(eKonvertuar)
    elif opsioni == 'euroNeFrang' :
        eKonvertuar = numri*1.1
        return str(eKonvertuar)
    elif opsioni == 'frangNeEuro' :
        eKonvertuar = numri/1.1
        return str(eKonvertuar)
    elif opsioni == 'euroNeLek' :
        eKonvertuar = numri*123.2
        return str(eKonvertuar)
    elif opsioni == 'lekNeEuro' :
        eKonvertuar = numri/123.2
        return str(eKonvertuar)

def threadi_klient(kerkesa,clientAddress):
    kerkesa_e_dekoduar = str(kerkesa.decode('utf-8'))
    if kerkesa_e_dekoduar == 'IP':
        pergjiegjja = IP(clientAddress);
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif kerkesa_e_dekoduar == 'NRPORTIT':
        pergjiegjja = NRPORTIT(clientAddress);
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^NUMERO .+$',kerkesa_e_dekoduar):
        pergjiegjja = NUMERO(kerkesa_e_dekoduar);
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^ANASJELLTAS .+$',kerkesa_e_dekoduar):
        pergjiegjja = ANASJELLTAS(kerkesa_e_dekoduar);
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^PALINDROM .',kerkesa_e_dekoduar)  :
        pergjiegjja = PALINDROM(kerkesa_e_dekoduar);
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif kerkesa_e_dekoduar == 'KOHA' :
        pergjiegjja = KOHA(); 
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif kerkesa_e_dekoduar == 'LOJA':
        pergjiegjja = LOJA();
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^GCF [0-9]+ [0-9]+$',kerkesa_e_dekoduar) :                  #permes regex e validojme kerkesen e dekoduar nese e match patternin qe e kemi caktuar
        pergjiegjja = GCF(kerkesa_e_dekoduar)
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^KONVERTO (cmNeInch|inchNeCm|kmNeMiles|mileNeKm$) [0-9]+$',kerkesa_e_dekoduar):         #permes regex e validojme kerkesen e dekoduar nese e match patternin qe e kemi caktuar, nuk ka shume kuptim me qene gjatesite negative andaj nuk e kemi lejuar vendosjen e gjatesive negative
        pergjiegjja = KONVERTO(kerkesa_e_dekoduar)
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^PRIM -?[0-9]+$',kerkesa_e_dekoduar):
        pergjiegjja = PRIM(kerkesa_e_dekoduar)
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^FIBONACCI [1-9][0-9]*$',kerkesa_e_dekoduar):
        pergjiegjja = FIBONACCI(kerkesa_e_dekoduar)
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    elif re.match(r'^KONVERTO_VALUTA (euroNeDollar|dollarNeEuro|euroNePound|poundNeEuro|euroNeFrang|frangNeEuro|euroNeLek|lekNeEuro) [0-9]+$',kerkesa_e_dekoduar):         #permes regex e validojme kerkesen e dekoduar nese e match patternin qe e kemi caktuar, nuk ka shume kuptim me qene gjatesite negative andaj nuk e kemi lejuar vendosjen e gjatesive negative
        pergjiegjja = KONVERTO_VALUTA(kerkesa_e_dekoduar)
        serverSocket.sendto(pergjiegjja.encode(),clientAddress)
    else :
        serverSocket.sendto("Kerkesa nuk ishte valide".encode(),clientAddress)

print("Serveri eshte startuar ne IP Adresen "+serverName+" ne portin "  + str(serverPort))
while True:
    print('Serveri eshte i gatshem te procesoj ndonje kerkese')
    kerkesa, clientAddress = serverSocket.recvfrom(128)
    print('Serveri pranoi kerkese nga klienti me IP Adrese '+clientAddress[0]+" i cili eshte duke perdorur portin "+str(clientAddress[1]))
    print('-------------------------------------------------------------')
    start_new_thread(threadi_klient,(kerkesa,clientAddress,))