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
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('edit_exam_template.tmp')


class EditExam(request_management , blobstore_handlers.BlobstoreUploadHandler):
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
            id_exam = int(self.request.get('exam_id',None))
            exam = exam_management().find_exam(id_exam)
            
            name = exam.name
            level = exam.level
            learning_type = exam.learning_type
            unit = exam.unit
            topic = exam.topic

            subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
            list_units = unit_management().get_all_units_of_subject(subject.key())
            

            
            
            
            list_questions = [] 
            
            for q in exam.questions:
                q=exam_management().find_question(q.id())
                list_questions.append(q)

            
            len_questions = len(list_questions)

            template_values={'name':name,
                             'level':level,
                             'learning_type':learning_type,
                             'unit':unit,
                             'topic':topic,
                             'list_questions':list_questions,
                             'len_questions':len_questions,
                             'id_exam':id_exam,
                             'list_units':list_units,
                             'upload_url':blobstore.create_upload_url('/upload_exam')
                             }
            
            self.response.write(template.render(template_values))
            return 2                    
        else:                        
            self.redirect('/')  
            return 3
           
    def post(self):
        print "Nunca debe llegar aqui"

        