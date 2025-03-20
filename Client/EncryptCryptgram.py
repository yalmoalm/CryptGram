import base64

class Encryption_and_Decryption:

    def __init__(self): # Initialization function for all instance variables in the class.
         
         self.cypher = 123


    def Encrypt(self, DataToEncrypt): # A function for encrypting the data.


        Encrypt_data= []

        for index_of_the_string in range(len(DataToEncrypt)): # A for loop that iterates over the length of the string.
                                                              # The iterator holds the index of the string.

            Encrypt_data.append(chr(ord(DataToEncrypt[index_of_the_string]) ^ self.cypher))
            
            # The process is as follows:
            # 1.Convert each character to its numeric representation using the ord function.
            # 2.Perform an XOR operation on the numeric value with the cipher key.
            # 3.Convert the resulting number back to a character using the chr function.
            # 4.Finally, append the character to a list.


        return(base64.b64encode("".join(Encrypt_data).encode()).decode())

        # This line of code performs the following operations:
        # 1.To concatenate all the characters in the list into a string, we used the join function.
        # 2.encode(): Encodes the resulting string into UTF-8 format, which converts the string into a byte sequence.
        # 3.base64.b64encode(...): Encodes the UTF-16 byte sequence into a Base64 format. Base64 encoding ensures the byte data is converted into a text-safe format, 
        #   commonly used for data transfer or storage.
        # 4.decode(): Converts the Base64 byte output back into a string.



    def Decrypt(self, DataToDecrypt): # A function for decoding the data.


      

        decoded_data = base64.b64encode(DataToDecrypt).encode()

        # The line of code performs the following operations:
        # 1.base64.b64decode(DataToDecrypt): Decodes the Base64-encoded string (DataToDecrypt) back into its original byte sequence. 
        # This reverses the Base64 encoding applied earlier.
        # 2.decode(): Converts the byte sequence into a string using the UTF-8 encoding. 
        # This reverses the UTF-16 encoding step during encryption.

  

        DecryptData = []

        for index_of_the_string in range(len(decoded_data)): # Same loop as in the previous function

            DecryptData.append(chr(ord(decoded_data[index_of_the_string]) ^ self.cypher)) 
        
        return("".join(DecryptData))


def main():

    encrypt_and_decrypt = Encryption_and_Decryption()
    x = encrypt_and_decrypt.Encrypt("string to encrypt")
    print("encrypt data:", x)
    y = encrypt_and_decrypt.Decrypt(x)
    print("Decrypted Data:", y)

if __name__ == "__main__":
    main() 
