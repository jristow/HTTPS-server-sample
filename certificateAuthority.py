import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


    
   
knownCerts = []
    
#Utility function that checks if a cert is in the list of known certs
def isKnown(cert):
    return cert in knownCerts
#Utility function to add a cert to the known certs list
def addKnown(cert):
    knownCerts.append(cert)
#Function that generates a key, currently will always return the same key.
#This is only for a demostration, do not use for production
def generateKey():
    return 'Sixteen byte key'

    
        
    
