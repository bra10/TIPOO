import os
import jinja2
from Controller.Lib.UserType import UserType as user_type

from RequestManager import RequestManagement as request_management

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
profile_template = JINJA_ENVIRONMENT.get_template('profile_template.tmp')

class Profile(request_management):
	def get(self):
		user = self.get_user_type()                    
		if user == user_type.visitor:                                   
			return 0
		elif user == user_type.student:    
			return 1
		elif user == user_type.tutor:  
			template_values = {
			}
			self.response.write(profile_template.render(template_values))                        
			return 2                    
		else:                        	           	    			
			return 3

	def post(self):

		pass