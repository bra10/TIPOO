'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel, Omar
'''
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
from Controller.Management.MaterialManagement.TextManagement import TextManagement as text_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model
from Model.ContentMaterial.Text import Text as text_model
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Controller.Lib.UserType import UserType as user_type

import os
import os.path
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
uploadtext_template = JINJA_ENVIRONMENT.get_template('upload_text_template.tmp')

class UploadText(request_management, blobstore_handlers.BlobstoreUploadHandler):

	def get(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:
			template_values={
                "user":"Student",   
                "header_welcome":"",
                "header_user":""
            }
			self.response.write(uploadtext_template.render(template_values))  						
		elif user == user_type.tutor:            
			self.session['extension'] = None
			self.session['name_file'] = None
			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
			# text_id = None
			# if 'text-id' in self.session:
			# 	text_id = self.session['text-id']
			# if text_id:
			# 	text_management().delete(text_id)				
			self.session['text-id'] = None			
			template_values={
                "user":"Tutor",   
                "header_welcome":"",
                "header_tutor":"",
                "upload_url":blobstore.create_upload_url('/upload_text'),
                "tutor_name": tutor_instance.first
            }            			
			self.response.write(uploadtext_template.render(template_values))			
		else:
			self.redirect('/')

	def post(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:
			self.redirect('/')
		elif user == user_type.tutor:				
			upload_text = self.get_uploads()[0]			
			blob_info = upload_text				
			text_properties = blob_info.properties()			
			text_info = blob_info.get(blob_info.key())
			text_name = text_info.filename				
			extension = os.path.splitext(text_name)[-1]			
			extension = extension[1:]
			self.session['extension'] = extension
			self.session['name_file'] = text_name						
			self.session['size'] = text_info.size
			text_format_allowed = ['pdf']
			if extension in text_format_allowed:			 	
			 	text_instance = text_management().add_content(blob_info)	
			 	self.session['text-id'] = text_instance.id()				
				self.response.write('{"status":"success"}')								
			else:					
			 	self.response.write('{"status":"error"}')				
			
		else:
			self.redirect('/')
			

        

