#Java 1 - Klienti aplikacioni - Python Socket Programming

#Immportojme librarine per socket komunikim
import socket

var = input("Shtypni 1 per te caktuar portin dhe IP Adresen e serverit default, cafredo karakteri tjeter per te caktuar manualisht : ")
if var== '1' :
    serverName = '127.0.0.1'
    serverPort = 14000
else : 
    serverName = input("Shtypni IP Adresen e serverit : ")
    serverPort = int(input("Shtypni porten e serverit : "))
    
while True:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soketi.connect((serverName,serverPort))
    except socket.error as e:
        print(str(e))
        soketi.close()
        print("Deshtoi te vendoset lidhja mes serverit dhe klientit")
        break 
    kerkesa = input('Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, PRIM, FIBONACCI, KONVERTO_VALUTA)?')
    
    #dergojme kerkesen tek serveri (ne kete rast localhost me portin 1200)
    try :
        soketi.sendall(str.encode(kerkesa))                                                                                                          #default encoding=utf-8           automatikisht ja attach paketes edhe source address 
    except socket.error as e:
        print(str(e))
        soketi.close()
        print( "serveri mbylli lidhjen para se te dergohet kerkesa")
        break
    
    #duhet te presim....
    mesazhi = ''
    try:
        while True: #unaze e pafundme  
            data = soketi.recv(4)                               #munet me gju error
            if len(data) <= 0:
               break
            mesazhi += data.decode("utf-8")
    except socket.error as e:
        print(str(e))
        soketi.close()
        break
    
    print("Pergjiegjja nga serveri : ", mesazhi)
    hapiIArdhshem = input("Shtypni 0 per te mbyllur, cfaredo karakteri per njer kerkese tjeter : ")
    if hapiIArdhshem == '0' :
        soketi.close()
        break
    else :
        soketi.close()


#socket komandat e perdorura - connect, close, sendall, recv