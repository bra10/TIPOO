
import os
import time
import json
import jinja2
import copy

from math import ceil as ceil
from google.appengine.ext import db
from Model.ContentMaterial.VideoMaterial import VideoMaterial as video_material
from Controller.Lib.UserType import UserType as user_type
from time import sleep
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management


JINJA_ENVIRONMENT = jinja2.Environment(
                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
admin_video_template = JINJA_ENVIRONMENT.get_template('admin_video_template.tmp')

class AdminVideo(request_management):
    list_list_vm = 0
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:                 
			student_instance = student_management().get_student(int(self.session['user-id']))
			tutor = tutor_management().get_all_tutors()[0]            
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')			
			unit_id = self.request.get('unit_id',None)
			if unit_id:
				unit_id = int(unit_id)
			else:
				##id de 1era unidad
				unit_id = 6348855016685568
			page = self.request.get('page',0)
			try:
				int(page)
				page = int(page)-1
			except ValueError:
				page = 0
			if page < 1:
				page = 0
			unit = unit_management().get_unit(unit_id)
			list_list_text_info = []            
			countent = {}
			list_counter = []   
			list_content = []
			listi = []
			list_all_videos = video_material_management().get_all_unit_available_videos(unit.key().id())
			for t in student_instance.tutors_list:
				listi.extend(video_material_management().get_all_videos_material(t,subject.key(),page))       
			self.list_list_vm = video_material_management().get_list_video_material_of_subject(tutor.key(),page)                        
			list_vm = video_material_management().get_unit_available_videos(unit.key().id(),page)     
			
			c=0
			list_videos = []
			total_text = 0
			if list_vm:
				for index in range(len(list_vm)):
					vm = list_vm[index]
					video_instance = video_material_management().get_video(vm)
					vinfo = {}        
					vinfo['id'] = vm.key().id()          
					vinfo['able'] = vm.available
					vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
					vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
					vinfo['content'] = video_instance.content                    
					vinfo['number_views'] = video_instance.number_views
					list_videos.append(vinfo)
					index = index + 1

			pages = int(ceil(len(list_all_videos)/10.))
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			
			html = ''
			template_values={
				"user":"Student",
				"header_welcome":"",
				"header_tutor":"",
                "total_pages":len(list_page),
                "current_page":(page+1),
				"list_videos": list_videos,
				"unit_id": unit_id,                
				"pages":list_page,
				"Titulo":"Gestion de Videos",
				"counter":list_counter,
				"html":html,
				"subject":subject.name,
				"student_name": student_instance.first
			}  
			                  
			self.response.write(admin_video_template.render(template_values))  
        	
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
			#self.list_list_vm = text_material_management().get_list_text_material_of_subject(tutor_key,pages) 

			listi = video_material_management().get_all_videos_material(tutor_key,subject,page)     
			list_vm = video_material_management().get_list_video_material_of_one_subject(tutor_key,subject.key(),page)
			c=0
			list_videos = []
			total_text = 0
			if list_vm:
				for index in range(len(list_vm)):
					vm = list_vm[index]
					video_instance = video_material_management().get_video(vm)
					vinfo = {}        
					vinfo['id'] = vm.key().id()          
					vinfo['able'] = vm.available
					vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
					vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
					vinfo['content'] = video_instance.content                    
					vinfo['number_views'] = video_instance.number_views
					list_videos.append(vinfo)
					index = index + 1
			
			pages = int(ceil(len(listi)/10.))
		
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			
			template_values={
				"user":"Tutor",
				"header_welcome":"",
				"header_tutor":"",
				"list_videos": list_videos,  
                "total_pages":len(list_page),
                "current_page":(page+1),
				"pages":list_page,
				"Titulo":"Gestion de Videos",
				"counter":list_counter,			
				"subject":subject.name,
				"tutor_name": tutor_instance.first
			}  
			                  
			self.response.write(admin_video_template.render(template_values))  
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
			pages = self.request.get('vm_page',None)
			if available:
				vm_id = self.request.get('vm_id',None)                
				video_material_management().make_available(int(vm_id))                        
			if delete:
				vm_id = self.request.get('vm_id',None)
				vm_instance = video_material_management().get_video_material(int(vm_id))
				v_instance = video_material_management().get_video(vm_instance)
				self.response.write(vm_instance.key())
				self.response.write(v_instance.key())				
				video_material_management().remove(vm_instance.key(),v_instance.key())
				sleep(0.1)
			return 2
        else:
            return 3
		
			

