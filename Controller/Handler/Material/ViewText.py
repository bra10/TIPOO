'''
Created on Feb 22, 2015

@author: Adriel, Omar
'''
import os
import urllib

from google.appengine.ext.webapp import blobstore_handlers
import jinja2
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
from Controller.Management.MaterialManagement.TextManagement import TextManagement as text_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
viewtext_template = JINJA_ENVIRONMENT.get_template('view_text_template.tmp')

class ViewText(request_management,blobstore_handlers.BlobstoreDownloadHandler):
    
    def get(self):
        user = self.get_user_type()
        if user == user_type.visitor:
            self.redirect('/')
        elif user == user_type.student:
            text_material_id = self.request.get('text_material_id',None)
            if not text_material_id:
                self.redirect('/explorer')
            text_instance = None        
            text_material_instance = None
            text_material_id = int(text_material_id)
            if text_material_id:                
                text_material_instance = text_material_management().get_text_material(text_material_id)
            if not text_material_instance:
                self.redirect('/explorer')                
            else:             
            	student_instance = student_management().find_key(self.session['user-id'])
                text_instance = text_material_management().get_text(text_material_instance)                        
                text_management().update_number_views(text_instance)
                list_tag_text_supported = ['pdf']
                list_tag_embedded_supported = ['pdf']
                #list_tag_object_supported = ['swf'] 
                tformat = text_instance.ext_format                
                tinfo = {}
                tinfo['format'] = tformat
                tinfo['tutor'] = (tutor_management().get_tutor(text_material_instance.tutor.key().id())).first
                tinfo['topic'] = (topic_management().get_topic(text_material_instance.topic.key().id())).name                    
                tinfo['content'] = text_instance.content
                tinfo['subject'] = (subject_management().get_subject(text_material_instance.subject.key().id())).name
                tinfo['description'] = text_instance.description
                tinfo['tags'] = text_material_instance.tags
                template_values={
                    "user":"Student",   
                    "header_welcome":"",
                    "header_tutor":"",                
                    "tinfo":tinfo,            
                    'embbeded_supported':list_tag_embedded_supported,
                    'text_supported':list_tag_text_supported,
                    "student_name":student_instance.first
                    #"object_supported":list_tag_object_supported
                }                                           
                self.response.write(viewtext_template.render(template_values))            
        elif user == user_type.tutor:
            text_material_id = int(self.request.get('text_material_id'))
            text_instance = None        
            text_material_instance = None
            if text_material_id:                
                text_material_instance = text_material_management().get_text_material(text_material_id)
            if not text_material_instance:
                self.redirect('/home')                
            else:
				tutor_id = self.session['user-id']
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				tutor_instance = tutor_management().get_tutor(tutor_id)
				text_instance = text_material_management().get_text(text_material_instance)                                                
				list_text_supported = ['pdf']
				tformat = text_instance.ext_format            
				#list_tag_object_supported = ['swf']
				tinfo = {}
				tinfo['format'] = tformat
				tinfo['tutor'] = (tutor_management().get_tutor(text_material_instance.tutor.key().id())).first
				tinfo['topic'] = (topic_management().get_topic(text_material_instance.topic.key().id())).name                    
				tinfo['content'] = text_instance.content
				tinfo['subject'] = (subject_management().get_subject(text_material_instance.subject.key().id())).name
				tinfo['description'] = text_instance.description
				tinfo['tags'] = text_material_instance.tags
				#blob_info = BlobInfo.get(text_instance.content.key())
				template_values={
					"user":"Tutor",   
					"header_welcome":"",
					"header_tutor":"",                
					"tinfo":tinfo,                                
					"tutor_name": tutor_instance.first,					
					#"object_supported":list_tag_object_supported
				}         
				#self.response.headers['Content-Type'] = 'video/avi'
				self.response.write(viewtext_template.render(template_values))            
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
			
			
			

        
