# Cryptgram Project

## Overview

The **Cryptgram** project is a secure social media platform where users can post messages, with their content being encrypted before storage and transmission. The system ensures the privacy and integrity of user data by encrypting posts, saving them in a secure database, and sending encrypted data to a server for further processing.

The application leverages encryption algorithms, database management with SQLite, socket communication, and a Flask-based web interface to display the posts.

## Project Components

### 1. **Encryption and Decryption**
   - Data is encrypted and decrypted using a custom encryption algorithm implemented in the `Encryption_and_Decryption` class.
   - The encryption utilizes an XOR operation with a constant cipher, followed by Base64 encoding for safe text transmission.

### 2. **Client-Side (Share Post)**
   - The `share_post` class is responsible for handling the post creation process. It takes the user input for the post and username, encrypts the data, and then stores it in a JSON file.
   - The `Client` class manages communication with the server, sending the encrypted post data over a socket connection.

### 3. **Server-Side**
   - The `Server` class listens for incoming connections from the client. It receives encrypted post data, decrypts it, and stores it in a SQLite database (`db_CG`).
   - The server is also capable of responding to basic "ping" and "pong" messages to check connectivity.

### 4. **Database Management**
   - The `database_CryptNet` class handles the SQLite database, where posts are stored. It includes functions to insert new posts, select posts by `postID`, retrieve all posts, and delete posts.
   - The database schema contains three fields: `postID` (primary key), `username`, and `post`.

### 5. **Web Interface**
   - The Flask web app provides a front-end for displaying posts. The posts are retrieved from the database and shown in a webpage (`CRYPTGRAM.html`).
   - The app uses SQLite to fetch the latest posts, and the Flask routes serve the data on a webpage.

## Technologies Used

- **Python**: Main programming language used for the backend and logic.
- **Flask**: Web framework used to create a web interface for displaying posts.
- **SQLite**: Lightweight relational database used to store user posts.
- **Socket Programming**: For communication between client and server using the `socket` module.
- **Encryption Algorithms**: Custom XOR-based encryption algorithm for securing posts.
- **Base64 Encoding**: Used to encode encrypted data for safe transmission.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptgram.git
   cd cryptgram

