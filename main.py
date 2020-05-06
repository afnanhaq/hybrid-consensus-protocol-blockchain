from blockchain import Blockchain, build_list_of_validators, build_list_of_miners
from list_of_all_validators import ValidatorList
from list_of_all_miners import MinerList
from parameters import *

def main():
    #initial_validators and initial_miners variables has been moved to parameters.py
    validator_list = build_list_of_validators(initial_validators)
    blockchain_validators = ValidatorList(validator_list)
    miner_list = build_list_of_miners(initial_miners)
    blockchain_miners = MinerList(miner_list)
    my_blockchain = Blockchain(blockchain_validators, blockchain_miners)    
    my_blockchain.add_value(5)
    my_blockchain.add_value(3)
    my_blockchain.add_value(13)
    my_blockchain.add_value(17)
    my_blockchain.add_value(13)
    
main()

