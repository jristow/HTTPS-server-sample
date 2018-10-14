import socket
from Crypto.Hash import SHA256
import certificateAuthority
from AEScipher import AESCipher 


#Initializing the certificateAuthority application
ca = certificateAuthority
#Adding the "certificate" to the known values in the certificate authority
certword = 'notsosecretpassword'
hasher = SHA256.new(certword.encode('utf-8'))
cert = hasher.digest()
ca.addKnown(cert)

#Initializing the socket
s = socket.socket()
port = 9500

#Attempting a connection to the server
s.connect(('127.0.0.1', port))
#Receiving a certificate from the server
cert2 = s.recv(1024)
#Checking if the cert is known by the certificate authority
if ca.isKnown(cert2):
    #If the cert is known, encrypt a message and send it
    key = ca.generateKey()
    
    newCipher = AESCipher(key)
    msg = newCipher.encrypt('Do I know you?')
    s.send(msg)
    response = s.recv(1024)
    print(newCipher.decrypt(response))
    
    s.close
#If the certificate is not known, send Goodbye and close the connection
else:
    s.send(bytes('Goodbye','utf-8'))
    s.close 
