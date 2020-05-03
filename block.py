from datetime import datetime

class Block:
    def __init__(self, Hash, validator = "", index = 0, prevHash = ""):
        DATE = datetime.now()
        self.index = index
        self.timestamp = str(DATE)
        self.prevHash = prevHash
        self.validator = validator
        self.hash = Hash

    def getHash(self):
        return self.Hash
