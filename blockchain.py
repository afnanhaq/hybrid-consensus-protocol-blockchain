#IMPORTED MODULES
from datetime import datetime
import time
from hashlib import sha256
from random import randint, choices

"""
THINGS TO DO (FROM BEFORE OUR DISCUSSION TODAY)
1. Increment the age by day for each new block added
2. Actually add the block if there is consensus using the Block class
3. Voting mechanism/Vote class
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
from miner import *
from list_of_all_miners import *

#BLOCKCHAIN CLASS
class Blockchain:
    def __init__(self, validators, miners):
        print("We are starting at block 4096")
        self.blockchain = []
        self.current_block = []
        self.validator_list = validators
        self.miner_list = miners
        self.block_reward = 50

    def update_block_reward_if_needed(self):
        if len(self) % 24 == 0:
            self.block_reward += 6
        
    def last_block_hash(self):
        #means blockchain is empty
        if len(self) == 0:
            return ""
        else:
            return self.blockchain[-1].getHash()

    def __repr__(self):
        print("The blockchain is built as follows:")
        for block in blockchain:
            print(block)       

    def __len__(self):
        return len(self.blockchain)

    def add_validator(self, validator):
        #takes Validator object as input
        self.validator_list.add_validator(validator)

    def build_new_block(self):
        #1. pick 5 validators from ValidatorList
        validators = self.validator_list.pick_winners()
        print("Congratulations! The validators for this round are:")
        for validator in validators.get_validators():
            print(validator.getName(), end=", ")
        print()
        #2. pick 10 miners from MinerList
        miners = self.miner_list.pick_winners()
        print("Congratulations! The miners for this round are: ")
        for miner in miners.get_miners():
            print(miner.getName(), end = ", ")
        print()
        #3. create a hash
        if len(self.blockchain) == 0:
            new_hash = create_hash("" + "".join(self.current_block))
        else:
            new_hash = create_hash(self.blockchain[-1].getHash() + "".join(self.current_block))
        #EVERYTHING BELOW IS MOSTLY FOR U TO DO
        print("Now the miners are mining...")
        #4. make "ALL" the miners mine the block
        queue = miners.mine(self.last_block_hash(), new_hash)
        #5. put the winners in a queue somehow
        print("The broadcasted proof of work by the miner x is",queue) #the broadcasted proof of work by x is proof
        #6. make the five random validators check the proof
        
        #write while loop like while length of queue != 0 like a while/else statement
        #break if consensus is reached so the else doesnt run. and the else just contains the slashing all of them
        block_has_consensus = broadcastBlock(self.validator_list.get_validators(),self.last_block_hash(), new_hash, proof)
        #7. check consensus of block
        #8. if 3 yes 2 no, it passes, block reward is shared by 3 and 2 no's gets slashed. if 2 yes 3 no, 2 yes's lose 0.6% of their block reward. Continues till there is consensus
        if block_has_consensus:
            print("This block was added")
            #7. Add the block or reject the block using the block class and then appending it to self.blockchain
            #9. block reward time, 60%, 30% (6% each validator max), 10%
            
            #10. update block reward if needed, I TOOK CARE OF THIS
            self.update_block_reward_if_needed()
        else:
            #8. start all over again and slash all five validators when queue is empty
            print("This block was not added as all miners failed")
        #11. remove age parameters from calculations for all participants, I ALSO TOOK CARE OF THIS 
            self.reset_ages(miners, validators)


    def reset_ages(miners, validators):
        for miner in miners:
            miner.reset_age()
        for validator in validators:
            validator.reset_age()

    def add_value(self, value):
        #add value to new block
        self.current_block.append(str(value))
        print("Added value of",value,"to potential block")
        #after every 5 transactions, a new block is created
        if len(self.current_block) == transactions_per_block:
            print("Creating new block now")
            self.build_new_block()

#users_data will contain a list of tuples as shown in the main() function
def build_list_of_validators(data):
    validator_list = []
    for user in data:
        if len(user) == 2:
            validator = Validator(user[0], user[1])
        else:
            validator = Validator(user[0], user[1], user[2])
        validator_list.append(validator)
    return validator_list

def build_list_of_miners(data):
    miner_list = []
    for user in data:
        if len(user) == 2:
            miner = Miner(user[0], user[1])
        else:
            miner = Miner(user[0], user[1], user[2])
        miner_list.append(miner)
    return miner_list


    











        
