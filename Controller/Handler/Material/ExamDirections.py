'''
Created on Dec 12, 2013
Last Modified on Jul 17, 2015
@author: Raul, Adriel, Omar
'''
import os
import os.path
import time
import json
import jinja2
import copy
import random
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.EvaluationManagement import ExamManagement as exam_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('directions_template.tmp')


class ExamDirections(request_management):
    '''
    Home
    '''
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:       
            unit_id = int(self.request.get('unit_id',None))
            unit = unit_management().get_unit(unit_id)
            exams = exam_management().get_exams_by_unit(unit)
            len_exams = len(exams)
            
            if(len_exams>0):
                exam_selected  = random.randint(0,len_exams - 1)
                exam = exams[exam_selected]
                template_values={'exam_id':exam.key().id()}
                self.response.write(template.render(template_values))
            else:
                self.response.write('There i no exams')
            return 1

        elif user == user_type.tutor:                          
			self.redirect('/home')  
			return 2                    
        else:                        
            self.redirect('/')  
                                   
            return 3
           
    def post(self):
        print "Nunca debe llegar aqui"

        