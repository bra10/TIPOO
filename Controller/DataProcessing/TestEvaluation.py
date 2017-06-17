'''
Created on Nov 15, 2014
Last modified on Nov 16, 2014
@author: adriel
'''
import math as math_operation
from Controller.Lib.FeedbackMessage import TestFeedbackMessage as test_feedback_message
from Model.Evaluation.Evaluation import Question as question_model
from Controller.Management.EvaluationManagement import ExamManagement as exam_management
from Controller.Management.EvaluationManagement import TestManagement as test_management

class TestEvaluation():
	'''
	This class have all the methods to evaluate a given test
	and get the results to display them
	'''
	def list_exam_answers(self,test_id):
		'''
		Function that retrieve all the correct answers of the exam answered

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			A list of the correct answers list of the exam
		'''
		test = test_management().find_test(test_id)		
		list_exam_answers = []
		exam_id = test.exam.key().id()
		exam_instance = exam_management().find_exam(exam_id)		
		for q in range(len(exam_instance.questions)):
			question = question_model().find_question(exam_instance.questions[q].id())
			list_exam_answers.append(question.correct_answers)
		
		return list_exam_answers

	def list_student_answers(self,test_id):
		'''
		Function that retrieve all the student answers of the exam answered

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			A list of the student answers of the exam
		'''
		test = test_management().find_test(test_id)
		return test.question_answers

	def count_correct_answers(self,test_id):	
		'''
		Function that retrieve the count of the correct answers of the exam answered

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			The total of the correct answers of the exam answered by the student
		'''
		list_exam_answers = self.list_exam_answers(test_id)
		list_student_answers = self.list_student_answers(test_id)
		counter = 0
		for index in range(len(list_exam_answers)):
			if list_student_answers[index] in list_exam_answers[index]:
				counter = counter + 1
		return counter		

	def count_question(self,test_id):
		'''
		Function that retrieve the number of questions of the exam answered

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			The total count of questions of the exam
		'''
		list_exam_answers = self.list_exam_answers(test_id)
		counter = 0
		for index in range(len(list_exam_answers)):
			counter = counter + 1
		return counter

	def list_question_value(self,test_id):
		'''
		Function that retrieve all the values of the questions of the exam answered

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			A list of the values of the questions of the exam
		'''
		test = test_management().find_test(test_id)		
		list_question_value = []
		exam_id = test.exam.key().id()
		exam_instance = exam_management().find_exam(exam_id)					
		for q in range(len(exam_instance.questions)):
			question = question_model().find_question(exam_instance.questions[q].id())
			list_question_value.append(question.value)
		
		return list_question_value
		#return test

	def total_sum_correct_answers(self,test_id):
		'''
		Function that retrieve the sum value of correct answers in the exam 
		answered by the student

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			The sum of all the correct answers of the student in the exam
		'''
		list_question_value = self.list_question_value(test_id)
		list_student_answers = self.list_student_answers(test_id)
		list_exam_answers = self.list_exam_answers(test_id)
		test_score = 0
		for index in range(len(list_exam_answers)):
			if list_student_answers[index] in list_exam_answers[index]:
				test_score = test_score + list_question_value[index]
		return test_score

	def total_sum_question_value(self,test_id):
		'''
		Function that retrieve the sum value of all the questions of the exam

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			The sum of all the questions values of the exam
		'''
		list_question_value = self.list_question_value(test_id)
		value = 0
		for index in range(len(list_question_value)):
			value = value + list_question_value[index]
		return value
		
	def test_score(self,test_id):
		'''
		Function that calculate the score of the test, with next algorithm

		final score: student scored on the test 
		exam total score: exam maximum score that can be obtain
		using the 3 rule, first multiply the final score by 100 to obtain the 
		scale of 1% to 100%, where the 100% represents the maximum that can score
		the student, than divide that between the exam total score

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			The score of the student of the test
		'''
		final_score = self.total_sum_correct_answers(test_id)
		number_questions = self.count_question(test_id)
		exam_total_score = self.total_sum_question_value(test_id)		
		total_score = final_score * 100 / exam_total_score 		
		return self.round_score(total_score)

	def score_range(self,value,inferior_limit,superior_limit):
		'''
		Function that retrieve if the score is in a determined value

		Args:
			value (Integer): it's the value to evaluate
			inferior_limit (Integer): is the inferior limit of the range to evaluate
			superior_limit (Integer): is the superior limit of the range to evaluate
		Returns:
			True if the value it's between the range, False otherwise
		'''
		if value >= inferior_limit and value <= superior_limit:
			return True
		return False

	def feedback_message(self,test_id):
		'''
		Function that evaluate the score and retrieve a message depending of 
		the score of the student test

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			A feedback message to know the state of the score
		'''
		test_score = self.test_score(test_id)						
		if self.score_range(test_score,95,100):
			return test_feedback_message.excellent
		elif self.score_range(test_score,80,94):
			return test_feedback_message.good
		elif self.score_range(test_score,60,79):
			return test_feedback_message.regular
		else:		
			return test_feedback_message.insuficient
		'''
		unnecessary else but put it for the visual code
		'''

	def is_approved(self,test_id):
		'''
		Function that retrieve the approved status of the test 

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			True if the test it's approved, False otherwise
		'''
		test_score = self.test_score(test_id)		
		if self.score_range(self.final_score,60,100):
			return True
		return False

	def round_score(self,test_score):
		'''
		Function that retrieve a rounded value of the test score depending
		if the test it's X.5 or higher it's rounded to up, otherwise it's rounded
		to down

		Args:
			test_id (Integer): represents the numeric value of a test id
		Returns:
			A list of the correct answers list of the exam
		'''
		if test_score % 1 >= 0.5:
			return round(test_score,0)
		else:
			return test_score - test_score % 1
