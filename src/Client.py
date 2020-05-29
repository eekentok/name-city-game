import socket
import random, string

HOST = "127.0.0.1"
PORT = 65432
answers = []
datalist = []

def letterRandomizer():
    return random.choice(string.ascii_uppercase)

def inputTaker():
    letter = letterRandomizer()
    name = input("Enter a name starts with " + str(letter) + " : ")
    city = input("Enter a city starts with " + str(letter) + " : ")
    animal = input("Enter a animal starts with " + str(letter) + " : ")
    answers.extend([name, city, animal])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    inputTaker()
    for i in answers: 
        s.sendall(i.encode())
        data = s.recv(1024).decode()
        datalist.append(data)

for i in datalist:
    print("Recieved", repr(i))

