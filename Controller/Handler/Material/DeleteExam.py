'''
Created on Dec 12, 2013
Last Modified on Jul 17, 2015
@author: Raul, Adriel, Omar
'''
import os
import time
import json
import jinja2
import copy
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.EvaluationManagement import ExamManagement as exam_management



class DeleteExam(request_management):
    '''
    Home
    '''
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:
            self.redirect('/home') 
            return 1

        elif user == user_type.tutor:
            
            id_exam = int(self.request.get('id_exam',None)) 
            exam_management().find_exam(id_exam).delete()
            self.redirect('menu_exam?page=1')
            return 2                    
        else:                        
            self.redirect('/')  
                                   
            return 3
           
    def post(self):
        print "Nunca debe llegar aqui"

        