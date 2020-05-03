from proof_of_work import *
from random import randint
from parameters import *

class Validator:
    def __init__(self, name, weight, age = 1):
        self.name = name
        self.weight = weight
        self.age = age

    def mine(self, last_hash, sha_signature):
        #gets that specific person to mine using proof of work algorithm
        return proof_of_work_algo(last_hash, sha_signature)

    def vote_proof(self, last_hash, new_hash, proof):
        #a random reading for the simulation of what should happen
        #NEEDS ALOT OF WORK HERE
        value = randint(0, 100)
        if value < chance_a_validator_is_offline:
            print(self.name,"is offline")
            self.weight -= 5
            print(self.name,"has lost 5 units as punishment")
            return ("offline")
        elif chance_a_validator_is_offline < value <= (chance_a_validator_is_offline + chance_a_validator_lies):
            print(self.name,"says no")
            return ("no")
        else:
            print(self.name,"says yes")
            return ("yes") 

