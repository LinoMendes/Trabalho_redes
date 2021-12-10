import threading
import socket

clients = [] #lista de clientes

def main():

    server = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    try: # ligação do servidor
        server.bind(('localhost', 7777)) # servidor e porta
        server.listen() #para receber as conecções (ouvir)
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True: # Para aceitar as conecções
        client, addr = server.accept() # para aceitar conecção
        clients.append(client) #adicinoar usuario a lista

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client): # função que faz o tratamento das msgs
    while True:
        try:
            msg = client.recv(2050)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client: #verifa se o cliente que enviu e diferente do que recebeu
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client): #caso não seja possívle enviar a msg, o cliente é excluido
    clients.remove(client)

main()