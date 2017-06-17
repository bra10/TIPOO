'''
Created on Dec 12, 2013
Last Modified on Mar 1, 2015@author: Raul, Adriel
'''
import os
import jinja2
#from cgi import escape
from Controller.DataProcessing.EmailConfirmation import EmailConfirmation as email_confirmation
from Controller.Lib.UserType import UserType as user_type
from Controller.DataProcessing.InputField import InputField as input_field
from Controller.Management.UserManagement import StudentManagement as student_management
from RequestManager import RequestManagement as request_management

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('signup_template.tmp')

class Signup(request_management):
    '''
    Signup
    '''
    def post(self):
        user=self.get_user_type()
        errors={}        
        if user == user_type.visitor:            
            #email=escape(self.request.get('email',None))  
            email=self.request.get('email',None)
            email.lower()            
            email.strip()                      
            #pwd=input_field().encrypt_password(escape(self.request.get('pwd',None)))
            pwd=input_field().encrypt_password(self.request.get('pwd',None))
            pwd.lower()
            pwd.strip()                    
            #first = escape(self.request.get('user',None))
            first = self.request.get('user',None)            
            
            if student_management().add_basic_info(first,email, pwd):
                #email_confirmation().send_mail(email)
                self.session['success'] = '<h2>Registro exitoso bienvenido a TIPOO</h2>'
                self.redirect('/login#signup')
            else:                
                self.session['error3'] = '<span>El usuario registrado ya existe en el sistema</span>'
                self.redirect('/login#signup')
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
            '''
            template_values = {
            
            }
            archivo_html = open('View/signup.html', 'r')
            self.response.write(archivo_html.read())
            #self.response.write(template.render(template_values))
            '''
            self.redirect('/login#signup')
            return 0
        elif user == user_type.student:
            self.redirect('/home')
            return 1
        elif user == user_type.tutor:
            self.redirect('/home')
            return 2
        else:
            template_values = {

            }
            self.response.write(template.render(template_values))
            return 3    
