'''
Created on Mar 1, 2015
@author: adriel
'''
from datetime import datetime
from google.appengine.ext import db

from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model

class SubjectManagement():
	
	def add(self,subject_name):
		subject_instance = subject_model()
		subject_instance.name = subject_name
		subject_instance.put()
		return True

	def modify(self,subject_key,subject_name):
		
		subject_instance = subject_model().get_subject(subject_key.id())
		subject_instance.name = subject_name
		subject_instance.put()
		return True
				
	def get_subject(self,subject_id):
		return subject_model().get_subject(subject_id)

	def get_all_subjects(self):				
		return subject_model().get_all_subject()
	def get_subject_by_name(self,name):
		return subject_model().find_name(name)
	def find_name(self,name):
		return subject_model().find_name(name)
	'''
	def find_test(self,test_id):
		return test_model().find_test(test_id)

	def find_same_exam(self,exam_id,student_id):		
		return test_model().find_same_exam(exam_id,student_id)

	def make_approved(self,test_id):
		test = test_model().find_test(test_id)
		test.approved = True
		return test.put()			
	'''