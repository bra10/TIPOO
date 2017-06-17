'''
Created on Dec 6, 2013
Last Modified on Jan 26, 2015
@author: Raul, Adriel
'''
from google.appengine.ext import db

from User import User as User

class Student(User):
    learning_style=db.StringProperty()
    consulted_material=db.StringProperty()
    recurrent_tutors=db.StringListProperty()
    progress=db.FloatProperty()
    complexx=db.StringProperty()
    tutors=db.StringListProperty()
    tutors_list=db.ListProperty(db.Key) 
    preferences=db.StringListProperty()
    evaluation=db.StringListProperty()    
    registration_tag = db.StringProperty()

    def set_or_get(self,email):
        query_str="SELECT * FROM Student WHERE email=:email"
        user=db.GqlQuery(query_str,email=email).get()
        if user is None:
            user=Student()
            user.put()
        return user
    
    def get_user(self,user_id):
        #key=db.Key.from_path('Student',user_id)
        #return Student.get(key)
        return Student.get_by_id(user_id)

    def delete(self,user_id):

        student_instance = self.get_user(user_id)
        if student_instance:
            db.delete(student_instance)
            return True
        return False
    











    '''
    Aun por debatir su futuro
    ''' 
    def find_name(self,user_id):

        student_instance = Student.get_by_id(user_id)
        if student_instance:                    
            return student_instance.first
        return False
        '''
        query_str="SELECT * FROM Student WHERE first=\'"+name+"\'"
        return db.GqlQuery(query_str).get()
        '''

    # def find_last(self,last):
    #     student_instance = Student.get_by_id(user_id)
    #     if student_instance:
    #         return student_instance.last
    #     return False

        query_str="SELECT * FROM Student WHERE last=\'"+last+"\'"
        return db.GqlQuery(query_str).get()
     
    def find_email(self,email):
        query_str="SELECT * FROM Student WHERE email=\'"+email+"\'"
        return db.GqlQuery(query_str).get()
    
    def find_tutor(self,tutor_email):
        query_str = "SELECT * FROM Tutor WHERE email=\'"+tutor_email+"\'"        
        return db.GqlQuery(query_str).get()  

    def find_all_tutors(self,email):
        #query_str = "SELECT tutors FROM Student WHERE email = :1"
        #return db.GqlQuery(query_str,email).fetch(limit=50)
        query_str="SELECT tutors FROM Student WHERE email=\'"+email+"\'"
        return db.GqlQuery(query_str).fetch(limit=50)
    #-------------------------------------------------------------------------#
    '''
    def find_tutor_available_exams(self,tutor_id):        
        query_str = "SELECT * FROM Exam WHERE __key__ = KEY('Tutor',{0})".format(tutor_id)
        return db.GqlQuery(query_str).get()    
        #modificar para aceptar todos los examenes disponibles para el estudiante
        #pero a la vez que no han sido aprobados

    def find_all_tests(self,student_id):
        query_str = "SELECT * FROM Test WHERE __key__ = KEY('Student',{0})".format(student_id)
        return db.GqlQuery(query_str).get()

    def find_exam_in_test(self,exam_id):
        query_str = "SELECT * FROM Exam WHERE __key__ = KEY('Exam',{0})".format(exam_id)
        return db.GqlQuery(query_str).get()
    '''    
    '''
    Todos los examenes disponibles y no realizados
    '''











