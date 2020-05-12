from random import choices, randint
from proof_of_work import *
import time
from parameters import *
class Miner:
    def __init__(self, name, age = 1, mistakes = 1):
        self.name = name
        self.age = age
        self.mistakes = mistakes
        self.reward_wallet = 0

    def mine(self, last_hash, sha_signature, random_wait):
        time.sleep(random_wait)
        mining_wrong_hash = randint(0,100)
        #Chance that a miner get the hash incorrectly
        if (mining_wrong_hash < chance_a_miner_gets_wrong_hash_for_block):
            return 'Jibberish'
        #gets that specific miner to mine using proof of work algorithm
        return proof_of_work_algo(last_hash, sha_signature)

    def getName(self):
        return self.name

    def reset_age_single(self):
        self.age = 1
        
    def win_block_reward(self, block_reward):
        reward = block_reward * 0.60
        self.reward_wallet += reward
        print(self.name + " MINER got reward of " + str(reward) + " owl coins")




        
