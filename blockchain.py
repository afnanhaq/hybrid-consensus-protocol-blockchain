#IMPORTED MODULES
from datetime import datetime
import time
from hashlib import sha256
from random import randint, choices

"""
THINGS TO DO
1. Increment the age by day for each new block added
2. Actually add the block if there is consensus using the Block class
3. Voting mechanism/Vote class
4. "Printing" the blockchain if someone wants to see it
5. Slashing a person if they vote twice
6. self.current_block has to empty list after build_new_block is called
7. add parameters for age and weight in pick_winners() in ValidatorList
8. IMPORTANT: vote_proof() is the main thing for simulating consensus and it is primitive now
9. Related to 8, broadcastBlock() in proof_of_stake.py is primitive
"""


#MY_OTHER_FILES
from proof_of_work import *
from single_validator import *
from parameters import *
from proof_of_stake import *
from list_of_all_validators import *
from block import *
from vote import *

#BLOCKCHAIN CLASS
class Blockchain:
    def __init__(self, validators):
        self.blockchain = []
        self.current_block = []
        self.validator_list = validators

    def last_block_hash(self):
        #means blockchain is empty
        if len(self) == 0:
            return ""
        else:
            return self.blockchain[-1].getHash()

    def __len__(self):
        return len(self.blockchain)

    def add_validator(self, validator):
        #takes Validator object as input
        self.validator_list.add_validator(validator)

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
        block_has_consensus = broadcastBlock(self.validator_list.get_validators(),self.last_block_hash(), new_hash, proof)
        #5. check consensus of block
        if block_has_consensus:
            print("This block was added")
        else:
            print("This block was not added")

    def add_value(self, value):
        #add value to new block
        self.current_block.append(str(value))
        print("Added value of",value,"to potential block")
        #after every 5 transactions, a new block is created
        if len(self.current_block) == transactions_per_block:
            print("Creating new block now")
            self.build_new_block()

#users_data will contain a list of tuples as shown in the main() function
def build_list_of_validators(users_data):
    validator_list = []
    for user in users_data:
        validator = Validator(user[0], user[1])
        validator_list.append(validator)
    return validator_list

#MAIN
def main():
    initial_users = [
        ("Afnan", 22, 3),
        ("David", 13),
        ("Monplaisir", 17, 1),
        ("Claudia", 25, 1),
        ("Adam", 33, 1),
        ("James", 26, 2),
        ("Mercury", 22, 1),
        ("Hope", 12, 2),
        ("John", 29, 4),
        ("Jacob", 18, 2),
        ("Jesus", 20,4)
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
    











        
