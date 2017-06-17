'''
Created on Mar 1, 2015
Last Modified on Mar 18, 2015
@author: Adriel
'''
import os
import time
import json
import jinja2
import copy
from RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
explorer_template = JINJA_ENVIRONMENT.get_template('explorer_template.tmp')

class Explorer(request_management):
    '''
    Explorer
    '''
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                                    
			self.redirect('/')
			return 0
        elif user == user_type.student:                    	
			'''
			#self.response.headers['Content-Type'] = 'text/html'
			classification = self.request.get('classification',None)
			student_instance = student_management().find_key(self.session['user-id'])
			page = 1            
			list_list_videos = []
			index = 0
			list_list_video_info = []            
			list_list_counter = []
			countent = {}
			list_counter = []   
			list_content = []         
			i = 0
			list_list_vm = video_material_management().get_subjects_available_videos(page)
			for index in range(len(list_list_vm)):
				list_videos = []
				counter = {}                
				content = {}
				if list_list_vm[index]:	
					counter['tutorid'] = ''
					counter['class'] = 'subject'
					counter['title'] = (subject_management().get_subject(list_list_vm[index][0].subject.key().id())).name                    
					counter['total-video'] = video_material_management().get_all_subject_available_videos(list_list_vm[index][0].subject.key(),page)
					for subindex in range(len(list_list_vm[index])):                    
						vm = list_list_vm[index][subindex]
						video_instance = video_material_management().get_video(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = 'Deshabilitar'
						else:
							vinfo['able'] = 'Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = video_instance.content                    
						vinfo['number_views'] = video_instance.number_views
						list_videos.append(vinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_video_info.append(list_videos)
			list_list_vm = video_material_management().get_tutors_available_videos(page)        		
			x = 2
			for index in range(len(list_list_vm)):
				list_videos = []
				counter = {}                
				content = {}
				if list_list_vm[index]:			
					counter['tutorid'] = list_list_vm[index][0].tutor.key().id()
					counter['class'] = 'tutor'		
					counter['title'] = (tutor_management().find_key(list_list_vm[index][0].tutor.key().id())).first                    
					counter['total-video'] = video_material_management().get_all_tutor_available_videos(list_list_vm[index][0].tutor.key(),page)
					for subindex in range(len(list_list_vm[index])):                    
						vm = list_list_vm[index][subindex]
						video_instance = video_material_management().get_video(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = 'Deshabilitar'
						else:
							vinfo['able'] = 'Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = video_instance.content                    
						vinfo['number_views'] = video_instance.number_views
						list_videos.append(vinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_video_info.append(list_videos)				

			new_list_counter = []
			l = []
			c = 0
			for i in range(len(list_counter)):
				c = 0
				l = list_counter[i]['total-video']
				new_counter = {}
				for j in range(len(l)):
					if l[j].available:
						c+=1
				# for j in range(len(list_counter[i])):
				# 	if list_counter[i][j]['total-video'].available:
				# 		c += 1
				new_counter['num_videos'] = c
				new_list_counter.append(copy.deepcopy(new_counter))

			html = ''			
			for i in range(len(list_list_video_info)):                
				if  x==2:
					html += '<div class="block '+str(list_counter[i]['class'])+'" data-tutor-id="'+str(list_counter[i]['tutorid'])+'" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['title'])+'</span><small> ('+str(new_list_counter[i]['num_videos'])+' Videos)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'
				else:
					html += '<div class="block '+str(list_counter[i]['class'])+'" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['title'])+'</span><small> (# Videos)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'					
				for j in range(len(list_list_video_info[i])):
					html +='\
					<a class="videor" href="view_video?video_material_id='+str(list_list_video_info[i][j]['id'])+'" alt="'+str(list_list_video_info[i][j]['topic'])+'">\
					<div class="video" id="'+str(list_list_video_info[i][j]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="views">\
					<i class="fa fa-eye"></i> '+str(list_list_video_info[i][j]['number_views'])+'\
					</div>\
					</div>\
					<div class="about">\
					<h2>'+str(list_list_video_info[i][j]['topic'])+'</h2>\
					<small>por '+str(list_list_video_info[i][j]['tutor'])+'</small>\
					</div>\
			 		</div>\
			 		</a>  '
			 	# if len(list_counter[i]['total-video']) > 6:
			 	if new_list_counter[i]['num_videos'] > 6:
			 		html += '<div class="more"><i class="fa fa-refresh"></i> Mostrar mas</div>'                    
			 	html += '</div>'           

			template_values={
				"user":"Student",
				"header_welcome":"",
				"header_tutor":"",
				"list_list_videos": list_list_video_info,                
				"counter":list_counter,
				"html":html,
				"student_name":student_instance.first
			}
			self.response.write(explorer_template.render(template_values)) 
			'''
			self.redirect('/home')
			return 1
        elif user == user_type.tutor:                      	        
			self.redirect('/home')            
			return 2                    
        else:          	        
			self.redirect('/home')                                         
			return 3
        
    def post(self):
    	user = self.get_user_type()                    
        if user == user_type.visitor:                    
			self.redirect('/')			               
			return 0
        elif user == user_type.student:
			page = self.request.get('vm_page',None)   
			tutor_id = self.request.get('vm_tutor',None)
			subject_name = self.request.get('vm_subject')
			list_list_videos = []			
			index = 0
			list_videos = []                  
			enter = False
			if tutor_id:
				tutor_id = int(tutor_id)
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				list_vm = video_material_management().get_tutor_available_videos(tutor_key,page)       
				enter = True
			elif subject_name:
				subject_instance = subject_management().find_name(subject_name)
				list_vm = video_material_management().get_subject_available_videos(subject_instance.key(),page)
				enter = True

			if enter == True:
				for index in range(len(list_vm)):                    
					vm = list_vm[index]
					video_instance = video_material_management().get_video(vm)
					vinfo = {}        
					vinfo['id'] = vm.key().id()          
					if vm.available == True:
						vinfo['able'] = 'Deshabilitar'
					else:
						vinfo['able'] = 'Habilitar'
					vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
					vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
					vinfo['content'] = video_instance.content                    
					vinfo['number_views'] = video_instance.number_views
					list_videos.append(vinfo)                      

				html = ''
				for i in range(len(list_videos)):                
					html +='\
					\
					<a class="videor" href="view_video?video_material_id='+str(list_videos[i]['id'])+'" alt="'+str(list_videos[i]['topic'])+'">\
					<div class="video" id="'+str(list_videos[i]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="views">\
					<i class="fa fa-eye"></i> '+str(list_videos[i]['number_views'])+'\
					</div>\
					</div>\
					<div class="about">\
					<h2>'+str(list_videos[i]['topic'])+'</h2>\
					<small>por '+str(list_videos[i]['tutor'])+'</small>\
					</div>\
					</div>\
					</a>  '												
				self.response.write(html)
			
			return 1
        elif user == user_type.tutor:              
            self.redirect('/home')
            return 2                    
        else:                   
			self.redirect('/home')                                         
			return 3
