'''
Created on Dec 10, 2013
Last Modified on Nov 10, 2014
@author: Raul, Adriel, Omar
'''
import datetime

from google.appengine.ext import db

from Model.User.Administrator import Administrator as admin_model
from Model.User.Student import Student as student_model
from Model.User.Tutor import Tutor as tutor_model
from Model.University.University import University as university_model
from Model.University.Faculty import Faculty as faculty_model
from Model.Subject.Subject import Subject as subject_model
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Model.Evaluation.Evaluation import Exam as exam_model



class StudentManagement():
	'''
	User Management
	'''
	def add_basic_info(self,first,email,password):
		user = student_model().set_or_get(email)
		tutor = tutor_model().set_or_get(email)
		if user.email or tutor.email:
			return False
		else:
			user.first = first
			user.email=email
			user.password=password
			user.activate = True
			user.put()
			return True

	def add(self,first,last,email,password,sex,year,month,date,picture=None):
		'''
		Add User
		'''        
		user=student_model().set_or_get(email)
		if user.email:
			return False
		else:
			user.first=first
			user.last=last
			user.email=email
			user.password=password
			user.sex=sex
			birth_date = '{0}-{1}-{2}'.format(year,month,date)
			user.bday=datetime.datetime.strptime(birth_date,"%Y-%m-%d").date()
			if not picture:                
				user.picture=db.Blob('Static\img\visitor.png')
			else:
				user.picture = picture
				user.activate = False
				user.put()
				return True
    
	def delete(self,user_id):
		return student_model().delete(user_id)
    
	def find_first(self,first):
		return student_model().find_name(first)
    
	def find_last(self,last):
		return student_model().find_last(last)
    
	def find_email(self,email):
		return student_model().find_email(email)
    
	def find_key(self,user_id):
		return student_model().get_user(user_id)
    
	def modify(self,first,last,email,password):
		user=student_model().get_or_insert(email)
		#Already Exist
		if user:
			user.first=first
			user.last=last
			user.email=email
			user.password=password
			user.put()
			return True
		else:
			return False

	def get_student(self,student_id):
		return student_model().get_user(student_id)

	def get_all_user_by_id(self,user_id):
		return student_model().get_all_user_by_id(user_id)
        
	def add_tutor(self,student_email,tutor_email):
		user=student_model().find_email(student_email)        
		if not tutor_email in user.tutors:
			user.tutors.append(tutor_email)
			user.put()
			return True
		return False
    
	def remove_tutor(self,student_email,tutor_email):
		user=student_model().get_or_insert(student_email)
		tutor=tutor_model().get_or_insert(tutor_email)
		user.tutors.remove(tutor)
		user.put()
    
	def find_all_tutors(self,email):        
		return student_model().find_all_tutors(email)        

	def find_tutor(self,tutor_email):
		return student_model().find_tutor(tutor_email)     
  
class TutorManagement():
	'''
	User Management
	'''
    
	def add(self,first,last,email,password,picture=None):
		'''
		Add User
		'''
		user=tutor_model().set_or_get(email)
		if user.email:
			return False
		else:
			user.first=first
			user.last=last
			user.email=email
			user.password=password
			user.activate = True
			user.subjects.append(subject_model().find_name('Programacion Orientada a Objetos').key())
			#if not picture:
			#    user.picture=db.Blob('Static\img\visitor.png')
			#else:   
			#    user.picture = picture
			user.put()                    
			return True
    
	def delete(self,user_id):
		return tutor_model.delete(user_id)
    
	def find_first(self,first):
		return tutor_model().find_name(first)

	def get_all_tutors(self):
		return tutor_model().get_all_tutor()
    
	def find_last(self,last):
		return tutor_model().find_last(last)
    
	def find_email(self,email):
		return tutor_model().find_email(email)
    
	def find_key(self,tutor_id):
		return tutor_model().get_user(tutor_id)
    
	def modify(self,first,last,email,password):
		user=tutor_model.get_or_insert(email)
		#Already Exist
		if user:
			user.first=first
			user.last=last
			user.email=email
			user.password=password
			user.put()
			return True
		else:
			return False
            
	def find_all_exams(self,tutor_id):        
		return tutor_model().find_all_exams(tutor_id)

	def find_all_exams(self,tutor , subject , page):
		return tutor_model().find_all_exams(tutor,subject,page,10)

	def find_all_exams_subject(self,tutor,subject):
		return tutor_model().find_all_exams_subject(tutor,subject)

	def get_list_exam_material(self,tutor,subject,page):
		s = subject_management().get_subject(subject.id())
		return tutor_model().get_list_exam_material(tutor,s.key(),page,10)


	def get_tutor(self,tutor_id):
		return tutor_model().get_user(tutor_id)

	def add_basic_info(self, name, email, password, university, faculty):
		tutor = tutor_model().set_or_get(email)
		user = student_model().set_or_get(email)
		if tutor.email or user.email:
			return False
		else:
			tutor.email=email
			tutor.password=password
			tutor.activate = True
			tutor.first = name

			u = university_model()
			u.name = university
			u_key = u.put()
			tutor.university = u_key

			f = faculty_model()
			f.name = faculty
			f_key = f.put()
			tutor.faculty = f_key
			tutor.put()
			return True

class AdminManagement():
	def find_email(self,email):
		return admin_model().find_email(email)

	def add(self,first,last,email,password,picture=None):
		'''
		Add User
		'''
		user=admin_model().set_or_get(email)
		if user.email:
			return False
		else:
			user.first=first
			user.last=last
			user.email=email
			user.password=password
			user.activate = True
			user.picture=picture
			user.put()        
			return True
