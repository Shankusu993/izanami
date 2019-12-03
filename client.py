import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#server coding
s.bind(("127.0.0.1",5000))
s.listen(5)
conn,addr=s.accept()#server can have many clientshence conn is used
print(addr)
conn.send(b"Hey this is server")#send in bytes
print(conn.recv(1024))
