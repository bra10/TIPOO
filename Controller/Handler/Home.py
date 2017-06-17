'''
Created on Dec 12, 2013
Last Modified on Jul 17, 2015
@author: Raul, Adriel, Omar
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
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('newhome_template.tmp')
content_template = JINJA_ENVIRONMENT.get_template('content_home_template.tmp')

class Home(request_management):
	'''
	Home
	'''
	def get(self):
		user = self.get_user_type()                    
		unit_exists = unit_management().get_unit_by_name("Introduccion a Java")
		'''
		subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
		unit_management().add('Unidad 1 Introduccion a Java',subject.key(),1)
		unit_management().add('Unidad 2  Variables, objetos y clases',subject.key(),2)
		unit_management().add('Unidad 3 Codificacion de imágenes',subject.key(),3)
		unit_management().add('Unidad 4 Ambiente de ejecución y arreglos',subject.key(),4)
		unit_management().add('Unidad 5 Tópicos avanzados de java',subject.key(),5)
		unit_management().add('Unidad 6 Manejo de Excepciones',subject.key(),6)
		unit_management().add('Unidad 7 Recursos Escenciales de Java',subject.key(),7)
		unit_management().add('Unidad 8 Hilos',subject.key(),8)
		unit_management().add('Unidad 9 Manipulación de medios',subject.key(),9)
		'''
		if user == user_type.visitor:                    
			self.redirect('/')
			return 0
		elif user == user_type.student:       
			tutors = tutor_management().get_all_tutors()
			student = student_management().get_student(int(self.session['user-id']))
			list = []

			for t in tutors:
				if t.key() not in student.tutors_list:
					student.tutors_list.append(t)					
			template_values = {
				"total":len(student.tutors_list),
				"user": "Student",
			}
			self.response.write(template.render(template_values))
			return 1

		elif user == user_type.tutor:     
			'''                     
			page = 1            
			list_list_videos = []
			tutor_id = self.session['user-id']
			tutor_key = tutor_management().get_tutor(tutor_id).key()
			tutor_instance = tutor_management().get_tutor(tutor_id)
			index = 0
			list_list_video_info = []            
			countent = {}
			list_counter = []   
			list_content = []         
			list_list_vm = video_material_management().get_list_video_material_of_subject(tutor_key,page)                        
			for index in range(len(list_list_vm)):
				list_videos = []
				counter = {}                
				content = {}
				if list_list_vm[index]:					
					counter['subject'] = (subject_management().get_subject(list_list_vm[index][0].subject.key().id())).name                    
					counter['total-video'] = video_material_management().get_all_videos_material(tutor_key,list_list_vm[index][0].subject.key(),page)
					for subindex in range(len(list_list_vm[index])):                    
						vm = list_list_vm[index][subindex]
						video_instance = video_material_management().get_video(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Deshabilitar'
						else:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = video_instance.content                    
						vinfo['number_views'] = video_instance.number_views
						list_videos.append(vinfo)
					index = index + 1
					counter['index'] = index
					list_counter.append(copy.deepcopy(counter))
					list_list_video_info.append(list_videos)
					self.response.write(list_list_vm[0])

			html = ''
			for i in range(len(list_list_video_info)):                
				html += '<div class="block" id="num'+str(i)+'"><div class="head"><i class="fa fa-book"></i> <span class="subject">'+str(list_counter[i]['subject'])+'</span><small> ('+str(len(list_counter[i]['total-video']))+' Videos)</small><span class="toggle"><i class="fa fa-caret-square-o-up"></i> Ocultar Materia</span></div>'
				for j in range(len(list_list_video_info[i])):
					html +='\
					\
					<a class="videor" href="view_video?video_material_id='+str(list_list_video_info[i][j]['id'])+'" alt="'+str(list_list_video_info[i][j]['topic'])+'">\
					<div class="video" id="'+str(list_list_video_info[i][j]['id'])+'">\
					<div class="bimg" style="background:url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS67YRkacb2A7x0mniuG1SUXllu22UOKOGYfJwARDWeZl8SyZQpfg);background-size:cover;background-position:center;">\
					<div class="remove" id="'+str(list_list_video_info[i][j]['id'])+'">'+str(list_list_video_info[i][j]['able'])+'</div>\
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
				#if len(list_counter[i]['total-video']) > 6:
					#html += '<div class="more"><i class="fa fa-refresh"></i> Mostrar mas</div>'                    
				html += '</div>' 

				pages =  len(list_counter[i]['total-video'])/6
				if pages < 1:
					pages = 1
				html += '\
				<nav> \
					<ul class="pagination">'
				for p in range(1, pages+1):
					html += '<li><a href="#">' + str(p) + '</a></li>'
				html += '\
				</ul>\
					</nav\>'
			'''
			template_values={					
				"user":"Tutor",
				"header_welcome":"",
				"header_tutor":"",				
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
				video_material_management().make_available(int(vm_id))                        
			if page:                
				page = int(page)
				list_list_videos = []
				tutor_id = self.session['user-id']
				tutor_key = tutor_management().get_tutor(tutor_id).key()
				subject_instance = subject_management().find_name(self.request.get('vm_subject'))
				index = 0
				list_videos = []
				list_vm = video_material_management().get_list_video_material(tutor_key,subject_instance.key(),page)                
				if list_vm:
					for index in range(len(list_vm)):                    
						vm = list_vm[index]
						video_instance = video_material_management().get_video(vm)
						vinfo = {}        
						vinfo['id'] = vm.key().id()          
						if vm.available == True:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Deshabilitar'
						else:
							vinfo['able'] = '<i class="fa fa-pencil-square-o"></i> Habilitar'
						vinfo['tutor'] = (tutor_management().get_tutor(vm.tutor.key().id())).first
						vinfo['topic'] = (topic_management().get_topic(vm.topic.key().id())).name                    
						vinfo['content'] = video_instance.content                    
						vinfo['number_views'] = video_instance.number_views
						list_videos.append(vinfo)                
						html = ""

						for v in list_videos:
							html += '\
							\
							<a class="videor" href="view_video?video_material_id='+str(v['id'])+'" alt="'+str(v['topic'])+'">\
							<div class="video" id="'+str(v['id'])+'">\
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

class HomeContent(request_management):
	def post(self):
		pass	