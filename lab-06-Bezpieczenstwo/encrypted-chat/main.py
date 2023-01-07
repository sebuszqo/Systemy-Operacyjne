import socket 
import threading
import rsa

        
def sending_messages(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(),public_partner))
        print(f"You've send {message}")

def receiving_messages(c):
    while True:
        print(f"You've received: {rsa.decrypt(c.recv(1024), private_key).decode()}")
    
public_key, private_key = rsa.newkeys(1024)
public_partner = None


choise = input("What you want to do: *1* host or *2* connect: ")
    
if choise == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9093))
    server.listen()
    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choise == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9093))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()