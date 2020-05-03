from single_validator import *

def broadcastBlock(lst_of_validators, last_hash, new_hash, proof):
    total_validators = len(lst_of_validators)
    #get a count for how many votes it has
    votes = 0
    #we can somehow use these arrays containing who says yes and no to figure out
    #who should be punished or rewarded
    says_no = []
    says_yes = []
    for validator in lst_of_validators:
        value = validator.vote_proof(last_hash, new_hash, proof)
        if value == "no":
            says_no.append(validator)
            votes += 0
        elif value == "yes":
            says_yes.append(validator)
            votes += 1
    #check if two/thirds of all validators agree
    if votes > total_validators*(2/3):
        return True
    else:
        return False
    
        
        
        

        
        
