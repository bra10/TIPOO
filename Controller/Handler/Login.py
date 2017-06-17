'''
Created on Dec 15, 2014
Last Modified on Mar 1, 2015
@author: Adriel
'''
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('login_template.tmp')
login_template = JINJA_ENVIRONMENT.get_template('session_template.tmp')
from Controller.Lib.UserType import UserType as user_type
from RequestManager import RequestManagement as request_management

class Login(request_management):
	'''
	Login
	'''
	def get(self):
		user = self.get_user_type()		
		if user == user_type.visitor:
			
			html = ''
			error1 = ''
			error2 = ''
			error3 = ''
			success = ''
			if 'error1' in self.session:
				error1 = self.session['error1']			
			if 'error2' in self.session:
				error2 = self.session['error2']			
			if 'error3' in self.session:
				error3 = self.session['error3']								
			if 'success' in self.session:
				success = self.session['success']								


			if error1:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="error">Ha habido un problema<br><i class="fa fa-times"></i><br>'
				html+= error1
				self.session['error1'] = ''
				html+= '<br><button class="closemodal">Aceptar</button></div>'
			elif error2:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="error">Ha habido un problema<br><i class="fa fa-times"></i><br>'
				html+= error2
				self.session['error2'] = ''
				html+= '<br><button class="closemodal">Aceptar</button></div>'
			elif error3:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="error">Ha habido un problema<br><i class="fa fa-times"></i><br>'
				html+= error3
				self.session['error3'] = ''
				url = '/login#signup'
				html+= '<br><button class="closemodal">Aceptar</button></div>'

			if success:
				html += '<div class="bg"></div><div'
				html += ' class="msgmodal" id="success">Grandioso<br><i class="fa fa-check"></i><br>'
				html+= success
				self.session['success'] = ''
				url = '/login#signup'
				html+= '<br><button class="closemodal">Aceptar</button></div>'
			'''
			if self.request.get('error'):
				html += '<div id="modalmessage">\
				<h2>Hemo tenido los siguientes problemas</h2>'
				if self.request.get('error',None) == '1':
					html+='<span>El usuario registrado ya existe en el sistema</span>'
				elif self.request.get('error',None) == '2':
					html += '<span>Los datos ingresados son incorrectos</span>'
				elif self.request.get('error',None) == '3':
					html += '<span>El usuario no existe el sistema</span>'
				html += '<button id="close">Aceptar</button></div>'			
			if self.request.get('success'):
				html += '<div id="modalmessage">\
				<h2>Registro exitoso bienvenido a TIPOO</h2>'
			'''
			template_values={
				"html":html,
			}
			self.response.write(login_template.render(template_values))
			return 0
		elif user == user_type.student:
			self.redirect('/explorer')
			return 1
		elif user == user_type.tutor:
			self.redirect('/home')
			return 2
		else:
			return 3
		
	def post(self):

		user = self.get_user_type()		
		if user == user_type.visitor:			
			self.response.write(html)
			#template_values={}
			#self.response.write(login_template.render(template_values))
			return 0
		elif user == user_type.student:
			self.redirect('/explorer')
			return 1
		elif user == user_type.tutor:
			self.redirect('/home')
			return 2
		else:

			return 3
