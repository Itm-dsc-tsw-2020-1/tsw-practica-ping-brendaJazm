# tsw-practica-ping-brendaJazm
tsw-practica-ping-brendaJazm created by GitHub Classroom
#BRENDA JAZMIN GUZMAN DOMINGUEZ--

#Libreria para llamar al sistema operativo
import os

#Definir servidor arevisar
hostname = "www.itmorelia.edu.mx"

#Llamada a la consola
respuesta =  os.system("ping " + hostname)

#Verificando la respuesta
if respuesta == 0:
    print(hostname + ": esta en funcionamiento!")
else:
    print(hostname + ": No funciona!") 

#CICLO DE: ¿Cuantas computadoras hay conectadas?
import os
contador = 0
#numIP = 254
red = "200.33.171."
#for i in range(numIP) //otra opcion
for i in range( 0 , 254 ):
    i+=1
    respuesta = os.system("ping "+ red + str(i))
    if respuesta == 0: print("CONECTADA"); contador+=1; print ("Computadoras conectadas hasta el momentito: "+ str(contador))
else:
    if respuesta == 1: print("DESCONECTADO")

#PRUEBAS

#compus conectadas
import os
red = "200.33.171.0/24"
os.system("nmap -sn "+red)

#Seleccionar segmento de red
red = "192.168.0.0/24"

#Rastrear red
os.system("nmap -sP " + red)

#Seleccionar una computadora
computadora = "192.168.0.15"

#Detectar puertos abierto
os.system("nmap -sT " + computadora)

#Seleccionar una computadora
computadora = "192.168.0.15"

#Detectar sistema operativo
os.system("nmap -O " + computadora)
