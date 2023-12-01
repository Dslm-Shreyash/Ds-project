import socket
import random

Score = 0
opponent_score = 0
port = 1234

def ClientSend(data):
    responce = data.encode()
    s.send(responce)
    
def ClientRecive():
    result = s.recv(1024)
    result = result.decode()
    return result

def ServerSend(deci) :
    deci = deci.encode()
    co.send(deci)

def ServerRecive():
    responce=co.recv(1024)
    return responce.decode()


joh = int(input("1 : Host \n2 : Join \nInput : "))    
if joh == 1:
    #!Server Part
    s = socket.socket()
    host = socket.gethostname()

    print('server will start on host : ',host)

    s.bind((host,port))
    print("server is bound successfully")

    s.listen(5)
   
    co,ad = s.accept()
    client_name = ServerRecive()
    print(f'{client_name} Has Joined')
    # print(ad, f'( {client_name} ) has connected')
    for x in range(5):
        number = random.randint(1,5)
        print(number)
        ServerSend(str(number))
        print("Waiting For Other Player Input")
        ServerRecive()
        responce = int(input("Enter The Number From 1 to 5 : "))
        if responce == number:
            print("You Have Guessed The Number Right")
            Score +=1
        else:
            print(f'You Have Guessed The Number Wrong The Number Was {number}')
            Score -= 1
        print("Waiting For Other Player Input !!!")
        av=ServerRecive()
    Score = str(Score)
    ServerSend(Score)
    opponent_score=int(ServerRecive())

    
else :
    #!Client part
    name = input("Enter Your Name : ")
    
    client = input("Enter host name : ")
    s = socket.socket()
    s.connect((client,port))
    ClientSend(name)
    print("connected to server")
    
    for x in range(5):
        # number = random.randint(1,5)
        number=int(ClientRecive())
        print(number)
        responce = int(input("Enter The Number From 1 to 5 : "))
        if responce == number:
            Score += 1
            print("You Have Guessed The Number Right")
        else:
            print(f'You Have Guessed The Number Wrong The Number Was {number}')
            Score -= 1
        ClientSend("true")
        print("Waiting For Other Player Input !!!")
    opponent_score=int(ClientRecive())
    Score = str(Score)
    ClientSend(Score)
    

print("Your Score : ",Score)
print("Opponent Score : ",opponent_score)
# s = socket.socket()
# client = input("Enter host name : ")

# s.connect((client,port))
# print("connected to server")
# SendResponce(name)

# # ReciveResponce()
# start = int(input("Press 1 to Start : "))

# if start == 1:
#  responce = input("Enter The Number From 1 to 5 : ")
#     SendResponce(responce)

#     ReciveResponce()

