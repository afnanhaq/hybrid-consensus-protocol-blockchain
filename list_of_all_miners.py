from miner import *

class MinerList:
    def __init__(self, list_of_miners):
        self.list_of_miners = list_of_miners

    def get_miners(self):
        return self.list_of_miners

    def add_miner(self, name, age = 1, mistakes = 1):
        new_miner = Miner(name, age, mistakes)
        print("The miner with the name", new_miner.name,"has been added")
        self.list_of_miners.append(new_miner)

    def mine(self, last_block_hash, new_hash):
        print("David will write a function in list_of_all_miners.py using miners.py")
        return "wow"

    def pick_winners(self):
        #weighted random based on mistakes
        #this While loop exists because choices() can do repeats
        while True:
            miners = choices(self.list_of_miners,
                             [(1/miner.mistakes)*miner.age for miner in self.list_of_miners],
                             k = 10)
            repeats = 0
            for elem in miners:
                if miners.count(elem) > 1:
                    repeats += 1
            if repeats == 0:
                return MinerList(miners)
        
        
