import socket
import select

data = None

timeout = 3
msg= "test"

host = "10.0.0.14" #This is the first Galileo port1
host2 = "10.0.0.15"#This is the Second Ethernet port
print ("Connecting to " + host)

port = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket made")

ready = select.select([s],[],[],timeout)


s.connect((host,port))
print("Connection made")

if ready[0]:
    print("[INFO] Sending Message...")
    s.sendall(msg)
    print("[INFO] Message sent.")

    data = s.recv(4096)
    print("[INFO] Data received")
    print (data)
else:
    s.connect((host2,port))
    print("Connection made")

    if ready[0]:
        print("[INFO] Sending Message...")
        s.sendall(msg)
        print("[INFO] Message sent.")

        data = s.recv(4096)
        print("[INFO] Data received")
        print (data)
    if data == 'Testu':
	    print("That's all folks")
    else:
        print("You fucked up")	




