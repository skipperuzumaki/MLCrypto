# Mining blocks
import blockchain

class miner:
    def __init__(self,Keys,Sockets):
        self.id = keys[0] # Public_key
        self.privatekey = keys[1]
        self.bchain = self.RBchain()
    def mine(self,model):
        transactions = self.recieve()
        bl = Block(self.bchain.last(),transactions)
        bl.msg_hash()
        bl.miner = self.id
        bl.secure(model)
        self.transmit(bl)
    def recieve(self):
        pass # recieve transactons and validate them
    def RBchain(self):
        pass # recieve blockchain
    def transmit(self):
        pass # transsmit block
        
        
