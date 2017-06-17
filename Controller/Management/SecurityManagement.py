'''
Created on Dec 6, 2013

@author: Raul
'''

from Controller.Lib.UserType import UserType as user_type


class SecurityManagement():
    '''
    Security Management
    
    '''

    def __init__(self, user_cookies):
        '''
        Constructor
        user_cookies: List of strings, represents user cookies
        '''
        self.__user_cookies=user_cookies
        
        
    def validate_user(self):
        user=self.__user_cookies['user']
        if user == user_type.admin:
            return user_type.admin
        elif user == user_type.student:
            return user_type.student
        elif user == user_type.tutor:
            return user_type.tutor
        else: 
            return user_type.visitor