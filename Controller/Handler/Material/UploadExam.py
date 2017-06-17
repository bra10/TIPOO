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
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Model.Evaluation.Evaluation import Question


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('upload_exam_template.tmp')


class UploadExam(request_management, blobstore_handlers.BlobstoreUploadHandler):
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
            subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
            list_units = unit_management().get_all_units_of_subject(subject.key())
            
            
            template_values={'list_units':list_units,
                             'upload_url':blobstore.create_upload_url('/upload_exam')}
            self.response.write(template.render(template_values))
            
            return 2                    
        else:                        
            self.redirect('/')  
            return 3
           
    def post(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:
            self.redirect('/home') 
            return 1

        elif user == user_type.tutor:
            
            id_exam = self.request.get('id_exam',None) 
            
            list_questions_aux = []
            if(id_exam):
                id_exam = int(id_exam)
                exam = exam_management().find_exam(id_exam)
                for q in exam.questions:
                    q=exam_management().find_question(q.id())
                    list_questions_aux.append(q)    
            
            self.response.write(len(list_questions_aux))
            
            tutor_id = self.session['user-id']
            tutor_key = tutor_management().get_tutor(tutor_id)
            
            id_unit = int(self.request.get('unit_exam',None))
            unit = unit_management().get_unit(id_unit)
            
            name_exam = self.request.get('name_exam',None)
            topic_exam = self.request.get('topic_exam',None)
            
            learning_type = int(self.request.get('learning_type',None))
            level = int(self.request.get('level',None))

            subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
            
            count_questions = int(self.request.get('count_questions',None))
            
            answers = []
            list_questions = []
            correct_answers = []
            cout_images = 0
            
            for i in range(count_questions):
                q = Question()
                q.text = self.request.get( 'Q_' + str(i+1) ,None)
                q.value = int(self.request.get('PossPtsQ_' + str(i+1) ,None))
                
                answers.append(self.request.get('Q_' + str(i+1) + '_A_' + '1',None))
                answers.append(self.request.get('Q_' + str(i+1) + '_A_' + '2',None))
                answers.append(self.request.get('Q_' + str(i+1) + '_A_' + '3',None))
                answers.append(self.request.get('Q_' + str(i+1) + '_A_' + '4',None))
                q.answers = answers

                if(self.request.get('Q_' + str(i+1) + '_ChkBox_' + '1')):
                    correct_answers.append(1)
                if(self.request.get('Q_' + str(i+1) + '_ChkBox_' + '2')):
                    correct_answers.append(2)
                if(self.request.get('Q_' + str(i+1) + '_ChkBox_' + '3')):
                    correct_answers.append(3)
                if(self.request.get('Q_' + str(i+1) + '_ChkBox_' + '4')):
                    correct_answers.append(4)
                q.correct_answers = correct_answers
                
                
                if(id_exam and i < len(list_questions_aux) ):
                    q.image = list_questions_aux[i].image

                if(self.request.get('Q_I' + str(i+1) )):
                    q.image = self.get_uploads()[cout_images]
                    cout_images = cout_images + 1
                    
                q = q.put()
                
                list_questions.append(q)
            
            if(id_exam):
                exam.delete()
            exam_management().add(name_exam,tutor_key,learning_type,level,unit,topic_exam,list_questions,subject)
            self.redirect('/admin_exam')
            
            return 2                    
        else:                        
            self.redirect('/')  
                                   
            return 3
        

        