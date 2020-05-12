from datetime import datetime

class Block:
    def __init__(self, Hash,proof, winner_miner, five_validators, transactions, prevHash = ''):
        DATE = datetime.now()
        self.timestamp = str(DATE)
        self.prevHash = prevHash
        self.transactions = transactions
        self.hash = Hash
        self.winner_miner = winner_miner
        self.proof = proof

    def __str__(self):
        output = ''
        output += ("Block" + " was mined on date " + str(self.timestamp)[:10] + " at " + str(self.timestamp)[11:19] + " by miner " + self.winner_miner.name + " and contains the following transactions:" + '\n')
        for value in self.transactions:
            output += value[1].upper() + ' sent ' + value[2].upper() + ' ' + value[0] + ' owl_coins ' + 'on date ' + value[3][:10] + ' at ' + value[3][11:19] + '\n'
        return output

    def getHash(self):
        return self.hash
    
    
    
