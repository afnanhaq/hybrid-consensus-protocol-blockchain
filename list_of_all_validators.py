from single_validator import *

class ValidatorList:
    #validators will be a list of Validator objects
    def __init__(self, validators):
        self.validators = validators

    def get_validators(self):
        return self.validators

    def add_validator(self, validator):
        self.validators.append(validator)
        self.total_weight += validator.weight

    def pick_winner(self):
        #weighted random based on amount staked (weight) and age
        #add parameters here???
        value = choices(self.validators, [self.validators[i].weight * (0.5 * self.validators[i].age)
                                          for i in range(len(self.validators))],k=1)
        return value
