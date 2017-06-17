'''
Created on Dec 10, 2013

@author: Raul
'''
import math


class Trapezoid():
    '''
    Trapezoid Membership function
    '''

    def __init__(self, a, b, c, d):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        
    def mf(self,x):
        if x<=self.__a:
            return 0
        elif x>self.__a and x<=self.__b:
            return (x-self.__a)/(self.__b-self.__a)
        elif x>self.__b and x<=self.__c:
            return 1
        elif x>self.__c and x<=self.__d:
            return (self.__d-x)/(self.__d-self.__c)
        else:
            return 0
        

class Triangle():
    '''
    Triangle Membership Function
    '''
    
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
        
    def mf(self,x):
        if x<=self.__a:
            return 0
        elif x>self.__a and x<=self.__b:
            return (x-self.__a)/(self.__b-self.__a)
        elif x>self.__b and x<=self.__c:
            return (self.__c-x)/(self.__c-self.__b)
        else:
            return 0
        
class Gaussian():
    '''
    Gaussian membership Function
    '''
    
    def __init__(self,sigma,a):
        self.__a=a
        self.__sigma=sigma
        
    def mf(self,x):
        return math.exp((-1*(x-self.__a)**2)/((2*self.__sigma)**2))
   

class Sigmoid():
    '''
    Sigmoid membership function 
    '''
    
    def __init__(self,a,c):
        self.__a=a
        self.__c=c
        
    def mf(self,x):
        return 1/(1+math.exp(-1*self.__a*(x-self.__c)))

