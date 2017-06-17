'''
Created on May 16, 2015
Last Modified on May 16, 2015
@author: Omar
'''
import os
import time
import json
import jinja2
import copy
from RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
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
			#self.response.headers['Content-Type'] = 'text/html'
			classification = self.request.get('classification',None)
			student_instance = student_management().find_key(self.session['user-id'])
			page = 1            
			list_list_texts = []
			index = 0
			list_list_text_info = []            
			list_list_counter = []
			countent = {}
			list_counter = []   
			list_content = []         
			i = 0
			list_list_tm = text_material_management().get_subjects_available_texts(page)
			for index in range(len(list_list_tm)):
				list_texts = []
				counter = {}                
				content = {}
				if list_list_tm[index]:	
					counter['tutorid'] = ''
					counter['class'] = 'subject'
					counter['title'] = (subject_management().get_subject(list_list_tm[index][0].subject.key().id())).name                    
					counter['total-text'] = text_material_management().get_all_subject_available_texts(list_list_tm[index][0].subject.key(),page)
					for subindex in range(len(list_list_tm[index])):                    
						tm = list_list_tm[index][subindex]
						text_instance = text_material_management().get_text(tm)
						tinfo = {}        
						tinfo['id'] = tm.key().id()          
						if tm.available == True:
							tinfo['able'] = 'Deshabilitar'
						else:
							tinfo['able'] = 'Habilitar'
						tinfo['tutor'] = (tutor_management().get_tutor(tm.tutor.key().id())).first
						tinfo['topic'] = (topic_management().get_topic(tm.topic.key().id())).name                    
						tinfo['content'] = text_instance.content                    
						tinfo['number_views'] = text_instance.number_views
						list_texts.append(tinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_text_info.append(list_texts)
			list_list_tm = text_material_management().get_tutors_available_texts(page)        		
			x = 2
			for index in range(len(list_list_tm)):
				list_texts = []
				counter = {}                
				content = {}
				if list_list_tm[index]:			
					counter['tutorid'] = list_list_tm[index][0].tutor.key().id()
					counter['class'] = 'tutor'		
					counter['title'] = (tutor_management().find_key(list_list_tm[index][0].tutor.key().id())).first                    
					counter['total-text'] = text_material_management().get_all_tutor_available_texts(list_list_tm[index][0].tutor.key(),page)
					for subindex in range(len(list_list_tm[index])):                    
						tm = list_list_tm[index][subindex]
						text_instance = text_material_management().get_text(tm)
						tinfo = {}        
						tinfo['id'] = tm.key().id()          
						if tm.available == True:
							tinfo['able'] = 'Deshabilitar'
						else:
							tinfo['able'] = 'Habilitar'
						tinfo['tutor'] = (tutor_management().get_tutor(tm.tutor.key().id())).first
						tinfo['topic'] = (topic_management().get_topic(tm.topic.key().id())).name                    
						tinfo['content'] = text_instance.content                    
						tinfo['number_views'] = text_instance.number_views
						list_texts.append(tinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_text_info.append(list_texts)				

			new_list_counter = []
			l = []
			c = 0
			for i in range(len(list_counter)):
				c = 0
				l = list_counter[i]['total-text']
				new_counter = {}
				for j in range(len(l)):
					if l[j].available:
						c+=1
				# for j in range(len(list_counter[i])):
				# 	if list_counter[i][j]['total-text'].available:
				# 		c += 1
				new_counter['num_texts'] = c
				new_list_counter.append(copy.deepcopy(new_counter))

			html = ''			
			for i in range(len(list_list_text_info)):                
				if  x==2:
					html += '<div class="block '+str(list_counter[i]['class'])+'" data-tutor-id="'+str(list_counter[i]['tutorid'])+'" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['title'])+'</span><small> ('+str(new_list_counter[i]['num_texts'])+' texts)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'
				else:
					html += '<div class="block '+str(list_counter[i]['class'])+'" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['title'])+'</span><small> (# texts)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'					
				for j in range(len(list_list_text_info[i])):
					html +='\
					<a class="textr" href="view_text?text_material_id='+str(list_list_text_info[i][j]['id'])+'" alt="'+str(list_list_text_info[i][j]['topic'])+'">\
					<div class="text" id="'+str(list_list_text_info[i][j]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="views">\
					<i class="fa fa-eye"></i> '+str(list_list_text_info[i][j]['number_views'])+'\
					</div>\
					</div>\
					<div class="about">\
					<h2>'+str(list_list_text_info[i][j]['topic'])+'</h2>\
					<small>por '+str(list_list_text_info[i][j]['tutor'])+'</small>\
					</div>\
			 		</div>\
			 		</a>  '
			 	# if len(list_counter[i]['total-text']) > 6:
			 	if new_list_counter[i]['num_texts'] > 6:
			 		html += '<div class="more"><i class="fa fa-refresh"></i> Mostrar mas</div>'                    
			 	html += '</div>'           

			template_values={
				"user":"Student",
				"header_welcome":"",
				"header_tutor":"",
				"list_list_texts": list_list_text_info,                
				"counter":list_counter,
				"html":html,
				"student_name":student_instance.first
			}
			self.response.write(explorer_template.render(template_values)) 
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
			page = self.request.get('tm_page',None)   
			tutor_id = self.request.get('tm_tutor',None)
			subject_name = self.request.get('tm_subject')
			list_list_texts = []			
			index = 0
			list_texts = []                  
			enter = False
			if tutor_id:
				tutor_id = int(tutor_id)
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				list_tm = text_material_management().get_tutor_available_texts(tutor_key,page)       
				enter = True
			elif subject_name:
				subject_instance = subject_management().find_name(subject_name)
				list_tm = text_material_management().get_subject_available_texts(subject_instance.key(),page)
				enter = True

			if enter == True:
				for index in range(len(list_tm)):                    
					tm = list_tm[index]
					text_instance = text_material_management().get_text(tm)
					tinfo = {}        
					tinfo['id'] = tm.key().id()          
					if tm.available == True:
						tinfo['able'] = 'Deshabilitar'
					else:
						tinfo['able'] = 'Habilitar'
					tinfo['tutor'] = (tutor_management().get_tutor(tm.tutor.key().id())).first
					tinfo['topic'] = (topic_management().get_topic(tm.topic.key().id())).name                    
					tinfo['content'] = text_instance.content                    
					tinfo['number_views'] = text_instance.number_views
					list_texts.append(tinfo)                      

				html = ''
				for i in range(len(list_texts)):                
					html +='\
					\
					<a class="textr" href="view_text?text_material_id='+str(list_texts[i]['id'])+'" alt="'+str(list_texts[i]['topic'])+'">\
					<div class="text" id="'+str(list_texts[i]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="views">\
					<i class="fa fa-eye"></i> '+str(list_texts[i]['number_views'])+'\
					</div>\
					</div>\
					<div class="about">\
					<h2>'+str(list_texts[i]['topic'])+'</h2>\
					<small>por '+str(list_texts[i]['tutor'])+'</small>\
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
