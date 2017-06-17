'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel, Omar
'''
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
from Controller.Management.MaterialManagement.TextManagement import TextManagement as text_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model
from Model.ContentMaterial.Text import Text as text_model
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Controller.Lib.UserType import UserType as user_type
from time import sleep
import os
import os.path
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
data_text_template = JINJA_ENVIRONMENT.get_template('data_text_template.tmp')

class DataText(request_management, blobstore_handlers.BlobstoreUploadHandler):

	def get(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:			
			if not 'text-id' in self.session:
				self.session['text-id'] = None
			text_content = ''
			if self.session['text-id'] == None:
				self.redirect('/home')

			try:
				text_id = int(self.session['text-id'])				
				text_instance = text_management().get_text(text_id)
				text_content = text_instance.content
			except ValueError:									
				text_content = ''		
			except TypeError:
				text_id = 0	

			template_values={
			    "user":"Student",   
			    "header_welcome":"",
			    "header_user":"",
			    "text_content":text_content			    
			}
			self.response.write(data_text_template.render(template_values))  			
		elif user == user_type.tutor:			
			text_material_id = self.request.get('text_material_id',None)
			if not 'text-id' in self.session:
				self.session['text-id'] = None
			if not 'name_file' in self.session:
				self.session['name_file'] = None	
			if not 'name_file' in self.session:
				self.session['extension'] = None		
			
			if self.session['text-id'] == None and self.session['name_file'] == None and text_material_id is None:
				self.redirect('/home')
											
			text_format_allowed = ['pdf']

			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
				
			if text_material_id:				
				text_material_id = int(text_material_id)
				text_material_instance = text_material_management().get_text_material(text_material_id)
				text_instance = text_material_management().get_text(text_material_instance)
				tinfo = {}                                
				tinfo['topic'] = text_material_instance.topic
				tinfo['description'] = text_instance.description
				tinfo['level'] = text_material_instance.level
				tinfo['tags'] = text_material_instance.tags
				text_content = text_instance.content
				subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
				subject_units = unit_management().get_all_units_of_subject(subject.key())
				list_units = []
				for unit in subject_units:
					uinfo = {}
					uinfo['name'] = unit.name
					uinfo['id'] = unit.key().id()
					list_units.append(uinfo)				
				template_values = {
					"user":"Tutor",
					"tinfo":tinfo,
					"edit":True,
					"text_content":text_content,
					"list_units":list_units,
					"name_file":self.session['name_file'],
					"tutor_name": tutor_instance.first,
					"text_material_id":text_material_id
				}				
			else:
				text_content = ''
				try:
					text_id = int(self.session['text-id'])				
					text_instance = text_management().get_text(text_id)
					text_content = text_instance.content
				except ValueError:									
					text_content = ''		
				except TypeError:
					text_id = 0
				subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
				subject_units = unit_management().get_all_units_of_subject(subject.key())
				list_units = []
				for unit in subject_units:
					uinfo = {}
					uinfo['name'] = unit.name
					uinfo['id'] = unit.key().id()
					list_units.append(uinfo)
				template_values={
					"user":"Tutor",   
					"header_welcome":"",
					"edit":False,
					"header_tutor":"",
					"text_content":text_content,
					"list_units":list_units,
					"name_file":self.session['name_file'],
					"tutor_name": tutor_instance.first,
					"text_material_id":""
				}        
			self.response.write(data_text_template.render(template_values))			
		else:
			self.redirect('/')

	def post(self):
		user = self.get_user_type()		
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:
			self.redirect('/')
		elif user == user_type.tutor:			
			if not 'text_material_id' in self.session:
				self.session['text_material_id'] = None
			if not 'extension' in self.session:
				self.session['extension'] = None
			if not 'size' in self.session:
				self.session['size'] = None
			title = self.request.get('title',None)
			description = self.request.get('description',None)
			level = int(self.request.get('level',None))
			unit_id = self.request.get('unit',None)
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
			if unit_id:
				unit_id = int(unit_id)
			topic = title
			tags = self.request.get_all('tags',None)				  			
			tutor_key = tutor_management().get_tutor(self.session['user-id']).key()
			text_material_id = self.request.get('text_material_id',None)			
			if text_material_id:
				text_material_id = int(text_material_id)
				text_material_instance = text_material_management().get_text_material(text_material_id)
				topic_ins = topic_management().get_topic(text_material_instance.topic.key().id())				
				topic_management().modify(subject.key(),topic_ins.key(),topic)
				text_ins = text_management().get_text(text_material_instance.text.key().id())							
				text_management().modify(text_ins.key(),description,text_ins.size)
				text_material_management().modify(text_material_instance.key(),text_ins.key(),level,unit_id,subject.key(),topic_ins.key(),tags,tutor_key)
			else:							
				size = self.session['size']
				size = int(size)
				ext_format = self.session['extension']
				topic_key = topic_management().add(subject.key(),topic)				
				text_id = self.session['text-id']
				if text_id:
					text_id=int(text_id)
				self.session['text-id'] = None
				self.session['text_material_id'] = None
				text_instance = text_management().get_text(text_id)	
				text_key = text_management().add(text_instance.key(),description,ext_format,size,0)
				text_material_management().add(text_key,level,unit_id,subject.key(),topic_key,tags,tutor_key)		
			sleep(0.1)					
			self.redirect('/admin_text')       	
		else:
			self.redirect('/')