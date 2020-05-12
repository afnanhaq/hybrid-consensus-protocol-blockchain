from single_validator import *

class ValidatorList:
    #validators will be a list of Validator objects
    def __init__(self, validators):
        self.validators = validators
    
    def __len__(self):
        return len(self.validators)

    def get_validators(self):
        return self.validators

    def add_validator(self, name, owl_coins_staked):
        if owl_coins_staked > 50:
            print("Too many owl coins staked by", name)
            return
        new_validator = Validator(name, owl_coins_staked, 1)
        print("Validator with the name",new_validator.name,"has been added")
        self.validators.append(new_validator)

    def pick_winners(self):
        #weighted random based on amount staked (weight) and age
        #add parameters here???
        while True:
        #this While loop exists because choices() can do repeats
            validators = choices(self.validators, [validator.owl_coins_staked
                                              * (0.5 * validator.coin_age)
                                              for validator in self.validators],k=5)
            repeats = 0
            for elem in validators:
                if validators.count(elem) > 1:
                    repeats += 1
            if repeats == 0:
                return ValidatorList(validators)
            
    def reset_age(self):
        for validator in self.validators:
            validator.reset_age_single()
