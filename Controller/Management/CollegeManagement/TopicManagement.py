'''
Created on Mar 1, 2015
@author: adriel
'''
from datetime import datetime
from google.appengine.ext import db

from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model

class TopicManagement():
	
	def add(self,subject_key,topic_name):		
		topic_instance = topic_model()
		topic_instance.name = topic_name
		topic_instance.subject = subject_key
		return topic_instance.put()
		

	def modify(self,subject_key,topic_key,topic_name):
		topic_instance = topic_model().get_topic(topic_key.id())
		topic_instance.name = topic_name
		topic_instance.subject = subject_key
		topic_instance.put()
		return True
		
	def get_topic(self,topic_id):
		return topic_model().get_topic(topic_id)

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