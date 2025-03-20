import sqlite3

class database_CryptNet:
    
    def __init__(self, tablename="db_CryptNet", postID="postID", username="username", post="post"):
        
        self.__tablename = tablename # hidden featuers
        self.__postID = postID
        self.__username = username
        self.__post = post
        
        conn = sqlite3.connect('db_CG') # Create a new SQLITE file. The command connects to an existing file, 
                                        # and if it does not exist, it creates a file.

        
        print("open database successfully")

        # Creating a table with does not exist, defining the properties of the table.
        str = "CREATE TABLE IF NOT EXISTS " + tablename + " ("
        str += self.__postID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
        str += self.__username + " TEXT NOT NULL, "
        str += self.__post + " TEXT NOT NULL )"
        
        conn.execute(str) # Execution of the command that appears in STR.
        print("table created successfully")
        conn.commit() # Saving the changes in the table.
        conn.close() # Closing a database connection.
        
    def Insert_data(self, username, post):

        conn = sqlite3.connect('db_CG')

        # Parameterized SQL query
        str_insert = f"INSERT INTO {self.__tablename} ({self.__username}, {self.__post}) VALUES (?, ?)"
        print("str_insert")
        
        conn.execute(str_insert, (username, post))
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_post_by_postID(self, postID):
        
        conn = sqlite3.connect('db_CG')
        
        # Parameterized SQL query
        str_query = f"SELECT {self.__postID}, {self.__username}, {self.__post} FROM {self.__tablename} WHERE {self.__postID} = ?"
        
        cursor = conn.execute(str_query, (postID,)) # The data of the query save in "corsur".
        
        # The loop run on the rows of the query data and print the info.
        for row in cursor:
            print("postID = ", row[0])
            print("username = ", row[1])
            print("post = ", row[2])
        
        print("operation done successfully")    
        conn.close()
            
             
    def get_all_post(self):
        
        conn = sqlite3.connect('db_CG')
        
        # Parameterized SQL query
        str_query = f"SELECT * FROM {self.__tablename}"
        
        cursor = conn.execute(str_query) # The data of the query save in "corsur".
        
        # The loop run on the rows of the query data and print the info.
        for row in cursor:
            print("------------------")
            print("postID = ", row[0])
            print("username = ", row[1])
            print("post = ", row[2])
            print("------------------")
        
        print("operation done successfully")    
        conn.close()        


    def delete_post_by_postID(self, postID):
        
        conn = sqlite3.connect('db_CG')
        
        # Parameterized SQL query
        str_query = f"DELETE FROM {self.__tablename} WHERE {self.__postID} = ?"
        
        conn.execute(str_query, (postID,))
        conn.commit()
        conn.close()
        print("delete successfully")





def main():

    db = database_CryptNet()

    db.Insert_data("Alice", "Just finished my encryption script! 🔐")
    db.Insert_data("Bob", "Does anyone here work on Flask + SQLite?")
    db.Insert_data("Charlie", "Security is a process, not a product.")
    db.Insert_data("David", "Cybersecurity tip: Never reuse passwords! 🔑")
    db.Insert_data("Eve", "This platform is amazing for private discussions.")
    db.Insert_data("Frank", "Hashing or encryption? When to use which? 🤔")
    db.Insert_data("Grace", "Looking for a team to build a privacy-focused app.")
    db.Insert_data("Heidi", "Quantum computers might break encryption soon! 🚀")
    db.Insert_data("Ivan", "Zero-trust security is the future of authentication.")
    db.Insert_data("Judy", "Your data is valuable. Protect it. 🔒")
    db.Insert_data("Kevin", "Trying out PGP for secure communication.")
    db.Insert_data("Laura", "Open-source encryption tools are essential! 💡")
    db.Insert_data("Mallory", "Don't trust—verify. Always check certificates! ✅")
    db.Insert_data("Nina", "AES-256 is strong, but how do you manage your keys?")
    db.Insert_data("Oscar", "Metadata exposes more than you think. Be careful.")
    
    #db.select_post_by_postID(69)
    #db.get_all_post()
    #db.delete_post_by_postID(4)
    #db.get_all_post()


if __name__ == '__main__': 
    main()




