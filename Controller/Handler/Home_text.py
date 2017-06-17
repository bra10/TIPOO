'''
Created on Jun 13, 21015
Last Modified on Jul 12, 2015
@author: Raul, Adriel, Omar
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

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('home_text_template.tmp')
content_template = JINJA_ENVIRONMENT.get_template('content_home_template.tmp')
jade_text = '''
ul.pagination
	li
		a(href="#") 1
		a(href="#") 2
		a(href="#") 3
		a(href="#") 4
		a(href="#") 5
''' 

class Home_text(request_management):
    '''
    Home
    '''
    list_list_vm = 0
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:       

			self.redirect('/explorer')        	
			return 1

        elif user == user_type.tutor:                          
			page = 1            
			list_list_texts = []
			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
			index = 0
			list_list_text_info = []            
			countent = {}
			list_counter = []   
			list_content = []         
			self.list_list_vm = text_material_management().get_list_text_material_of_subject(tutor_key,page)                        
			for index in range(len(self.list_list_vm)):
				list_texts = []
				counter = {}                
				content = {}
				if self.list_list_vm[index]:					
					counter['subject'] = (subject_management().get_subject(self.list_list_vm[index][0].subject.key().id())).name                    
					counter['total-text'] = text_material_management().get_all_texts_material(tutor_key,self.list_list_vm[index][0].subject.key(),page)
					for subindex in range(len(self.list_list_vm[index])):                    
						vm = self.list_list_vm[index][subindex]
						text_instance = text_material_management().get_text(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Deshabilitar'
						else:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = text_instance.content                    
						vinfo['number_views'] = text_instance.number_views
						list_texts.append(vinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_text_info.append(list_texts)

			self.response.write(self.list_list_vm)

			html = ''
			for i in range(len(list_list_text_info)):                
				html += '<div class="block" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['subject'])+'</span><small> ('+str(len(list_counter[i]['total-text']))+' texts)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'
				for j in range(len(list_list_text_info[i])):
					html +='\
					\
					<a class="videor" href="view_text?text_material_id='+str(list_list_text_info[i][j]['id'])+'" alt="'+str(list_list_text_info[i][j]['topic'])+'">\
					<div class="video" id="'+str(list_list_text_info[i][j]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="remove" id="'+str(list_list_text_info[i][j]['id'])+'">'+str(list_list_text_info[i][j]['able'])+'</div>\
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
				if len(list_counter[i]['total-text']) > 6:
					html += '<div class="more"><i class="fa fa-refresh"></i> Mostrar mas</div>'                    
				html += '</div>'                    
			template_values={
				"user":"Tutor",
				"header_welcome":"",
				"header_tutor":"",
				"list_list_texts": list_list_text_info,                
				"counter":list_counter,
				"html":html,
				"tutor_name": tutor_instance.first
			}  
			                  
			self.response.write(template.render(template_values))  
			return 2                    
        else:                        
            
            template_values = {

            }
            self.response.write(template.render(template_values))                        
            return 3
           
    def post(self):

        user = self.get_user_type()                    
        if user == user_type.visitor:                    
                
            return 0
        elif user == user_type.student:                   
            return 1
        elif user == user_type.tutor:
			available = self.request.get('available',None)  
			page = self.request.get('vm_page',None)
			if available:
				vm_id = self.request.get('vm_id',None)                
				text_material_management().make_available(int(vm_id))                        
			if page:                
				page = int(page)
				list_list_texts = []
				tutor_id = self.session['user-id']
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				subject_instance = subject_management().find_name(self.request.get('vm_subject'))
				index = 0
				list_texts = []
				list_vm = text_material_management().get_list_text_material(tutor_key,subject_instance.key(),page)                
				if list_vm:
					for index in range(len(list_vm)):                    
						vm = list_vm[index]
						text_instance = text_material_management().get_text(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Deshabilitar'
						else:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = text_instance.content                    
						vinfo['number_views'] = text_instance.number_views
						list_texts.append(vinfo)                
						html = ""

						for v in list_texts:
							html += '\
							\
							<a class="textr" href="view_text?text_material_id='+str(v['id'])+'" alt="'+str(v['topic'])+'">\
							<div class="text" id="'+str(v['id'])+'">\
							<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
							<div class="remove" id="'+str(v['id'])+'">'+str(v['able'])+'</div>\
							<div class="views">\
							<i class="fa fa-eye"></i> '+str(v['number_views'])+'\
							</div>\
							</div>\
							<div class="about">\
							<h2>'+str(v['topic'])+'</h2>\
							<small>por '+str(v['tutor'])+'</small>\
							</div>\
							</div>\
							</a>  '
				self.response.write(html)
			return 2
        else:
            return 3

class Home_textContent(request_management):
    def post(self):
        pass