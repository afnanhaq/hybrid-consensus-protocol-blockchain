from proof_of_work import *
from random import random
from parameters import *

class Validator:
    def __init__(self, name, weight, age = 0):
        self.name = name
        self.weight = weight
        self.age = age

    def mine(self, last_hash, sha_signature):
        return proof_of_work_algo(last_hash, sha_signature)

    def vote_proof(last_hash, new_hash, proof):
        value = random()
        if value < chance_a_validator_is_offline:
            print(self.name,"is offline")
            self.weight -= 5
            print(self.name,"has lost 5 units as punishment")
            return (0, "offline")
        elif chance_a validator_is_offline < value < chance_a_validator_is_offline + chance_a_validator_lies:
            print(self.name,"says no")
            return 
            
            
            
            
        #if value <  

