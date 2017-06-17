'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel
'''
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.MaterialManagement.VideoManagement import VideoManagement as video_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model
from Model.ContentMaterial.Video import Video as video_model
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Controller.Lib.UserType import UserType as user_type
import os
import os.path
import jinja2
from time import sleep
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
datavideo_template = JINJA_ENVIRONMENT.get_template('data_video_template.tmp')

class DataVideo(request_management, blobstore_handlers.BlobstoreUploadHandler):

	def get(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:			
			if not 'video-id' in self.session:
				self.session['video-id'] = None
			video_content = ''
			if self.session['video-id'] == None:
				self.redirect('/home')

			try:
				video_id = int(self.session['video-id'])				
				video_instance = video_management().get_video(video_id)
				video_content = video_instance.content
			except ValueError:									
				video_content = ''		
			except TypeError:
				video_id = 0	

			template_values={
			    "user":"Student",   
			    "header_welcome":"",
			    "header_user":"",
                "edit":False,
			    "video_content":video_content			    
			}
			self.response.write(datavideo_template.render(template_values))  			
		elif user == user_type.tutor:			
			video_material_id = self.request.get('video_material_id',None)
			if not 'video-id' in self.session:
				self.session['video-id'] = None
			if not 'name_file' in self.session:
				self.session['name_file'] = None	
			if not 'extension' in self.session:
				self.session['extension'] = None		

			if self.session['video-id'] == None and self.session['name_file'] == None and video_material_id is None:
				self.redirect('/home')
											
			video_format_allowed = ['mp4','wmv','mkv','ogg','webm']
			if not self.session['extension'] in video_format_allowed and video_material_id is None:
				self.redirect('/upload_video')

			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
				
			if video_material_id:			
				video_material_id = int(video_material_id)	
				video_material_instance = video_material_management().get_video_material(video_material_id)
				video_instance = video_material_management().get_video(video_material_instance)									
				vinfo = {}                                
				vinfo['topic'] = video_material_instance.topic
				vinfo['description'] = video_instance.description
				vinfo['level'] = video_material_instance.level
				vinfo['tags'] = video_material_instance.tags
				video_content = video_instance.content
				l_u=[]
				sub = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
				list_unit = unit_management().get_all_units_of_subject(sub.key())		
				
				for u in list_unit:
					_u = {}
					_u['name'] = u.name
					_u['id'] = u.key().id()
					l_u.append(_u)			
				template_values = {
					"user":"Tutor",
					"vinfo":vinfo,
					"video_content":video_content,
					"list_unit":l_u,
					"name_file":self.session['name_file'],
                    "edit":True,
					"tutor_name": tutor_instance.first,
					"video_material_id":video_material_id
				}
			else:
				video_content = ''
				l_s = []
				l_u=[]
				try:
					video_id = int(self.session['video-id'])				
					video_instance = video_management().get_video(video_id)
					video_content = video_instance.content
				except ValueError:									
					video_content = ''		
				except TypeError:
					video_id = 0
				sub = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
				list_unit = unit_management().get_all_units_of_subject(sub.key())		
				
				for u in list_unit:
					_u = {}
					_u['name'] = u.name
					_u['id'] = u.key().id()
					l_u.append(_u)

				template_values={
					"user":"Tutor",   
					"header_welcome":"",
					"header_tutor":"",
					"video_content":video_content,
					"list_unit":l_u,
					"name_file":self.session['name_file'],
					"tutor_name": tutor_instance.first,
					"video_material_id":"",
				}        
			self.response.write(datavideo_template.render(template_values))			
		else:
			self.redirect('/')

	def post(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			self.redirect('/')
		elif user == user_type.student:
			self.redirect('/')
		elif user == user_type.tutor:			

			if not 'video_material_id' in self.session:
				self.session['video_material_id'] = None
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
			video_material_id = self.request.get('video_material_id',None)
			if video_material_id:
				video_material_id = int(video_material_id)
				video_material_instance = video_material_management().get_video_material(video_material_id)
				topic_ins = topic_management().get_topic(video_material_instance.topic.key().id())
				topic_management().modify(subject.key(),topic_ins.key(),topic)								
				video_ins = video_management().get_video(video_material_instance.video.key().id())
				video_management().modify(video_ins.key(),description,video_ins.size)
				video_material_management().modify(video_material_instance.key(),video_ins.key(),level,unit_id,subject.key(),topic_ins.key(),tags,tutor_key)
			else:				
				size = self.session['size']
				self.session['size'] = None
				size = int(size)
				duration = self.request.get('duration',None)
				ext_format = self.session['extension']
				#size = self.request.get('size',None)
				topic_key = topic_management().add(subject.key(),topic)				
				video_id = int(self.session['video-id'])
				self.session['video-id'] = None
				video_instance = video_management().get_video(video_id)	
				video_key = video_management().add(video_instance.key(),description,duration,ext_format,size,0)
				video_material_management().add(video_key,level,unit_id,subject.key(),topic_key,tags,tutor_key)				
			sleep(0.1)
			self.redirect('/admin_video')       	
		else:
			self.redirect('/')

        

