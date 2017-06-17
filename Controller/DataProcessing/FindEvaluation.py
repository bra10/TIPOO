'''
Created on Nov 17, 2014
Last Modified on Jan 27, 2015
@author: Adriel
'''

from google.appengine.ext import db
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.EvaluationManagement import ExamManagement as exam_management
class FindEvaluation():
    '''
    Agregar historidal de examenes realizados, servira para futuro!!!
    '''
    '''
    Class that handle the way to get all the exam or test from the database
    to send them later in the templates
    '''
    def find_tutor_available_exam(self,tutor_email): 
        '''
        Function that just call a query to retrieve all the exams of a tutor, just
        if this ones are available
        Args:
            tutor_email (String): the email of a tutor
        Return:
            A list of exams 
        '''
        return FindEvaluationQueries().find_tutor_available_exam(tutor_email)        
    
    def find_all_tests(self,student_id):
        '''
        Function that just call a query to retrieve all the test solved by the 
        student
        Args:
            student_id (Integer): represents the numeric id of a student
        Return:
            A list of tests
        '''
        return FindEvaluationQueries().find_all_tests(student_id)

    def find_exam_in_test(self,exam_id):
        '''
        Function that just call a query to retrieve all the exams of a tutor, just
        if this ones are available
        Args:
            tutor_email (String): the email of a tutor
        Return:
            A list of exams 
        '''
        return FindEvaluationQueries().find_exam_in_test(exam_id)

    def list_tutors_exams(self,tutor_list):
        '''
        Function that merge all the tutors exams, separating each tutor
        with their own exams
        Args:
            tutor_list (List): all the tutors that belong to a student
        Return:
            A list of all the exams created from the tutors 
        '''
    	tutors_exam = []                                        
    	for index in range(len(tutor_list)):
            exams = self.find_tutor_available_exam(str(tutor_list[index]))                    
            
            exam = []
            if exams:            
                for sub_index in range(len(exams)):
                    if exams[sub_index].available == True:
                        exam.append(exams[sub_index])            
            tutors_exam.append(exam)                    
        return tutors_exam  

    def is_passed(self,tutor_exam,exam,test):
        '''
        Function that evaluate if the test has been approved
        If the tutor_exam it's equal to the exam it means that are
        the same exam, now it has to be available so that can be
        solved
        After just left to know if this one has been approved
        Args:
            tutor_exam (Exam): the exam of the tutor
            exam (Exam): an exam of all the existent exams 
            test (Test): it's the test that has been solved
        Return:
            True if the test has been approved, false otherwise
        '''
        passed = False
        if tutor_exam.user.key().id() == exam.user.key().id() and exam.available == True and tutor_exam.key().id() == exam.key().id():                
            if test.approved == True:
                passed = True
        return passed

    def find_test_exam_available(self,student_instance):    
        '''        
        Function that retrieve all the exams that hasn't been approved and
        are available for the student
        The algorithm user three nested loops
        First loop: to access each tutor
        Second loop: to access each exam of a tutor
        Third loop: to compare the tests solved and look for the ones
        that has been approved to remove them from the list to send to
        the view            

        Args:
            student_instance (Student): a student user instance
        Return:
            A list of exams to solve for the student
        '''            
        #tutor_list = student_management().find_all_tutors(student_instance.email)        
        tutor_list = student_instance.tutors    
        tutors_exam = self.list_tutors_exams(tutor_list)                
        copy_tutors_exam = self.list_tutors_exams(tutor_list)                
        student_id = student_instance.key()        
        test_list = self.find_all_tests(student_id)                    
        
        passed = False    
        data = False
        
        i=0
        while i < len(tutors_exam):                
            j=0
            while j < len(tutors_exam[i]):                    
                passed = False
                k = 0
                while k < len(test_list):                                        
                    exam = exam_management().find_exam(test_list[k].exam.key().id())                                                
                    if self.is_passed(tutors_exam[i][j],exam,test_list[k]):                
                        passed = True
                        break
                    k=k+1
                
                if passed:                    
                    copy_tutors_exam[i][j] = None
                j=j+1                
            i = i+1

          
        return copy_tutors_exam
    
class FindEvaluationQueries():
    '''
    Class that handle the GQL queries
    '''
    def find_tutor_available_exam(self,tutor_email):        
        '''
        Function that just call a query to retrieve all the exams of a tutor, just
        if this ones are available
        Args:
            tutor_email (String): the email of a tutor
        Return:
            A list of exams 
        '''
        tutor_instance = tutor_management().find_email(tutor_email)                        
        if tutor_instance:
            return tutor_management().find_all_exams(tutor_instance.key())        
        else:
            return False

    def find_all_tests(self,student_id):  
        '''
        Function that just call a query to retrieve all the test solved by the 
        student
        Args:
            student_id (Integer): represents the numeric id of a student
        Return:
            A list of tests
        '''      
        query_str = "SELECT * FROM Test WHERE applicant = :s"
        return db.GqlQuery(query_str,s=student_id).fetch(limit=50)    
        #query_str = "SELECT * FROM Test"
        #return db.GqlQuery(query_str).fetch(limit=50)    

    def find_exam_in_test(self,exam_id):
        '''
        Function that just call a query to retrieve all the exams of a tutor, just
        if this ones are available
        Args:
            tutor_email (String): the email of a tutor
        Return:
            A list of exams 
        '''
        query_str = "SELECT * FROM Exam WHERE __key__ = KEY('Exam',{0})".format(exam_id)
        return db.GqlQuery(query_str).get()    