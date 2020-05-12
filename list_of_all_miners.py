from miner import *
import concurrent.futures
import time
import random


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
        #10 miners mine simultaneously by using multiprocessing
        #1. Define ProcessPoolExecutor, where processes will be created and executed
        with concurrent.futures.ProcessPoolExecutor() as executor:
            #2. ten_miners_working_processes ---> list of 10 processes - 10 miners mining
            ten_miners_working_processes = []
            #3. miners_process_mapping ---> stores address of processes as a key
            #                               and the miner associated with this 
            #                               process as value
            # Step 3 is done to be able to retrieve the miner who finishes the
            #                               job first
            miners_process_mapping = dict()
            #4. Go though the all 10 miners and
            # random_time_miner_sleeps ---> simulate that some miners will have
            # better GPU's than others, so they will solve the challenge faster
            random_time_miner_sleeps = random.random() #returns a float from 0 to 1
            for miner in self.list_of_miners:
                #5. Start a process for each miner
                process_miner = executor.submit(miner.mine, last_block_hash, new_hash, random_time_miner_sleeps)
                #6. Store this process in a list
                ten_miners_working_processes.append(process_miner)
                #7. Build the dict described in step 3
                miners_process_mapping[process_miner.__repr__()[11:25]] = miner
            #8. Whoever from miners finishes first yield
            for winner in concurrent.futures.as_completed(ten_miners_working_processes):
                yield (winner.result(), miners_process_mapping[winner.__repr__()[11:25]])

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
            
    def reset_age(self):
        for miner in self.list_of_miners:
            miner.reset_age_single()
            
# initial_miners = [
#     ("Venus", 1),
#     ("Theodore",3),
#     ("Jacobson",3, 2),
#     ("February", 1),
#     ("Kyrgyztan",2),
#     ("Jeremiah", 1),
#     ("Lover", 1),
#     ("Hopeful",3,3),
#     ("Lol", 1),
#     ("Hebrew", 1),
#     ]
# def build_list_of_miners(data):
#     miner_list = []
#     for user in data:
#         if len(user) == 2:
#             miner = Miner(user[0], user[1])
#         else:
#             miner = Miner(user[0], user[1], user[2])
#         miner_list.append(miner)
#     return miner_list
# # miner_list = build_list_of_miners(initial_miners)
# # test = MinerList(miner_list)

# # x = test.mine('947c73cff4a8229837bf48dde21053586ec46274f5a67914d09a4fcab6c381d1','6980a80d5168cc83fceef88e5382fdd3821dc11d2c99d6f03d6645edcc10e3ad')
# # print(next(x))

#         #LAST 947c73cff4a8229837bf48dde21053586ec46274f5a67914d09a4fcab6c381d1
        
#         #NEW 6980a80d5168cc83fceef88e5382fdd3821dc11d2c99d6f03d6645edcc10e3ad
        
