'''
Created on Dec 12, 2013
Last modified Jan 27, 2015
@author: Raul, Tristian, Adriel
'''
import os
import time
import datetime as dt
import json
import copy
import jinja2
from google.appengine.ext import db
from Model.Evaluation.Evaluation import Question as question_model
from Model.Evaluation.Evaluation import Exam as exam_model
#from Model.Unused.Learning import Subject as subject_model
from Model.Subject import Subject as subject_model
from Controller.Lib.UserType import UserType as user_type
from Controller.Lib.LearningStyle import LearningStyle as learning_type
from Controller.Lib.LevelType import LevelType as level_type
from Controller.Lib.FeedbackMessage import TestFeedbackMessage as feedback_msg
from RequestManager import RequestManagement
from Controller.Management.TeachingMaterialManagement import TeachingMaterialManagement as teaching_material_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.EvaluationManagement import ExamManagement as exam_management
from Controller.Management.EvaluationManagement import TestManagement as test_management
from Controller.DataProcessing.TestEvaluation import TestEvaluation as test_evaluation
from Controller.DataProcessing.ElapsedTime import ElapsedTime as elapsed_time
JINJA_ENVIRONMENT = jinja2.Environment(
		loader = jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('Exam.tmp')	

class Exam(RequestManagement):	
	'''
	Class that handle the exam to the server
	'''
	def post(self):
		user = self.get_user_type()		
		if user == user_type.visitor:
			self.response.write('0')
			self.redirect('/')
			return 0
		elif user == user_type.student:
			'''
			Retrieve the exam_id from the url and find that exam, 
			receive the start and end time of the exam, the student who 
			answered and the answers of this one.

			Save that instance and later calculate the score to get the 
			results, update the test to know if the student approved or not
			the test and show in the template the results
			'''
			exam_id = int(self.request.get('exam_id',None))
			exam_instance = exam_management().find_exam(exam_id)			
			list_answers = []			
			number_questions = len(exam_instance.questions)
			for index in range(number_questions):
				list_answers.append(int(self.request.get('r[{0}]'.format(index),0)))
			time_init = self.request.get('time_init',None)
			'''
			Cambiar por sesiones o cookies
			'''
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
				"count_question":count_questions,
				"status":1
			}						
			self.response.write(template.render(template_values))
			return 1
		elif user == user_type.tutor:								
				
			'''
			This is use it to retrieve all the elements of an exam if
			exists one or show the form to create a new one

			delete and available came from a request of ajax and update 
			the exam

			otherwise it will create a new one and retrieve all the data
			from the form
			'''
			available = self.request.get('available',None)
			'''
			to be deleted
			'''
			delete = self.request.get('delete',None)
			if delete:								
				exam_id = int(self.request.get('exam_id',None))					
				exam_instance = exam_management().find_exam(exam_id)
				db.delete(exam_instance)
			if available:
				exam_id = int(self.request.get('exam_id',None))					
				exam_instance = exam_management().find_exam(exam_id)
				if exam_instance.available == True:
					exam_instance.available = False
				else:
					exam_instance.available = True
				exam_instance.put()
			else:
				'''
				This section it's for create the exam with the values that
				came from the server
				'''
				session = self.session['user-id']			
				user = tutor_management().find_key(session)						

				learning_style = self.request.get('learning_style',None)
				level = self.request.get('level',None)			
				unit = self.request.get('unit',None)
				subject = self.request.get('subject',None)
						
				number_questions = 0
				while self.request.get_all('q[{0}]'.format(number_questions),None):
					number_questions = number_questions + 1

				question = []
				question_value = []
				list_answer = []
				list_correct_answer = []						
				list_correct_answer_int = []
				list_list_correct_answer_int = []
				question_value_int = []
				list_list_str_answer = []
				list_str_question = []
				'''
				Retrieve all the inputs from the form and save it in lists
				'''
				for index in range(number_questions):				
					question.append(self.request.get('q[{0}]'.format(index),None))
					question_value.append(self.request.get('v[{0}]'.format(index),None))				
					list_answer.append(self.request.get_all('a[{0}]'.format(index),None))
					list_correct_answer.append(self.request.get_all('r[{0}]'.format(index),None))			

				for index in range(number_questions):
					sub_index = 0
					list_correct_answer_int = []
					while sub_index < len(list_correct_answer[index]):					
						list_correct_answer_int.append(int(list_correct_answer[index][sub_index]))
						sub_index = sub_index + 1
					list_list_correct_answer_int.append(list_correct_answer_int)
				
				for index in range(number_questions):
					question_value_int.append(int(question_value[index]))

				for index in range(number_questions):
					sub_index = 0
					list_str_answer = []
					while sub_index < len(list_answer[index]):
						list_str_answer.append(str(list_answer[index][sub_index]))
						sub_index = sub_index + 1
					list_list_str_answer.append(list_str_answer)

				for index in range(number_questions):							
					list_str_question.append(str(question[index]))
				self.response.write(list_list_correct_answer_int)			
				list_questions = []
				'''
				Put the list in a question model object to store in the database
				'''
				for index in range(number_questions):
					q = question_model()	
					q.text = list_str_question[index]
					q.answers = list_list_str_answer[index]
					q.correct_answers = list_list_correct_answer_int[index]
					q.value = question_value_int[index]				
					#list_questions[index]= q.put()
					list_questions.append(q.put())

				s = subject_model()
				s.name = str(subject)							
				exam_id = self.request.get('exam_id',None)
				'''
				If a exam_id it's retrieved from the url it means that this exam it's been
				modified, so it doesn't need to be created, otherwise it have to and put all
				the data need to store it in the database
				'''
				if exam_id:
					exam_id = int(exam_id)
					exam_instance = exam_management().modify(exam_id,user,int(learning_style),int(level),int(unit),s.put(),list_questions)
					self.redirect('/home')
					#self.response.write('<a href="/home">Home</a>')
					#desplegar mensaje que se ha modificado
				else:
					exam_key = exam_management().add(user,int(learning_style),int(level),int(unit),s.put(),list_questions)								
					self.redirect('/home')
					#self.response.write('<a href="/home">Home</a>')
					#desplegar mensaje que se ha creado
				#self.redirect('/home')			
			return 2
			
		else:
			self.response.write('3')
			self.redirect('/home')
			return 3

	def get(self):
		user = self.get_user_type()		
		if user == user_type.visitor:
			self.response.write('0')
			self.redirect('/')
			return 0
		elif user == user_type.student:
			exam_id = int(self.request.get('exam_id',None))
			exam_instance = exam_management().find_exam(exam_id)
			'''
			THIS SECTION NEEDS SOME WORK
			This section just retrieve the exam data to show
			in the view for the student to solve
			'''
			exam = {}
			question = exam_instance.questions
			list_questions = []
			exam['id'] = exam_instance.key().id()
			exam['learning_style'] = learning_type().Value_Spanish[exam_instance.learning_type]
			exam['level'] =  level_type().Value_Spanish[exam_instance.level]
			exam['unit'] = exam_instance.unit
			exam['subject'] = subject_model().find_subject(exam_instance.subject.key().id())
			for index in range(len(question)):
				list_questions.append(question_model().find_question(question[index].id()))
			exam['question'] =  list_questions                
			list = []
			var = {}			
			index=0
			while index <len(question):
				var['index'] = index
				list.append(copy.deepcopy(var))  #copy.deepcopy it's a special function, don't deleted
				index = index + 1
			template_values = {
				"user":"Student",
				"exam":exam,
				"time_init":dt.datetime.utcnow(),
				"list":list,
				"status":0
			}								                  
			self.response.write(template.render(template_values))
			return 1
		elif user == user_type.tutor:			
			'''
			This section just retrieve the exam_id from the url if one exists
			and depending of it, shows the exam or the form to create a new exam
			'''
			exam_id = self.request.get('exam_id',None)
			exam = {}
			list = []
			var = {}
			if exam_id:
				exam_id = int(exam_id)
				exam_instance = exam_management().find_exam(exam_id)								
				question = exam_instance.questions
				list_questions = []
				exam['id'] = exam_instance.key().id()
				exam['learning_style'] = learning_type().Value_Spanish[exam_instance.learning_type]
				exam['level'] =  level_type().Value_Spanish[exam_instance.level]
				exam['unit'] = exam_instance.unit
				exam['subject'] = subject_model().find_subject(exam_instance.subject.key().id())
				for index in range(len(question)):
					list_questions.append(question_model().find_question(question[index].id()))
				exam['question'] =  list_questions            
				index=0
				while index <len(question):
					var['index'] = index
					list.append(copy.deepcopy(var))
					index = index + 1
			template_values = {
				"user":"Tutor",
				"exam":exam,
				"list":list	
			}
			self.response.write(template.render(template_values))
			return 2
		else:						
			template_values = {}
			#self.response.write(template.render(template_values))
			self.redirect('/')
			return 3

