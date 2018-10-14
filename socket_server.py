import socket
from AEScipher import AESCipher
from Crypto.Hash import SHA256


#Initializing key value and certificate information
key = 'Sixteen byte key'
#iv = Random.new().read(AES.block_size)
#cipher = AES.new(key, AES.MODE_CFB, iv)
certword = 'notsosecretpassword'
hasher = SHA256.new(certword.encode('utf-8'))
cert = hasher.digest()

#Creating the socket
s = socket.socket()
print("Socket successfully created")
port = 9500
s.bind(('',port))
print("socket binded to %s" %(port))

#Setting the socket to listen
s.listen(5)
print('socket is listening')

#Accepts a connection, sends the certificate and recieves some encrypted
#information if the certificate is valid.
while True:

    c, addr = s.accept()
    c.send(cert)
    message = c.recv(128)
    newCipher = AESCipher(key)
    decryptedMsg = newCipher.decrypt(message)
    print(decryptedMsg)
    c.send(newCipher.encrypt('Yes, you do.'))

    c.close
    
