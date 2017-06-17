'''
Created on Nov 15, 2014
@author: adriel
'''
from datetime import datetime
from google.appengine.ext import db

from Model.Evaluation.Evaluation import Exam as exam_model
from Model.Evaluation.Evaluation import Question as question_model
from Model.Evaluation.Evaluation import Test as test_model
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management

class TestManagement():
	'''
	EvaluationManagement
	'''
	def add(self,completion_time,applicant,exam,question_answers):

		test = test_model()
		test.date = datetime.now().date()
		test.completion_time = completion_time
		test.applicant = applicant
		test.exam = exam
		test.question_answers = question_answers
		test.approved = False
		return test.put()

	def find_test(self,test_id):
		return test_model().find_test(test_id)

	def find_same_exam(self,exam_id,student_id):		
		return test_model().find_same_exam(exam_id,student_id)

	def make_approved(self,test_id):
		test = test_model().find_test(test_id)
		test.approved = True
		return test.put()			

class ExamManagement():
    '''
    EvaluationManagement
    '''
    def get_exams_by_unit(self,unit_key):
        return exam_model().get_exams_by_unit(unit_key)

    def add(self, name , user, learning_type, level, unit, topic, questions,subject):
        exam = exam_model()
        exam.name = name
        exam.level = level
        exam.unit = unit
        
        exam.topic = topic                     
        for index in range(len(questions)):
            exam.questions.append(questions[index])                    
        exam.learning_type = learning_type
        exam.user = user
        exam.subject = subject
        exam.available = True
        return exam.put()   
        '''
        e = exam.put()    
        if e.has_id_or_name():
            debug.response.write('tiene')
        else:
            debug.response.write('noup')
        e2 = e.id()            
        ea = self.find_exam(e2)            
        for index in range(len(questions)):
            q = self.find_question(ea.questions[index].id())
            debug.response.write(q.text)        
        '''
    def find_question(self,question_id):
        return question_model().find_question(question_id)

    def modify(self,exam_id, user, learning_type, level, unit, subject, questions):
        exam = exam_model().find_exam(exam_id)
        exam.level = level
        
        exam.unit = unit
        exam.subject = subject                     
        exam.questions = []
        for index in range(len(questions)):
            exam.questions.append(questions[index])                    
        exam.learning_type = learning_type
        exam.user = user        

        return exam.put()       

    def find_exam(self, exam_id):
    	return exam_model().find_exam(exam_id)

    def remove(self, exam_key):
    	db.delete(exam_key)
        return True
	##Prueba
    def get_list_exam_material_unit(self,tutor,subject,unit,page):
    	return exam_model().get_unit_exams_available(tutor,subject,unit,page,10)

    def get_unit_available_exams(self,unit_key,page):
    	return exam_model().get_unit_available_exams(unit_key,page,10)
    
    def get_all_unit_available_exams(self,unit_key):
        return exam_model().get_all_unit_available_exams(unit_key)
        
    def get_all_exam_material(self,tutor,subject):
        return exam_model().get_all_exam_material(tutor,subject)
    
    def get_all_exams(self,tutor):
        return exam_model().get_all_exams(tutor)
    
    
    def get_list_exam_material_of_one_subject(self,tutor,subject,page):
        s = subject_management().get_subject(subject.id())
        return exam_model().get_list_exam_material(tutor,s.key(),page,10)
    

    def make_available(self,exam_id):
    	exam = self.find_exam(exam_id)
    	if exam.available:
    		exam.available = False;
    	else:
    		exam.available = True
        exam.put()
        return True

