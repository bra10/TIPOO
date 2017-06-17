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
import datetime as dt
from google.appengine.ext import db
from Controller.Handler.RequestManager import RequestManagement as request_management
from Model.Evaluation.Evaluation import Question as question_model
from Model.Evaluation.Evaluation import Exam as exam_model
#from Model.Unused.Learning import Subject as subject_model
from Model.Subject import Subject as subject_model
from Controller.Lib.UserType import UserType as user_type
from Controller.Lib.LearningStyle import LearningStyle as learning_type
from Controller.Lib.LevelType import LevelType as level_type
from Controller.Lib.FeedbackMessage import TestFeedbackMessage as feedback_msg
from Controller.Management.TeachingMaterialManagement import TeachingMaterialManagement as teaching_material_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.EvaluationManagement import ExamManagement as exam_management
from Controller.Management.EvaluationManagement import TestManagement as test_management
from Controller.DataProcessing.TestEvaluation import TestEvaluation as test_evaluation
from Controller.DataProcessing.ElapsedTime import ElapsedTime as elapsed_time


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('exam_template.tmp')
tutor_template = JINJA_ENVIRONMENT.get_template('view_exam_template.tmp')
finished_template = JINJA_ENVIRONMENT.get_template('exam_finished_template.tmp')


class Exam(request_management):
    '''
    Home
    '''
    def get(self):
        user = self.get_user_type()     
        if user == user_type.visitor:
            self.response.write('0')
            self.redirect('/')
            return 0
        elif user == user_type.student:
            exam_id = int(self.request.get('exam_id',None))
            exam =  exam_management().find_exam(exam_id)
            


            list_questions = [] 
            for q in exam.questions:
                q=exam_management().find_question(q.id())
                list_questions.append(q)
            
            len_questions = len(list_questions)
            
            
            template_values = {
                "exam":exam,
                "list_questions":list_questions,
                "exam_id":exam_id,
                "len_questions":len_questions,
                "time_init":dt.datetime.utcnow(),
                
            }                                                 
            self.response.write(template.render(template_values))
            
            return 1
        elif user == user_type.tutor:
            id_exam = int(self.request.get('exam_id',None))
            number_question = int(self.request.get('number_question',0))    
            exam =  exam_management().find_exam(id_exam)
            
            list_questions = [] 
            for q in exam.questions:
                q=exam_management().find_question(q.id())
                list_questions.append(q)
            
            len_questions = len(exam.questions)
            
            template_values = {
                "exam":exam,
                "number_question":number_question,
                "len_questions":len_questions,
                "list_questions":list_questions,
                "id_exam":id_exam
            }                                                 
            self.response.write(tutor_template.render(template_values))
            return 2
        else:                       
            
            self.redirect('/')
            return 3
           
    def post(self):
        user = self.get_user_type()     
        if user == user_type.visitor:
            self.response.write('0')
            self.redirect('/')
            return 0
        elif user == user_type.student:
            
            exam_id = int(self.request.get('exam_id',None))
            exam_instance = exam_management().find_exam(exam_id)            
            list_answers = []           
            number_questions = len(exam_instance.questions)
            for i in range(number_questions):
                list_answers.append( int(self.request.get('r['+ str(i) +']')))
            time_init = self.request.get('time_init',None)
            
            

            time_end = dt.datetime.utcnow()
            time = elapsed_time().elapsed_time(time_init,time_end)
            
            session = self.get_user_id()
            student = student_management().find_key(session)            
            test_id = test_management().add(time.time(),student.key(),exam_instance.key(),list_answers)
            test_id = int(test_id.id())
            test = test_management().find_test(test_id)
            feedback_message = test_evaluation().feedback_message(test_id)
            #self.response.write(feedback_message)          
            test_score = test_evaluation().test_score(test_id)
            #self.response.write(test_score)
            count_correct_answers = test_evaluation().count_correct_answers(test_id)
            #self.response.write(count_correct_answers)
            count_questions = test_evaluation().count_question(test_id)
            #self.response.write(count_questions)
            if feedback_message != feedback_msg.insuficient:
                test.approved = True
                test.put()
                                                
            template_values = {
                "user":"Student",
                "feedback_message":feedback_message,
                "test_score":test_score,
                "count_correct_answers":count_correct_answers,
                "count_questions":count_questions,
                
            }
            self.response.write(finished_template.render(template_values))
            return 1
        elif user == user_type.tutor:                               
            self.redirect('/home')             
            return 2
            
        else:
            
            self.redirect('/home')
            return 3

        