'''
Created on Feb 22, 2015

@author: Adriel
'''
import os
import urllib

from google.appengine.ext.webapp import blobstore_handlers
import jinja2
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.MaterialManagement.VideoManagement import VideoManagement as video_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
viewvideo_template = JINJA_ENVIRONMENT.get_template('view_video_template.tmp')

class ViewVideo(request_management,blobstore_handlers.BlobstoreDownloadHandler):
    
    def get(self):
        user = self.get_user_type()
        if user == user_type.visitor:
            self.redirect('/')
        elif user == user_type.student:
            video_material_id = self.request.get('video_material_id',None)
            if not video_material_id:
                self.redirect('/explorer')
            video_instance = None        
            video_material_instance = None
            video_material_id = int(video_material_id)
            if video_material_id:                
                video_material_instance = video_material_management().get_video_material(video_material_id)
            if not video_material_instance:
                self.redirect('/explorer')                
            else:             
            	student_instance = student_management().find_key(self.session['user-id'])
                video_instance = video_material_management().get_video(video_material_instance)                        
                video_management().update_number_views(video_instance)
                list_tag_video_supported = ['mkv','mp4']
                list_tag_embedded_supported = ['wmv','mov','mpg','avi']
                #list_tag_object_supported = ['swf'] 
                vformat = video_instance.ext_format                
                vinfo = {}
                vinfo['format'] = vformat
                vinfo['tutor'] = (tutor_management().get_tutor(video_material_instance.tutor.key().id())).first
                vinfo['topic'] = (topic_management().get_topic(video_material_instance.topic.key().id())).name                    
                vinfo['content'] = video_instance.content
                vinfo['subject'] = (subject_management().get_subject(video_material_instance.subject.key().id())).name
                vinfo['description'] = video_instance.description
                vinfo['tags'] = video_material_instance.tags
                template_values={
                    "user":"Student",   
                    "header_welcome":"",
                    "header_tutor":"",                
                    "vinfo":vinfo,            
                    'embbeded_supported':list_tag_embedded_supported,
                    'video_supported':list_tag_video_supported,
                    "student_name":student_instance.first
                    #"object_supported":list_tag_object_supported
                }                                           
                self.response.write(viewvideo_template.render(template_values))            
        elif user == user_type.tutor:
            video_material_id = int(self.request.get('video_material_id', None))
            video_instance = None        
            video_material_instance = None
            if video_material_id:                
                video_material_instance = video_material_management().get_video_material(video_material_id)
            if not video_material_instance:
                self.redirect('/home')                
            else:
				tutor_id = self.session['user-id']
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				tutor_instance = tutor_management().get_tutor(tutor_id)
				video_instance = video_material_management().get_video(video_material_instance)                                                
				list_video_supported = ['mp4','wmv','mkv','ogg','webm']
				vformat = video_instance.ext_format            
				#list_tag_object_supported = ['swf']
				vinfo = {}
				vinfo['format'] = vformat
				vinfo['tutor'] = (tutor_management().get_tutor(video_material_instance.tutor.key().id())).first
				vinfo['topic'] = (topic_management().get_topic(video_material_instance.topic.key().id())).name                    
				vinfo['content'] = video_instance.content
				vinfo['subject'] = (subject_management().get_subject(video_material_instance.subject.key().id())).name
				vinfo['description'] = video_instance.description
				vinfo['tags'] = video_material_instance.tags
				#blob_info = BlobInfo.get(video_instance.content.key())
				template_values={
					"user":"Tutor",   
					"header_welcome":"",
					"header_tutor":"",                
					"vinfo":vinfo,                                
					"tutor_name": tutor_instance.first,					
					#"object_supported":list_tag_object_supported
				}         
				#self.response.headers['Content-Type'] = 'video/avi'
				self.response.write(viewvideo_template.render(template_values))            
        else:
            self.redirect('/home')

    def post(self):
        user = self.get_user_type()
        if user == user_type.visitor:
            self.redirect('/')
        elif user == user_type.student:
            self.redirect('/explorer')
        elif user == user_type.tutor:           
            self.redirect('/home')          
        else:
            self.redirect('/home')

        
