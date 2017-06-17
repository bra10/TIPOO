import os
import time
import json
import jinja2
import copy

from math import ceil as ceil
from google.appengine.ext import db
from Model.ContentMaterial.TextMaterial import TextMaterial as text_material
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.EvaluationManagement import ExamManagement as exam_management

from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.MaterialManagement.TextMaterialManagement import TextMaterialManagement as text_material_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management


JINJA_ENVIRONMENT = jinja2.Environment(
                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
admin_exam_template = JINJA_ENVIRONMENT.get_template('admin_exam_template.tmp')

class AdminExam(request_management):
	list_list_em = []
	def post(self):
		user = self.get_user_type()                    
		if user == user_type.visitor:                    
			return 0
		elif user == user_type.student:                   
			return 1
		elif user == user_type.tutor:
			available = self.request.get('available',None)  
			delete = self.request.get('delete',None)
			page = self.request.get('vm_page',None)
			if available:
				em_id = self.request.get('em_id',None)                
				exam_management().make_available(int(em_id))                        
			if delete:
				em_id = self.request.get('em_id',None)
				exam = exam_management().find_exam(int(em_id))
				exam_management().remove(exam.key())
				sleep(0.1)
			return 2
		else:
			return 3
		
	def get(self):
		user = self.get_user_type()               
		if user == user_type.visitor:                    
			self.redirect('/')
			return 0
		elif user == user_type.student:
			tutor_id = self.session['user-id']
			student_instance = student_management().get_student(int(self.session['user-id']))
			tutor = tutor_management().get_all_tutors()[0]
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
			page = self.request.get('page',0)   
			unit_id = self.request.get('unit_id',None)
			if unit_id:
				unit_id = int(unit_id)
			else:
				##id de 1era unidad
				unit_id = 5750892489867264
			page = self.request.get('page',0)
			try:
				int(page)
				page = int(page)-1
			except ValueError:
				page = 0
			if page < 1:
				page = 0
			index = 0
			unit = unit_management().get_unit(unit_id)
			list_list_text_info = []            
			countent = {}
			list_counter = []   
			list_content = []  
			list_all_exams = exam_management().get_all_unit_available_exams(unit.key())  
			list_em = exam_management().get_unit_available_exams(unit.key(),page)
			
			list_exams = []
			if list_em:				
				#total_text = text_material_management().get_all_texts_material(tutor_key,self.list_list_tm[index][0].subject.key(),page)
				for index in range(len(list_em)):
					em = list_em[index]
					exam_instance = exam_management().find_exam(em.key().id())
					einfo = {}        
					einfo['id'] = em.key().id()          
					einfo['able'] = em.available
					einfo['tutor'] = (tutor_management().get_tutor(em.user.key().id())).first
					einfo['topic'] = em.topic                    
					#einfo['content'] = exam_instance.content                    
					#einfo['number_views'] = exam_instance.number_views
					#einfo['description'] = 	exam_instance.description					
					list_exams.append(einfo)
					index = index + 1
			html = ''
			pages = int(ceil(len(list_all_exams)/10.))
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			template_values={
				"user":"Student",
				"header_welcome":"",
				"header_tutor":"",
                "total_pages":len(list_page),
                "current_page":(page+1),
				"list_exams": list_exams,                
				"pages":list_page,
				#Agregado
				"unit_id":unit_id,
				"Titulo":"Gestion de Textos",
				"counter":list_counter,
				"html":html,
				"subject":subject.name,
				"student_name": student_instance.first
			} 	
			self.response.write(admin_exam_template.render(template_values))
			
			return 1		

		elif user == user_type.tutor:
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
			listi = tutor_management().find_all_exams_subject(tutor_key,subject.key())      
			#self.list_list_tm = text_material_management().get_list_text_material_of_subject(tutor_key,page)
			list_em = tutor_management().find_all_exams(tutor_key,subject.key(),page)
			
			c=0                        
			list_exams = []
			total_em = 0
			if list_em:				
				#total_text = text_material_management().get_all_texts_material(tutor_key,self.list_list_tm[index][0].subject.key(),page)
				for index in range(len(list_em)):
					em = list_em[index]
					exam_instance = exam_management().find_exam(em.key().id())
					einfo = {}        
					einfo['id'] = em.key().id()          
					einfo['able'] = em.available
					einfo['tutor'] = (tutor_management().get_tutor(em.user.key().id())).first
					einfo['topic'] = em.topic                    
					'''
					einfo['content'] = exam_instance.content                    
					einfo['number_views'] = exam_instance.number_views
					einfo['description'] = 	exam_instance.description					
					'''
					list_exams.append(einfo)
					index = index + 1								
			html = ''
			
			pages = int(ceil(len(listi)/10.))
			if pages < 1:
				pages = 1
			list_page = [None] * pages              
			template_values={
				"user":"Tutor",
				"header_welcome":"",
				"header_tutor":"",
                "total_pages":len(list_page),
                "current_page":(page+1),
				"list_exams": list_exams,
				"subject":subject.name,
				"pages":list_page,
				"Titulo":"Gestion de Examenes",                
				"counter":list_counter,
				"tutor_name": tutor_instance.first
			}  
            
			self.response.write(admin_exam_template.render(template_values))
			
			return 2                                      
		else: 
			return 3