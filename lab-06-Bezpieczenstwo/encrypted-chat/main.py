import socket 
import threading
import rsa


def sending_messages(client):
    while True:
        message = input("")
        client.send(message.encode())
        print(f"You've send {message}")

def receiving_messages(client):
    while True:
        message = input("")
        print(f"You've send {client.recv(1024).decode()}")        

try:
    choise = int(input("What you want to do: *1* host or *2* connect: "))

    match choise:
        case 1:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 9999))
            server.listen()
            client, _ = server.accept()
        case 2:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("127.0.0.1", 9999))
        case _:
            exit()


    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receiving_messages, args=(client)).start()

except ValueError:
    print("Sorry, wrong choise!, try again")
    
