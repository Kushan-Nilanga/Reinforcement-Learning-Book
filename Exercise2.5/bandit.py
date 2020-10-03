import numpy as np
from typing import List

class StationaryBandit:
    """
    This class defines a stationary bandit whose rewards are
    constant.
    """
    def __init__(self, arms:int):
        """
        initalise the bandit object
        - define arm (actions in reinforcement learning terms)
        - seeding values to generate reward according to random normal distribution
        """
        super(StationaryBandit, self)
        self.arms = [i for i in range(arms)]

        # saving seed values for future use
        self.__bandit_seed = numpy.random.randn(len(arms), 2)+2
        
        # Q true is the actual maximum reward that can be obtained
        self.__Q_true = np.prod(self.__bandit_seed, axis=1)
        
    def step(self, action:int):
        

    # def select_action(Q:np.array):
    #     assert Q.shape is not self.__Q_true.shape
    #     id = np.argmax(Q)
    #     probs = np.ones_like(Q) * self.__epsilon
    #     probs[id] = 1 - self.__epsilon
    #     probs = probs/probs.sum()
    #     return numpy.random.choice(arms, p=probs)

    def __repr__(self):
        """
        Represent bandit class with true values of the state and the arms
        """
        return f"<StationaryBandit[Q({self.__Q_true}), Arms({self.arms})]>"