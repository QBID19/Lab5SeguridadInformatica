#Mario Rodriguez
#Lab Seguridad Informatica

import socket
Mensaje_Cifrado = ""

Letras_Ascii = [] #Guarda el mensaje letra a letra en ascii

Entrada = open('mensajeentrada.txt','r') #Txt que contiene el texto plano
for i in Entrada.read():
    Letras_Ascii.append(ord(i))
Entrada.close()

Cifrado =  ""#Almacena el mensaje cifrado

B = int(input("Ingrese su valor de B: "))

Host = "LocalHost"
Puerto = 8000

Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))

for i in range(1):
    P = Mi_Socket.recv(1024)
    P = int(P.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'P recibido por el cliente')
    G = Mi_Socket.recv(1024)
    G = int(G.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'G recibido por el cliente')
    k = Mi_Socket.recv(1024)
    k = int(k.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'k recibido por el cliente')
    print((Mi_Socket.recv(1024)).decode(encoding="ascii", errors="ignore"))
    
    #Mensaje Cifrado
    for m in Letras_Ascii:
        y2 = pow(k,B)*m % P
        Cifrado += chr(y2)

    print("Cifrado:", Cifrado, "\n")
    
    y1 = pow(G,B) % P#Se envía hacia el servidor
    Mi_Socket.send(str(y1).encode(encoding="ascii", errors="ignore"))
    print("y1 enviado")
    print((Mi_Socket.recv(1024)).decode(encoding="ascii", errors="ignore"))
    
    for i in Cifrado:
        Mensaje_Cifrado += "," + str(ord(i))
        
    Mi_Socket.send(Mensaje_Cifrado.encode(encoding="ascii", errors="ignore"))#Envia al server el mensaje cifrado en ascii
    
    
    
    
    


