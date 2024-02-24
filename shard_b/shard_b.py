import socket

HOST = '0.0.0.0'
PORT = 7000
BUFFER_SIZE = 1024

# create a socket UDP to wait listen all clients in the network

print("shard_b recebendo operações de debito instanciado")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print('Servidor UDP esperando conexão na porta', PORT)

while True:
    message, client_address = server_socket.recvfrom(BUFFER_SIZE)
    print('Mensagem recebida do cliente',
          client_address, ':', message.decode())
    server_socket.sendto('Olá, debito!'.encode(), client_address)
    print('Resposta enviada ao cliente', client_address)
