'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel
'''
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.MaterialManagement.VideoManagement import VideoManagement as video_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model
from Model.ContentMaterial.Video import Video as video_model
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Controller.Lib.UserType import UserType as user_type

import os
import os.path
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
uploadvideo_template = JINJA_ENVIRONMENT.get_template('upload_video_template.tmp')

class UploadVideo(request_management, blobstore_handlers.BlobstoreUploadHandler):

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
			self.response.write(uploadvideo_template.render(template_values))  						
		elif user == user_type.tutor:            
			self.session['extension'] = None
			self.session['name_file'] = None
			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
			# video_id = None
			# if 'video-id' in self.session:
			# 	video_id = self.session['video-id']
			# if video_id:
			# 	video_management().delete(video_id)				
			self.session['video-id'] = None			
			template_values={
                "user":"Tutor",   
                "header_welcome":"",
                "header_tutor":"",
                "upload_url":blobstore.create_upload_url('/upload_video'),
                "tutor_name": tutor_instance.first
            }            			
			self.response.write(uploadvideo_template.render(template_values))			
		else:
			self.redirect('/')

	def post(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:
			self.redirect('/')
		elif user == user_type.tutor:				
			upload_video = self.get_uploads()[0]			
			blob_info = upload_video				
			video_properties = blob_info.properties()			
			video_info = blob_info.get(blob_info.key())
			video_name = video_info.filename				
			extension = os.path.splitext(video_name)[-1]			
			extension = extension[1:]
			self.session['extension'] = extension
			self.session['name_file'] = video_name						
			self.session['size'] = video_info.size
			video_format_allowed = ['mp4','wmv','mkv','ogg','webm']
			if extension in video_format_allowed:			 	
			 	video_instance = video_management().add_content(blob_info)	
			 	self.session['video-id'] = video_instance.id()				
				self.response.write('{"status":"success"}')								
			else:					
			 	self.response.write('{"status":"error"}')				
			
		else:
			self.redirect('/')
			

        

