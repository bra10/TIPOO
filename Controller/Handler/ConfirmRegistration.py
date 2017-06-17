'''
Created on Dec 11, 2014
@author: Adriel
'''
import os
import jinja2
from google.appengine.ext import db
from RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import AdminManagement as admin_management
from Controller.Handler.UserSession import UserSession as user_session

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('confirm_registration_template.tmp')

class ConfirmRegistration(request_management):
	'''
	Class that handle the confirm registration of a user
	'''
	def get(self):
		'''
		Function that retrieve from the server
		'''
		user = self.get_user_type()		
		if user == user_type.visitor:
			'''
			Retrieve from the url the email to find the user with
			that email and activate the account
			'''
			key = self.request.get('key',None)
			email = key.partition('_')[0]
			user = user_session().find_user(email)
			if user:
				user.activate = True
				user.put()
				template_values = {
					"first": user.first,
					"last": user.last,
					"error":0				
				}								
			else:				
				template_values = {
					"error":1					
				}
			self.response.write(template.render(template_values))
			return 0
		elif user == user_type.student:
			self.redirect('/')
			return 1
		elif user == user_type.tutor:
			self.redirect('/')
			return 2
		else:
			self.redirect('/')
			return 3
		

	def post(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
			return 0
		elif user == user_type.student:
			self.redirect('/')
			return 1
		elif user == user_type.tutor:
			self.redirect('/')
			return 2
		else:
			self.redirect('/')
			return 3