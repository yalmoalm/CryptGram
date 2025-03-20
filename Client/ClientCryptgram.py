import socket
import os

class Client:

    def __init__(self):

        self.soc = socket.socket()
        self.serverIP = "127.0.0.1"
        self.port = 1234


    def CheckConnect(self):
        
            self.soc.connect((self.serverIP, self.port))  # Connect to the server.
            self.soc.send(b"ping")  # Send a "ping" message to the server.
            print("Client send: ping")
          
            response = self.soc.recv(1024).decode() # Receive response.

            if response == "pong":
                print("Server respone: pong")  
                print("Connection successful!")

            else:
                raise ConnectionError("Unexpected response from server!")

            self.CloseSocket()


    def SendData(self):

        self.soc.connect((self.serverIP, self.port))  # Connect to the server.
        print("Connected to the server.")

        with open ("POST.json", "rb") as f: # Opens the file in byte string mode.
            
            file_size = os.path.getsize("POST.json")
            print(f"File size: {file_size} bytes")

            self.soc.sendall(str(file_size).encode())  # Send file size followed by a newline
            print("File size sent to the server.")


            total_send = 0 # A variable that checks how much information has already been sent.


            chunk = f.read(256)            

            while total_send < file_size:  # Read the file in 256-byte chunks
                self.soc.sendall(chunk)
                total_send += len(chunk)
                print(f"Sent {total_send}/{file_size} bytes")


        print("The data has been sent successfully!")   
        self.CloseSocket()
            

    def CloseSocket(self):
        self.soc.close()
        print("socket-closed.") 




def main():

    ClientCryptgram = Client()
    #ClientCryptgram.CheckConnect()
    ClientCryptgram.SendData()


if __name__ == "__main__":
    main() 
