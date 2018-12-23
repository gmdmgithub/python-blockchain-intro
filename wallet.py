from Crypto.PublicKey import RSA
import Crypto.Random
import binascii

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = self.generate_key()
        
    def generate_key(self):
        private_key = RSA.generate(2048,Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER').decode('asci')),
        binascii.hexlify(public_key.exportKey(format='DER').decode('asci')))
        