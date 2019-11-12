#Defining blocks
import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class Block:
    def __init__(self,prev,transactions):
        self.id = bin(int(prev.id)+1)
        self.timestamp = bin(datetime.now())
        self.transactions = bin(transactions)
        self.prevhash = prev.hash
        self.msghash = msg_hash()
        self.traindata = b''
        self.improvement = b''
        self.hash = b''
    def msg_hash(self):
        digest = hashes.Hash(hashes.SHA512(),backend = default_backend())
        digest.update(self.id)
        digest.update(self.timestamp)
        digest.update(self.transactions)
        digest.update(self.prevhash)
        return digest.finalize()
    def secure(self,model):
        value = []
        for i in range(0,512,4):
            value.append(self.msghash[i:i+4])
        self.traindata , self.improvement = model.use(value)
        digest = hashes.Hash(hashes.SHA512(),backend = default_backend())
        digest.update(self.msghash)
        digest.update(self.traindata)
        digest.update(self.improvement)
        self.hash = digest.finalize()
    def validate(self,prev,model):
        if (self.prevhash != prev.hash):
            return False
        if (self.msghash != self.msg_hash()):
            return False
        if (self.improvement != model.check(self.traindata,prev)):
            return False
        digest = hashes.Hash(hashes.SHA512(),backend = default_backend())
        digest.update(self.msghash)
        digest.update(self.traindata)
        digest.update(self.improvement)
        if (self.hash != digest.finalize()):
            return False
        return True

class genesisBlock:
    def __init__(self):
        self.id = bin(0)
        digest = hashes.Hash(hashes.SHA512(),backend = default_backend())
        digest.update(b'Start')
        self.hash = digest.finalize()
