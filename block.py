from datetime import datetime

class Block:
    def __init__(self, Hash, miners, validators, transactions, index = 0, prevHash = ""):
        DATE = datetime.now()
        self.index = index
        self.timestamp = str(DATE)
        self.prevHash = prevHash
        self.miner = miner
        self.transactions = transactions
        self.hash = Hash

    def __repr__(self):
        print("Block",self.index,"was mined on date",self.timestamp,"by",self.miner,"and contains the following transactions:")
        self.getTransactions()

    def getTransactions(self):
        for value in self.transactions:
            print(value)

    def getHash(self):
        return self.Hash
