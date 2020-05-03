from datetime import datetime
import time
from hashlib import sha256
from random import randint, choices



#MY_OTHER_FILES
from proof_of_work import *
from single_validator import *
from parameters import *
from proof_of_stake import *

class Blockchain:
    def __init__(self, validators):
        self.blockchain = []
        self.current_block = []
        self.validator_list = validators

    def last_block_hash(self):
        if len(self) == 0:
            return ""
        else:
            return self.blockchain[-1].getHash()

    def __len__(self):
        return len(self.blockchain)

    def build_new_block(self):
        #1. pick a new winner from ValidatorList
        winner = (self.validator_list.pick_winner())[0]
        print("Congratulations! The winner is", winner.name)
        #2. create a hash
        if len(self.blockchain) == 0:
            new_hash = create_hash("" + "".join(self.current_block))
        else:
            new_hash = create_hash(self.blockchain[-1].getHash() + "".join(self.current_block))
        #3. make winner mine the block
        proof = winner.mine(self.last_block_hash(), new_hash)
        #4. broadcast the block and get everyone to check it
        print("The broadcasted proof of work is",proof)
        block_has_consensus = broadcastBlock(self.validator_list.get_validators()
                                             , self.last_block_hash(), new_hash, proof)
        
        
        
        #1. pick a new winner from ValidatorList
        #create a hash
        #2. make that winner mine the block
        #3. get everyone to check the hash
        #4. if it works, then add that block, if not, then reject the block

    def add_value(self, value):
        self.current_block.append(str(value))
        print("Added value of",value,"to potential block")
        if len(self.current_block) == transactions_per_block:
            print("Creating new block now")
            self.build_new_block()
              

    def check_vote_results(self):
        pass

    def slash(self):
        pass

class ValidatorList:
    #validators will be a list of validator objects
    def __init__(self, validators):
        self.validators = validators

    def get_validators(self):
        return self.validators

    def add_validator(self, validator):
        self.validators.append(validator)
        self.total_weight += validator.weight

    def pick_winner(self):
        value = choices(self.validators, [self.validators[i].weight * (0.5 * self.validators[i].age)
                                          for i in range(len(self.validators))],k=1)
        return value
        
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
        

class Vote:
    def __init__(self, currentBlockHash, previousBlockHash, ):
        self.currentBlockHash = currentBlockHash
        self.previousBlockHash = previousBlockHash
        self.user = user



#users_data will contain a list of tuples as shown in the main() function
def build_list_of_validators(users_data):
    validator_list = []
    for user in users_data:
        validator = Validator(user[0], user[1])
        validator_list.append(validator)
    return validator_list





def main():
    initial_users = [
        ("Afnan", 22, 3),
        ("David", 13),
        ("Monplaisir", 17, 1),
        ("Claudia", 25, 1)
        ]
    validator_list = build_list_of_validators(initial_users)
    blockchain_validators = ValidatorList(validator_list)
    my_blockchain = Blockchain(blockchain_validators)    
    my_blockchain.add_value(5)
    my_blockchain.add_value(3)
    my_blockchain.add_value(13)
    my_blockchain.add_value(17)
    my_blockchain.add_value(13)
    
main()
    











        
