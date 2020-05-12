#IMPORTED MODULES
from datetime import datetime
import time
from hashlib import sha256
from random import randint, choices
import copy


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
        self.transactions_per_block = []
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
        output = ''
        output += "START OF BLOCKCHAIN:" + '\n'
        output += '==========================================' + '\n'
        for index in range(len(self.blockchain)):
            output += (str(index) + 'th ' + str(self.blockchain[index]) + '\n') 
        output += '==========================================' + '\n'
        output += "ENF OF BLOCKCHAIN"
        return output

    def __len__(self):
        return len(self.blockchain)

    def add_validator(self, validator):
        #takes Validator object as input
        self.validator_list.add_validator(validator.name, validator.owl_coins_staked)

    def build_new_block(self):
        print("The reward for this block is", self.block_reward)
        #1. pick 5 validators from ValidatorList
        five_validator_winners = self.validator_list.pick_winners()
        print("Congratulations! The validators for this round are:")
        for validator in five_validator_winners.get_validators():
            print(validator.getName(), end=", ")
        print()
        #2. pick 10 miners from MinerList
        ten_miner_winners = self.miner_list.pick_winners()
        print("Congratulations! The miners for this round are: ")
        for miner in ten_miner_winners.get_miners():
            print(miner.getName(), end = ", ")
        print()
        #3. create a hash
        if len(self.blockchain) == 0:
            new_hash = create_hash("" + "".join(self.transactions_per_block[0]))
        else:
            new_hash = create_hash(self.blockchain[-1].getHash() + "".join(self.transactions_per_block[0]))
        print("Now the miners are mining...")
        #4. make "ALL" the miners mine the block
            #We get a generator with the next(generator_for_miners) being the 
            #fastest miner to solve the challenge
        generator_for_miners = ten_miner_winners.mine(self.last_block_hash(), new_hash)
        #5. announce that 1/10 miners won and start validating
        for place in range(1, 11):
            #winner_miner is a tuple with (integer proof, miner_object)
            winner_miner = next(generator_for_miners)
            print("Congratulations, miner", winner_miner[1].name, 'won the challenge and came in', place, 'place')
        #6. make the five random validators check the proof
        #break if consensus is reached so the else doesnt run. and the else just contains the slashing all of them
            block_has_consensus = broadcastBlock(five_validator_winners,self.last_block_hash(), new_hash, winner_miner[0])
            validators_said_yes = block_has_consensus[2]
            validators_said_no = block_has_consensus[3]
        #7. check consensus of block
        #8. if 3 yes 2 no, it passes, block reward is shared by 3 and 2 no's gets slashed. if 2 yes 3 no, 2 yes's lose 0.6% of their block reward. Continues till there is consensus
            if block_has_consensus[0]:
                print("This block was added")
                
                print("Validators get their reward:")
                for reward_validator in validators_said_yes:
                    reward_validator.get_reward_for_block(self.block_reward)
                print()
                if(len(validators_said_no) == 0):
                    print("No VALIDATORS get punished for this block, well done!")
                else:
                    print("Validators who disapproved the block get punished:")
                    for punish_slash_validator in validators_said_no:
                        print(punish_slash_validator.name, "gets slashed full amount of stake, which is",punish_slash_validator.owl_coins_staked)
                        punish_slash_validator.fully_slash()
                    
                print("Miner get rewarded:")
                winner_miner[1].win_block_reward(self.block_reward)
                print()
                #7. Add the block or reject the block using the block class and then appending it to self.blockchain
                #9. block reward time, 60%, 30% (6% each validator max), 10%
                
                #10. update block reward if needed
                self.update_block_reward_if_needed()
                
                five_validator_winners.reset_age()
                ten_miner_winners.reset_age()
                
                #reset reward for VALIDATORS
                for validator in five_validator_winners.get_validators():
                    validator.reward_percentage = 0.6
                
                block_to_add_to_chain = Block(new_hash, winner_miner[0], winner_miner[1], five_validator_winners, copy.deepcopy(self.transactions_per_block), self.last_block_hash())
                self.blockchain.append(block_to_add_to_chain)
                #Reset the ages of validators and miners
                self.transactions_per_block.clear()
                return
            elif(block_has_consensus[0] == False and block_has_consensus[1] == 'Proof of Work Incorrect'):
                

                #8. start all over again and slash all five validators when queue is empty
                print("This block was not added because hashing was done incorrectly, so we are going to choose a new miner")
                if (len(validators_said_yes) != 0):
                    print("Validators that approved the block are now going to be punished")
                    for punish_slash_validator in validators_said_yes:
                        print(punish_slash_validator.name, "gets slashed full amount of stake, which is",punish_slash_validator.owl_coins_staked)
                        punish_slash_validator.fully_slash()
                    
                print('Punish ' + winner_miner[1].name + ' by increasing mistakes count from', winner_miner[1].mistakes, 'to', winner_miner[1].mistakes + 1)
                winner_miner[1].mistakes += 1
                continue
            else: #block_has_consensus[0] == False and block_has_consensus[1] == 'Less than 3/5 of validators said yes'
                print("This block was not added because less than 3/5 of validators said yes")
                print("That means that majority of VALIDATORS said no, so the system will punish VALIDATORS who said yes")
                for punish_slash_validator in validators_said_yes:
                        punish_slash_validator.reward_percentage -= 0.006
                        print(punish_slash_validator.name, "gets slashed 0.006% of potential reward for this block, so the reward for",punish_slash_validator.name, "is now",str(punish_slash_validator.reward_percentage) + '%')
                #for punish_slash_validator in validators_said_yes:
                    #print(punish_slash_validator.name, "gets slashed 0.6% amount of stake, which is",punish_slash_validator.owl_coins_staked)
                    
                print()
        print()
        print()
        print()
        print("EVERYTHING WENT WRONG, ALL ARE MALICIOUS, COMMON???? THE WORLD IS A CRUEL PLACE I GUESS")

    def add_value(self, From, To, owls_coins_amount):
        time_stamp = str(datetime.now())[:19]
        #add value to new block
        self.transactions_per_block.append((str(owls_coins_amount), From, To,\
                                                                time_stamp))
            
        print(From.upper() + ' wants to send '+ str(owls_coins_amount) + \
              ' owls coins to ' + To.upper() + ' at ' + time_stamp)
        
        #after every 5 transactions, a new block is created
        if len(self.transactions_per_block) == amount_transactions_per_block:
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




    











        
