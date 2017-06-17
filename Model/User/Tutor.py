'''
Created on Dec 6, 2013
Last Modified on Feb 17, 2015
@author: Raul
'''
from google.appengine.ext import db
from User import User as User
from Model.University.Faculty import Faculty
from Model.University.University import University

class Tutor(User):
    uploaded_material = db.StringListProperty()
    university = db.ReferenceProperty(University)
    speciality = db.StringProperty()
    #assignatures: have to change to db.Subject reference
    #subjects = db.StringListProperty()
    subjects = db.ListProperty(db.Key)
    faculty = db.ReferenceProperty(Faculty)

    def set_or_get(self, email):
        query_str = "SELECT * FROM Tutor WHERE email =:email"
        user = db.GqlQuery(query_str, email=email).get()
        if user is None:
            user = Tutor()
            user.put()
        return user

    def get_user(self, user_id):
        return Tutor.get_by_id(user_id)

    def delete(self, user_id):

        tutor_instance = self.get_user(user_id)
        if tutor_instance:
            db.delete(tutor_instance)
            return True
        return False


    def find_name(self, name):
        query_str = "SELECT * FROM Tutor WHERE first=\'" + name + "\'"
        return db.GqlQuery(query_str).get()

    def find_last(self, last):
        query_str = "SELECT * FROM Tutor WHERE last=\'" + last + "\'"
        return db.GqlQuery(query_str).get()

    def find_email(self, email):
        query_str = "SELECT * FROM Tutor WHERE email = :email"
        return db.GqlQuery(query_str, email=str(email)).get()

    def find_all_exams(self, tutor_id):
        query_str = "SELECT * FROM Exam WHERE user = :tutor"
        return db.GqlQuery(query_str, tutor=tutor_id).fetch(limit=50)

    def find_all_exams_subject(self, tutor_id,subject):
        query_str = "SELECT * FROM Exam WHERE user = :tutor AND subject=:subject"
        return db.GqlQuery(query_str, tutor=tutor_id,subject=subject).fetch(limit=1000)
    
    def find_all_exams(self, tutor_id , subject, page , limit):
        offset = limit * page
        query_str = "SELECT * FROM Exam WHERE user = :tutor AND subject = :subject"
        return db.GqlQuery(query_str, tutor=tutor_id , subject = subject).fetch(limit=limit,offset=offset)

    def get_all_unit_available_exams(self,unit):
		query_str = "SELECT * FROM Exam WHERE unit=:unit AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,unit=unit).fetch(limit=1000)

    def get_list_exam_material(self,tutor,subject,page,limit):
        offset = limit * page
        query_str = "SELECT * FROM Exam WHERE user=:tutor ORDER BY uploaded_time DESC"  
        return db.GqlQuery(query_str,tutor=tutor).fetch(limit=limit,offset=offset)
    


    def get_all_tutor(self):
        query_str = "SELECT * FROM Tutor"
        return db.GqlQuery(query_str).fetch(limit=5)

  
