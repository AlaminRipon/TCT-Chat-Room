from http import server
import threading
import socket

host = '127.0.0.1' #Local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
  for client in clients:
    client.send(message)

def handle(client):
  while True:
    