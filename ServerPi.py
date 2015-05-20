__author__ = 'Donny'
import socket
import thread
import sys



#daftar = []
#for i in range(2):
#    daftar.append(1)

#def baca_file(baris, kata, daftar):
#    f=open("nat.txt", "r")
#    baris = f.xreadlines(2)
#    for baris in f:
#        for baris in line.split():
#            daftar[i]= baris
#            print daftar[1]
#            if daftar == 1:
#               int (daftar [1])
#    f.close()


#port = baca_file()
port_A = 1900
port_B = 1901

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)  #TCP conecction type
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
#    if daftar[1]==1900:
#        s.bind(('127.0.0.1', 1900))
#        s.listen(10)
#    elif daftar[1]==1901:
#        s1.bind(('127.0.0.1', 1901))
#        s1.listen(10)
#    else:
#        print 'IP dan Port tujuan salah'
    s.bind(('127.0.0.1', port_A)) #listening
    s.listen(10)
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)  #TCP conecction type
    s1.bind(('127.0.0.1', port_B)) #listening port
    s1.listen(10)

except socket.error, msg:
    print 'Failed to create socket. EROR CODE:' + str(msg[0]) + ', Eror Message :' + str(msg[1])
    sys.exit()
print 'socket created'


#s.listen(5) #backlog bisa nampung requert sampe 5 request dalam queue
#s1.listen(5)
print 'socket is now listening'


def koneksi(threadname,soket):
    while 1:
        conn, addr = soket.accept() #terima koneksi
        print 'dari IP : ',addr
        data = conn.recv(1024)
        print 'data : ', data
        conn.send('siap')

try:
    thread.start_new_thread( koneksi, ("Thread-1",s, ) ) #menjalankan thread untuk listening PORT_A
    print 'berhasil1'
    thread.start_new_thread( koneksi, ("Thread-2",s1, ) )#menjalankan thread untuk listening port_B
    print 'berhasil2'
except:
   print "Error: unable to start thread"

daftar = []
for i in range(2):
    daftar.append(1)


while 1:

    def baca_file(baris, kata, daftar):
        f=open("nat.txt", "r")
        baris = f.xreadlines()
        for baris in f:
            for baris in line.split():
                daftar[i]= baris
                print daftar[1]
                if daftar == 1:
                    int (daftar [1])
        f.close ()

    if koneksi ==1 :
        if baca_file() == port_A:
            daftar[2]
        elif baca_file() == port_B:
            daftar[2]
        else:
            print "port tujuan tidak cocok"
   #pass


