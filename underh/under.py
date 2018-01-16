import random
import pickle
class Game():
    def __init__(self):
        pass

    def _ngen(self):
        g = random.randint(0, 1)
        if g:
            with open('data/male-first-names','rb') as fileObject:
                fnames = pickle.load(fileObject)
        else:
            with open('data/female-first-names','rb') as fileObject:
                fnames = pickle.load(fileObject)
        with open('data/last-names','rb') as fileObject:
                lnames = pickle.load(fileObject)
        yield random.choice(fnames), random.choice(lnames)





class Hand(Game):
    def __init__(self):
        '''If you have over 15 you get greed
        if you have over 4 suspicion you get busted'''
        self.holding = [Money(),Money(), 
                        Food(), Food(), 
                        Cultist(),Cultist(),
                        Prisoner(), Prisoner()]