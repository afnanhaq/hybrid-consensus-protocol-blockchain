from proof_of_work import *
from random import randint
from parameters import *
from hashlib import sha256

class Validator:
    def __init__(self, name, owl_coins_staked, coin_age = 1):
        self.name = name
        self.owl_coins_staked = owl_coins_staked
        self.coin_age = coin_age
        self.reward_percentage = 0.06
        
    def getName(self):
        return self.name
    

    def vote_proof(self, last_hash, new_hash, proof):
        #a random reading for the simulation of what should happen
        #NEEDS ALOT OF WORK HERE
        value = randint(0, 100)
        
        if not checkProofOfWork(last_hash, new_hash, proof):
            if (value < chance_proof_of_work_incorrect_but_validator_say_yes):
                return ('Proof of Work Incorrect but validator is malicious')
            else:
                return ('Proof of Work Incorrect')
        
        if value < chance_a_validator_is_offline:
            print(self.name,"owl_coins destroyed due to being offline")
            self.owl_coins_staked = 0
            return ("offline")
        elif chance_a_validator_is_offline < value <= (chance_a_validator_is_offline + chance_a_validator_rejects):
            print(self.name,"says no")
            return ("no")
        else:
            print(self.name,"says yes")
            return ("yes")

    def reset_age_single(self):
        self.coin_age = 1
        
    def fully_slash(self):
        self.owl_coins_staked = 0
    
    def get_reward_for_block(self, block_reward):
        reward = block_reward * self.reward_percentage
        self.owl_coins_staked += reward
        print(self.name + " VALIDATOR got reward of " + str(reward) + " owl coins")

def checkProofOfWork(last_hash, new_hash, proof):
        input_to_sha256 = (last_hash + str(proof) + new_hash).encode()
        check_hash = sha256(input_to_sha256).hexdigest()
        if (check_hash[:4] == '0000'):
            return True
        else:
            return False
