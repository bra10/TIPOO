'''
Created on Dec 11, 2013

@author: Raul
'''
from FuzzySet import FuzzySet as fuzzy_set
from MembershipFunction import Gaussian as gaussian, Sigmoid as sigmoid, \
    Triangle as triangle


class TestTime(fuzzy_set):
    '''
    Test Time Fuzzy Set
    '''
    fuzzy_values={0:"Low",1:"Medium",2:"High"}
    membership_functions=[]
    mf_sigmoidl=triangle(-1.54, 0.349, 1)
    membership_functions.append(mf_sigmoidl)
    mf_gaussian=gaussian(0.7, 3)
    membership_functions.append(mf_gaussian)
    mf_sigmoidr=sigmoid(1.111, 3.22)
    membership_functions.append(mf_sigmoidr)
    
    def fuzzy(self,x):
        return self.fuzzification(x, self.membership_functions, self.fuzzy_values)        