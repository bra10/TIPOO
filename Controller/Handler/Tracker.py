'''
Created on Mar 13, 2015
Last Modified on Mar 19, 2015
@author: Thomas, Adriel, Omar
'''

import webapp2
import jinja2
import os
import json
from Controller.Management.StudentRecordsManagement import StudentRecordsManagement as student_records_management
from RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
#from Model.UserTracking.StudentRecords import StudentRecords as student_records_model
#from Model.UserTracking.Action import Action as action_model
from google.appengine.ext import db
from Controller.Management.UserManagement import StudentManagement as student_management


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
tracker_template = JINJA_ENVIRONMENT.get_template('tracker_template.tmp')

class Tracker(request_management):

	def post(self):	           
		user = self.get_user_type()                    
		if user == user_type.visitor: 
			self.redirect('/')                              
			return 0
		elif user == user_type.student:			
			user_id = self.session["user-id"]
			user_instance = student_management().find_key(user_id)							
			date_1 = self.request.get('date_1',None)
			date_2 = self.request.get('date_2',None)		
			event = self.request.get('event',None)
			content_url = self.request.get('content_url',None)
			information = self.request.get('information',None)
			site_url = self.request.get('site_url',None)
			
			if date_1 and date_2:
				list_sites_url = student_records_management().get_all_sites()
				list_events = student_records_management().get_all_events()
				list_events_site = student_records_management().get_average_student_records_site_url(user_instance.key())
				count_events = 0
				html=''										
				date_1 = str(date_1)
				date_2 = str(date_2)
				for site_url in list_sites_url:
					c=0
					if site_url == '/view_video' or site_url == '/explorer' or site_url == '/tracker':
						pass
					else:
						html+='<br /><hr /><span>'+site_url+'</span>'
						for i in range(len(list_events)):						
							html+='<br />Evento: '+str(list_events[i])
							#count_events = student_records_management().count_events(list_events[i],site_url)
							count_events = student_records_management().count_events_between_dates(date_1,date_2,list_events[i],site_url,user_instance.key())
							html+=', '+str(count_events)+' veces'
						c+=1
				#html+='</div><div>'	
				html+='<br /><hr /><span>Urls</span>'			
				list_content_urls = student_records_management().get_all_content_urls()
				for content_url in list_content_urls:
					if content_url:
						if str(content_url).find('view_video') >= 0:
							html+='<br />Url visitada: '+str(content_url)
							count_url = student_records_management().count_content_urls_between_dates(date_1,date_2,content_url,user_instance.key())
							html+=', '+str(count_url)+' veces'
				#html+='</div>'
				m = student_records_management().get_average_student_records(date_1,date_2,user_instance.key())				
				
				self.response.write(html)
			elif event and site_url:
				html=''
				user_id = int(self.session['user-id'])
				student_records_management().add(user_id,site_url,event,content_url,information)
			return 1
		elif user == user_type.tutor:			
			self.redirect('/home')
			return 2
		else:
			self.redirect('/home')	
		return 3

	def get(self):
		user = self.get_user_type()                    
		if user == user_type.visitor: 
			self.redirect('/')                   
			return 0
		elif user == user_type.student: 
			user_id = self.session["user-id"]
			user_instance = student_management().find_key(int(user_id))
								
			list_sites_url = student_records_management().get_all_sites()
			list_events = student_records_management().get_all_events()
			
			list_events_site = student_records_management().get_average_student_records_site_url(user_instance.key())
			
			count_events = 0			
			html = ''			
			html+= '<div id="tracker"><div id="content">'
			for site_url in list_sites_url:
				c=0
				if site_url == '/view_video' or site_url == '/explorer' or site_url == '/tracker':
					pass
				else:
					html+='<br /><hr /><span>'+site_url+'</span>'
					for i in range(len(list_events)):
						html+='<br />Evento: '+str(list_events[i])
						count_events = student_records_management().count_events(list_events[i],site_url,user_instance.key())
						html+=', '+str(count_events)+' veces'
					c+=1		
			html+='<br /><hr /><span>Urls</span>'		
								
			list_content_urls = student_records_management().get_all_content_urls()
			for content_url in list_content_urls:
				if content_url:
					if str(content_url).find('view_video') >= 0:
						html+='<br />Url visitada: '+str(content_url)
						count_url = student_records_management().count_content_urls(content_url,user_instance.key())
						html+=', '+str(count_url)+' veces'
			#html+='</div>'			
			template_values = {
				"html":html,
				"user":"Student",					
				"student_name":user_instance.first
			}				
			self.response.write(tracker_template.render(template_values))
			#'''
		elif user == user_type.tutor:
			self.redirect('/home')
		else:
			self.redirect('/home')
	
