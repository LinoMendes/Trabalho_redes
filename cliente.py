import socket
import threading #para que uma função rode um ao lado da outra - pois uma vai receber uma msg outra receber


def main():
    client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    try: # PARTE RESPOSAVEL PARA FAZER A CONEÇÃO
        client.connect(('localhost', 7777)) # Servidor e porta
    except:
        return print("\nNão foi possível se conectar ao servidor!\n")

    username = input('usuário > ') #Identificação do usuario que esta enviando a msg
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMenssages, args=[client]) #targert = o que vai ser executado / args => o que vai ser aceito
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start() # inicialização das funções
    thread2.start()


def receiveMenssages(client): #Função para receber as msgs
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível permancer conectado ao servidor!\n')
            print('Precione <Enter> Para continuar...')
            client.close()
            break


def sendMessages(client, username): #Função para envia as msgs
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.decode('utf-8'))
        except:
            return


main()
