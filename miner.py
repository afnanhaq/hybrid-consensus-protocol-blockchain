from random import choices
class Miner:
    def __init__(self, name, age = 1, mistakes = 1):
        self.name = name
        self.age = age
        self.mistakes = mistakes

    def mine(self, last_hash, sha_signature):
        #gets that specific miner to mine using proof of work algorithm
        return proof_of_work_algo(last_hash, sha_signature)

    def getName(self):
        return self.name

    def reset_age(self):
        self.age = 1




        
