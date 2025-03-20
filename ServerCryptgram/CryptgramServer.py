import socket
import json

from Encrypt_the_data import Encryption_and_Decryption
from DB_Cryptgram import database_CryptNet






class Server:


    def __init__(self):

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of the port.
        self.serverIP = "127.0.0.1"
        self.port = 1234
        self.crypto = Encryption_and_Decryption()
        self.DB = database_CryptNet()
    
    def Bind(self):

        self.soc.bind((self.serverIP, self.port)) # Setting the port the server will listen to.
        self.soc.listen(5)    # Setting the amount of connections the server will hold. 

        print("Server waiting...")

    
    def ChackConnect(self):
        
        client, addr = self.soc.accept()
        print(f"Connection from {addr}")

        data = client.recv(1024).decode()  # Receive data.
        print(f"Received: {data}")
            
        if data == "ping":
            client.send(b"pong")  # Send back "pong".
            print("Sent: pong")
                
        else:
            client.send(b"error")  # Send error if message is not "ping".
            print("Sent: error")
                
        self.closeSocket()
    
    
    def closeSocket(self):
        
        self.soc.close() 
        print("Socket-closed.")

    
    def ReciveData(self):
       
        client, addr = self.soc.accept()
        print(f"Connection from {addr}")
        
    
       
        file_size_data = client.recv(1024).decode().strip() # Receive file size and strip whitespace



        # Convert file size to integer
        file_size = int(file_size_data)
        print(f"File size received: {file_size} bytes")

                
        # Step 2: Open a file to save the incoming data
        with open("POST.JSON", "wb") as f:
            total_recv = 0

            while total_recv < file_size:  # Keep receiving data until the full file is received.
                buffer = client.recv(256)  # Receive data in chunks.
                if not buffer:  # Break if no data is received.
                    break
                f.write(buffer)  # Write the received data to the file.
                total_recv += len(buffer)
                print(f"Received {total_recv}/{file_size} bytes")

        print("All the data received!")        
        client.close()  # Close the client connection
        self.DataExtraction()            
    
    
    def DataExtraction(self):
    
        with open ("POST.JSON", "r") as f:

            data = json.load(f)
    

        UserName = data["UserName"] 
        Post = data["Post"]
        print(f"the username befor decryption is: {UserName}, the Post befor decryption is: {Post}") 
        UserName = self.crypto.Decrypt(UserName)
        Post = self.crypto.Decrypt(Post)
        print(f"the username after decryption is: {UserName}, the Post after decryption is: {Post}")  
        
        
        self.DB.Insert_data(UserName, Post)


def main():

    ServerCryptgram = Server()
    ServerCryptgram.Bind()
    #ServerCryptgram.ChackConnect()
    ServerCryptgram.ReciveData()
    



if __name__ == "__main__":
    main()
    
