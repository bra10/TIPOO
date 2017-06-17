'''
Created on Dec 10, 2013

@author: Raul
'''
class FuzzySet():
    '''
    Fuzzy Ranges
    '''
    def fuzzification(self,value,membership_functions,fuzzy_values):
        self.__mf=membership_functions
        self.__x=value
        self.__size=len(self.__mf)
        self.__fuzzy_values=fuzzy_values
        result=[self.__mf[i].mf(self.__x) for i in range(self.__size)]
        #=======================================================================
        #DEBUG
        # print result
        # print result.index(max(result))
        # print self.__fuzzy_values[result.index(max(result))]
        #=======================================================================
        return self.__fuzzy_values[result.index(max(result))]
        
        