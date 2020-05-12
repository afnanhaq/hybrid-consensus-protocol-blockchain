from blockchain import Blockchain, build_list_of_validators, build_list_of_miners
from list_of_all_validators import ValidatorList
from list_of_all_miners import MinerList
from single_validator import Validator
from parameters import *
from random import randint
initial_users = [
        ("Afnan", 22, 3),
        ("David", 13),
        ("Monplaisir", 17),
        ("Claudia", 25),
        ("Adam", 33),
        ("James", 26, 2),
        ("Mercury", 22),
        ("Hope", 12, 2),
        ("John", 29, 4),
        ("Jacob", 18, 2),
        ("Jesus", 20,4),
        ("Nemo", 17),
        ("Campuchea", 25, 3),
        ("Colonel Sanders",35),
        ("Korean", 29),
        ("Japon", 33)
        ]
def main():
    #initial_validators and initial_miners variables has been moved to parameters.py
    validator_list = build_list_of_validators(initial_validators)
    blockchain_validators = ValidatorList(validator_list)
    miner_list = build_list_of_miners(initial_miners)
    blockchain_miners = MinerList(miner_list)
    my_blockchain = Blockchain(blockchain_validators, blockchain_miners)    
    number_of_transactions = 15
    new_validator = Validator("Remy", 22)
    my_blockchain.add_validator(new_validator)
    for transaction in range(number_of_transactions):
        sender = randint(0, len(initial_users) - 1)
        receiver = randint(0, len(initial_users) - 1)
        owl_coins = randint(0, 100)
        #Checking that sender and reciever are different users with a while
        while sender == receiver:
            receiver = randint(0, len(initial_users))
        my_blockchain.add_value(initial_users[sender][0]\
                                , initial_users[receiver][0]\
                                , owl_coins)
    print()
    print(my_blockchain)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

