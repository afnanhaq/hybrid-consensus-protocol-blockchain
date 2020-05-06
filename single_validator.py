from proof_of_work import *
from random import randint
from parameters import *

class Validator:
    def __init__(self, name, owl_coins_staked, coin_age = 1):
        self.name = name
        self.owl_coins_staked = owl_coins_staked
        self.coin_age = coin_age
        
    def getName(self):
        return self.name

    def vote_proof(self, last_hash, new_hash, proof):
        #a random reading for the simulation of what should happen
        #NEEDS ALOT OF WORK HERE
        value = randint(0, 100)
        if value < chance_a_validator_is_offline:
            print(self.name,"is offline")
            self.weight -= 5
            print(self.name,"has lost 5 units as punishment")
            return ("offline")
        elif chance_a_validator_is_offline < value <= (chance_a_validator_is_offline + chance_a_validator_rejects):
            print(self.name,"says no")
            return ("no")
        else:
            print(self.name,"says yes")
            return ("yes") 

    def reset_age(self):
        self.coin_age = 1
