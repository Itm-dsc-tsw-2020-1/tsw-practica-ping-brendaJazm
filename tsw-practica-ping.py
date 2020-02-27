#Brenda Jazmin Guzman Dominguez
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
