#BRENDA JAZMIN GUZMAN DOMINGUEZ - ¿Cuantas computadoras estan conectdas al Tec de Morelia?
import os
red = "200.33.171.0/24"
os.system("nmap -sn "+red)


#RESULTADO con nmap
"""
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 12:21 Hora estßndar central (MÚxico)
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.13
Host is up (0.012s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)  
Host is up (0.059s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.031s latency).
Nmap scan report for 200.33.171.66
Host is up (0.0080s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.016s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.016s latency).
Nmap scan report for 200.33.171.86
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.99
Host is up (0.024s latency).
Nmap scan report for 200.33.171.120
Host is up (0.0080s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.125
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.127
Host is up (0.028s latency).
Nmap done: 256 IP addresses (13 hosts up) scanned in 42.84 seconds
"""
