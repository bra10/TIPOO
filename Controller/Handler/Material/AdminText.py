
import os
import time
import json
import jinja2
import copy

from math import ceil as ceil
from google.appengine.ext import db
from Model.ContentMaterial.TextMaterial import TextMaterial as text_material
from Controller.Lib.UserType import UserType as user_type
from time import sleep
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management


JINJA_ENVIRONMENT = jinja2.Environment(
                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
admi_text_template = JINJA_ENVIRONMENT.get_template('admin_text_template.tmp')

class AdminText(request_management):
	list_list_tm = 0
	def get(self):
		user = self.get_user_type()                  
		if user == user_type.visitor:                    
			self.redirect('/')
			return 0
		elif user == user_type.student:     
			list_list_texts = []
			tutor_id = self.session['user-id']
			student_instance = student_management().get_student(int(self.session['user-id']))
			tutor = tutor_management().get_all_tutors()[0]			
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
			page = int(self.request.get('page',0))
			unit_id = self.request.get('unit_id',None)
			if unit_id:
				unit_id = int(unit_id)
			else:
				##id de 1era unidad
				unit_id = 5750892489867264
			page = self.request.get('page',0)
			try:
				int(page)
				page = int(page)-1
			except ValueError:
				page = 0
			if page < 1:
				page = 0
			index = 0
			unit = unit_management().get_unit(unit_id)
			list_list_text_info = []            
			countent = {}
			list_counter = []   
			list_content = []  
			listi = []
			list_all_texts = text_material_management().get_all_unit_available_texts(unit.key().id())
			for t in student_instance.tutors_list:
				listi.extend(text_material_management().get_all_texts_material(t,subject,page))    
			list_tm = text_material_management().get_unit_available_texts(unit.key().id(),page)
			c=0                        
			list_texts = []
			total_text = 0
			if list_tm:				
				#total_text = text_material_management().get_all_texts_material(tutor_key,self.list_list_tm[index][0].subject.key(),page)
				for index in range(len(list_tm)):
					tm = list_tm[index]
					text_instance = text_material_management().get_text(tm)
					tinfo = {}        
					tinfo['id'] = tm.key().id()          
					tinfo['able'] = tm.available
					tinfo['tutor'] = (tutor_management().get_tutor(tm.tutor.key().id())).first
					tinfo['topic'] = (topic_management().get_topic(tm.topic.key().id())).name                    
					tinfo['content'] = text_instance.content                    
					tinfo['number_views'] = text_instance.number_views
					tinfo['description'] = 	text_instance.description					
					list_texts.append(tinfo)
					index = index + 1								
			html = ''
			
			pages = int(ceil(len(list_all_texts)/10.))
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			template_values={
				"user":"Student",
				"header_welcome":"",
				"header_tutor":"",
                "total_pages":len(list_page),
                "current_page":(page+1),
				"list_texts": list_texts,
				"unit_id": unit_id,                
				"pages":list_page,
				"Titulo":"Gestion de Textos",
				"counter":list_counter,
				"html":html,
				"subject":subject.name,
				"student_name": student_instance.first
			}                  
			self.response.write(admi_text_template.render(template_values))  
			return 1		

		elif user == user_type.tutor:                          
			list_list_texts = []
			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
			page = self.request.get('page',0)
			try:
				int(page)
				page = int(page)-1
			except ValueError:
				page = 0
			if page < 1:
				page = 0
			index = 0
			list_list_text_info = []            
			countent = {}
			list_counter = []   
			list_content = []  
			listi = text_material_management().get_all_texts_material(tutor_key,subject,page)      
			#self.list_list_tm = text_material_management().get_list_text_material_of_subject(tutor_key,page)
			list_tm = text_material_management().get_list_text_material_of_one_subject(tutor_key,subject.key(),page)
			
			
			c=0                        
			list_texts = []
			total_text = 0
			if list_tm:				
				#total_text = text_material_management().get_all_texts_material(tutor_key,self.list_list_tm[index][0].subject.key(),page)
				for index in range(len(list_tm)):
					tm = list_tm[index]
					text_instance = text_material_management().get_text(tm)
					tinfo = {}        
					tinfo['id'] = tm.key().id()          
					tinfo['able'] = tm.available
					tinfo['tutor'] = (tutor_management().get_tutor(tm.tutor.key().id())).first
					tinfo['topic'] = (topic_management().get_topic(tm.topic.key().id())).name                    
					tinfo['content'] = text_instance.content                    
					tinfo['number_views'] = text_instance.number_views
					tinfo['description'] = 	text_instance.description					
					list_texts.append(tinfo)
					index = index + 1								
			html = ''
			
			pages = int(ceil(len(listi)/10.))
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			template_values={
				"user":"Tutor",
				"header_welcome":"",
				"header_tutor":"",
                "total_pages":len(list_page),
                "current_page":(page+1),
				"list_texts": list_texts,
				"subject":subject.name,
				"pages":list_page,
				"Titulo":"Gestion de Textos",                
				"counter":list_counter,
				"tutor_name": tutor_instance.first
			}  
			                  
			self.response.write(admi_text_template.render(template_values))  
			
			return 2                                      
		else:                        
            
			admi_text_template_values = {

			}
			self.response.write(admi_text_template.render(template_values))                        
			return 3
           
	def post(self):
		user = self.get_user_type()                    
		if user == user_type.visitor:                    
                
			return 0
		elif user == user_type.student:                   
			return 1
		elif user == user_type.tutor:
			available = self.request.get('available',None)  
			delete = self.request.get('delete',None)
			page = self.request.get('vm_page',None)
			if available:
				tm_id = self.request.get('tm_id',None)                
				text_material_management().make_available(int(tm_id))                        
			if delete:
				tm_id = self.request.get('tm_id',None)
				tm_instance = text_material_management().get_text_material(int(tm_id))
				t_instance = text_material_management().get_text(tm_instance)
				text_material_management().remove(tm_instance.key(),t_instance.key())
				sleep(0.1)
			return 2
		else:
			return 3
			

