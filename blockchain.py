#implementing blockchain
import block

class BlockChain:
    def __init__(self):
        self.blocks = []
        self.swapblocks = []
        self.swapstart = 0
        g = genesisBlock()
        self.blocks.append(g)
    #TODO this is very rudementery change later
    def add(self,block,model):
        if block.validate(self.blocks[-1],model):
            self.blocks.append(block)
            self.swapstart += 1
        elif self.swapstart != 0:
            if block.validate(self.swapblocks[-1],model):
                self.swapblocks.append(block)
        elif self.swapstart == 0:
            for i in range(5):
                if block.validate(self.blocks[-1*(1+i)],model):
                    self.swapstart = i
                    self.swapblocks.append(block)
    #TODO optimize for speed not size
    def clearswap(self):
        if len(self.swapblocks) > self.swapstart:
            for i in range(len(self.swapblocks)):
                if i < self.swapstart:
                    self.blocks[-1*(1+i)] = self.swapblocks[i]
                else:
                    self.blocks.append(self.swapblocks[i])
        self.swapstart = 0
        self.swapblocks = []
    def last(self):
        return self.blocks[-1]
