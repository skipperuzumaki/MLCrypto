#implementing blockchain
import block

class BlockChain:
    def __init__(self):
        self.blocks = []
        self.swapblocks = []
        self.swapstart = 0
        g = genesisBlock()
        self.blocks.append(g)
    #TODO this is still quite rudementery change later
    def add(self,block,validation):
        if (len(self.swapblocks) + self.swapstart) - len(self.blocks) >= 3:
            self.clearswap()
        if len(self.blocks) >= (int(block.id)):
            if block.validate(self.blocks[int(block.id) - 1],validation):
                if self.blocks[-1].id == int(block.id) - 1:
                    self.blocks.append(block)
                else:
                    self.clearswap()
                    self.swapstart = int(block.id) - 1
                    self.swapblocks.append(block)
        elif (len(self.swapblocks) + self.swapstart) >=  int(block.id):
            if block.validate(self.swapblocks[int(block.id) - 1],validation):
                if self.swapblocks[-1].id == int(block.id) - 1:
                    self.swapblocks.append(block)
                else:
                    self.clearswap()
                    self.add(block,validation)
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
