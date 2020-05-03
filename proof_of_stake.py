from single_validator import *

def broadcastBlock(lst_of_validators, last_hash, new_hash, proof):
    total_validators = len(lst_of_validators)
    votes = 0
    says_no = []
    says_yes = []
    for validator in lst_of_validators:
        vote, value = validator.vote_proof(last_hash, new_hash, proof)
        if value == "no":
            says_no.append(validator)
            votes += 0
        elif value == "yes:
            says_yes.append(validator)
            votes += 1
    if votes > total_validators*(2/3):
        
        
        

        
        
