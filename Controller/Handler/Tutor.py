'''
Created on Dec 12, 2013
Last modified on Nov 14, 2014
@author: Raul, Adriel
'''
import os
import jinja2
from cgi import escape
from Controller.Lib.UserType import UserType as user_type
from RequestManager import RequestManagement as request_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import AdminManagement as admin_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Lib.UserType import UserType as user_type
from Controller.DataProcessing.InputField import InputField as input_field

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
tutor_template = JINJA_ENVIRONMENT.get_template('tutor_template.tmp')


class Tutor(request_management):
    
	def post(self):
		user=self.get_user_type()
		errors={}        
		if user == user_type.visitor:            
			email=escape(self.request.get('email',None))  
			email.lower()            
			email.strip()                      
			pwd=input_field().encrypt_password(escape(self.request.get('password',None)))
			pwd.lower()
			pwd.strip()                    
			first = escape(self.request.get('name',None))
			u = self.request.get('university',None)
			f = self.request.get('faculty',None)					
			if tutor_management().add_basic_info(first,email, pwd,'',''):			
				self.session['successt'] = '<h2>Registro exitoso bienvenido a TIPOO</h2>'
				self.redirect('/tutor')
			else:                
				self.session['errort'] = '<span>El usuario registrado ya existe en el sistema</span>'
				self.redirect('/tutor')
			return 0

		elif user == user_type.student:
			self.redirect('/')
			return 1

		elif user == user_type.tutor:
			self.redirect('/')
			return 2

		else:
			return 3

	def get(self):
		user=self.get_user_type()
		if user == user_type.visitor: 
			html = ''
			error3 = ''
			success = ''
			if 'errort' in self.session:
				error3 = self.session['errort']								
			if 'successt' in self.session:
				success = self.session['successt']											
			if error3:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="error">Ha habido un problema<br><i class="fa fa-times"></i><br>'
				html+= error3
				self.session['errort'] = ''
				url = '/tutor'
				html+= '<br><button class="closemodal">Aceptar</button></div>'

			if success:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="success">Grandioso<br><i class="fa fa-check"></i><br>'
				html+= success
				self.session['successt'] = ''
				url = '/'
				html+= '<br><button class="closemodal">Aceptar</button></div>'                       
			template_values={            
				"html":html
			}            
			self.response.write(tutor_template.render(template_values))
			return 0
		elif user == user_type.student:                        
			self.redirect('/explorer')
			return 1
		else:            
			self.redirect('/home')
			return 2
