'''
Created on Nov 4, 2014
Last modified on Nov 13, 2014
@author: Adriel
'''
from Controller.Lib.UserType import UserType as user_type
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import AdminManagement as admin_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
import time
class UserSession():

	'''
	This encharge of initialize de user session with a type, the user id and the actual time
	'''
	def init(self, session, user_type, user, time):
		session['user'] = user_type
		#session['user-k'] = user.key()
		session['user-id'] = user.key().id_or_name()
		session['user-time'] = time

	def close(self,session):
		session['user'] = user_type.visitor
		#session['user-k'] = None
		session['user-id'] = None
	'''
	Limpiar todas las variables de sesion!!!
	'''
	'''
	This encharge of finding a user if this one exists, returning the user model information	
	'''
	def find_user(self,user_email):		
		login_user_type = [student_management().find_email(user_email), tutor_management().find_email(user_email), admin_management().find_email(user_email)]		
		for user_data in login_user_type:
			if user_data is not None:
				return user_data		
	'''
	This encharge of assigning a new type to the login user, return a valid user type
	Student, Tutor, Admin, or the default, the Visitor
	'''
	def new_user_type(self,user_email):		
		login_user_type = [student_management().find_email(user_email), tutor_management().find_email(user_email), admin_management().find_email(user_email)]		
		for index, user_data in enumerate(login_user_type):
			if user_data is not None:				
				return user_type.Value[index+1]