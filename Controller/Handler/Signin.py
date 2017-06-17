'''
Created on Jan 17, 2014
Last modified on Mar 1, 2015
@author: Raul, Adriel
'''
import os
import time
from google.appengine.ext import db
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import AdminManagement as admin_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Handler.UserSession import UserSession as user_session
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.DataProcessing.InputField import InputField as input_field


class Signin(request_management):
    '''
    Home
    '''
    def post(self):
        user=self.get_user_type() 
        
        session = self.session  
        if user == user_type.visitor:
            #visitor
			user_email=self.request.get('email',None)
			user_pwd=input_field().encrypt_password( self.request.get('pwd',None) )                                    
			if not user_email or not user_pwd:                
				self.redirect('/login')                
			else:
				user_data = user_session().find_user(user_email)                                                                
				if user_data:
					if user_data.password == user_pwd:
						if user_data.activate == True:
							user = user_session().new_user_type(user_email)                                                        
							user_session().init(session, user, user_data, time.time())                        
							if self.session['user'] == user_type.tutor:                                
								self.redirect('/home')                                
							elif self.session['user'] == user_type.student:                                
								self.redirect('/home')                                                                                      
						else:                            
							self.session['error'] = '0'
							self.redirect('/login')                            
					else:           
						self.session['error1'] = '<span>Los datos ingresados son incorrectos</span>'
						self.redirect('/login')                        
				else:                                           
					self.session['error2'] = '<span>El usuario no existe el sistema</span>'
					self.redirect('/login')                            
			return 0
                
        elif user == user_type.student:
            self.redirect('/home')
            return 1
        elif user == user_type.tutor:
            self.redirect('/home')
            return 2
        else:
            self.redirect('/home')
            return 3
        

    def get(self):
        user=self.get_user_type()           
        if user == user_type.visitor:            
            self.redirect('/')
            return 0
        elif user == user_type.student:
            self.redirect('/explorer')
            return 1
        elif user == user_type.tutor:
            self.redirect('/home')
            return 2
        else:
            self.redirect('/home')
            return 3        
                             