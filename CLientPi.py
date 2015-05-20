__author__ = 'Donny'
import socket
from sys import argv

file = argv
ip = argv
port_akses = argv


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    host = ip #raw_input( ("masukkan alamat IP : "))
    port = port_akses #int(raw_input ("Pilih socket (Sensor A = 1900, Sensor B = 1901) : "))
except :
    print "masukan alamat IP dan port !"

s.connect((host,port))
s.send ('cas')
data = s.recv(1024)
print 'data : ', data
#print (data)
s.close()
#print (data)



