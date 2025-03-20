import json
from EncryptCryptgram import Encryption_and_Decryption
from ClientCryptgram import Client

class share_post:

    def __init__(self, username, post): # Initialization function for all instance variables in the class.

        self.data = dict(UserName= username , Post= post)
        self.Encryption_obj = Encryption_and_Decryption()
        self.SendData_obj = Client()

    def Print_the_data(self): # A function that prints the data received by the system.
        
        newstr = self.data
        return newstr
       

    def  Encrypt_data(self): # A function that sends each value from the data individually for encryption.

        self.data['UserName']= self.Encryption_obj.Encrypt(self.data['UserName'])
        #print(self.data['UserName'])
        self.data['Post']= self.Encryption_obj.Encrypt(self.data['Post'])
        #print(self.data['Post'])


    
    def Create_json_file(self): # A function that opens a JSON file and stores the encrypted data in it.    
        
        filepath = "C:/Users/Home/Desktop/cryptgram/cryptgram_clint/Post.json"

        # Writing the dictionary to a JSON file
        with open(filepath, 'w') as f:
            json.dump(self.data, f, indent=4)  # 'indent=4' formats the JSON to be more readable

        print(f"Data successfully written to {filepath}")
  
    def Send_data_to_server(self): 

        self.SendData_obj.SendData()



def main():

    post_01 = share_post(input("Enter UserName: "), input("Enter Post: ")) 
    print(f"The data has been received successfully {post_01.Print_the_data()}")             
    post_01.Encrypt_data()
    post_01.Create_json_file()
    post_01.Send_data_to_server()

if __name__ == "__main__":
    main() 
