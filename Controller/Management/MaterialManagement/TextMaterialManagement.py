'''
Created on Feb 22, 2015
Last modified on Mar 17, 2015
@author: Adriel
'''
from datetime import datetime
from google.appengine.ext import db
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Model.ContentMaterial.TextMaterial import TextMaterial as text_material_model
from Controller.Management.MaterialManagement.TextManagement import TextManagement as text_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.UserManagement import TutorManagement as tutor_management

class TextMaterialManagement():
	'''
	textMaterialManagement
	'''
	def add(self,text_key,level,unit,subject,topic,tags,tutor):	
		
		text_material_instance = text_material_model()
		text_material_instance.level = level
		text_material_instance.unit = unit
		text_material_instance.subject = subject
		text_material_instance.topic = topic
		text_material_instance.tags = tags
		text_material_instance.tutor = tutor
		text_material_instance.text = text_key		
		text_material_instance.available = False
		text_material_instance.put()
		return True


	def modify(self,text_material_key, text_key,level,unit,subject,topic,tags,tutor):
		text_material_instance = self.get_text_material(text_material_key.id())
		text_material_instance.level = level
		text_material_instance.unit = unit
		text_material_instance.subject = subject
		text_material_instance.topic = topic
		text_material_instance.tags = tags
		text_material_instance.tutor = tutor
		text_material_instance.text = text_key		
		text_material_instance.available = False
		text_material_instance.put()
		return True
		
	def remove(self,text_material_key,text_key):
		db.delete(text_material_key)
		db.delete(text_key)	
		return True

	def make_available(self,text_material_id):
		text_material_instance = self.get_text_material(text_material_id)		
		if text_material_instance.available:
			text_material_instance.available = False
		else:
			text_material_instance.available = True								
		text_material_instance.put()
		return True

	def get_number_views(self,text_material_id):
		text_material_instance = self.get_text_material(text_material_id)
		if text_material_instance:
			text_instance =  self.get_text(text_material_instance)
			return text_management().get_number_views(text_instance)
		return None

	def update_number_views(self,text_material_id):
		text_material_instance = self.get_text_material()
		if text_material_instance:
			text_instance = self.get_text(text_material_instance)
			text_management().update_number_views(text_instance)
			return True
		return False		

	def get_text_material(self,text_material_id):
		return text_material_model().get_text_material(text_material_id)

	def get_text(self,text_material_instance):				
		return text_management().get_text(text_material_instance.text.key().id())

	def get_text_content(self,text_material_id):
		text_material_instance = self.get_text_material(text_material_id)
		if text_material_instance:
			text_instance = self.get_text(text_material_instance)		
			return text_instance.content
		return None

	def get_list_text_material(self,tutor,subject,page):
		return text_material_model().get_list_text_material(tutor,subject,page,10)
		
	

	def get_list_text_material_of_subject(self,tutor,page):
		list_subject = subject_management().get_all_subjects()
		list_list_tm = []
		for s in list_subject:
			list_tm = self.get_list_text_material(tutor,s.key(),page)			
			list_list_tm.append(list_tm)
		return list_list_tm
		
		
	def get_list_text_material_of_one_subject(self,tutor,subject,page):
		s = subject_management().get_subject(subject.id())
		return self.get_list_text_material(tutor,s.key(),page)
	##PRUEBA
	def get_list_text_material_of_one_subject_unit(self,tutor,subject,unit,page):
		s = subject_management().get_subject(subject.id())
		u = unit_management().get_unit(unit.id())
		return self.get_list_text_material_unit(tutor,s.key(),u.key(),page)
		
	def get_list_text_material_unit(self,tutor,subject,unit,page):
		return text_material_model().get_unit_texts_available(tutor,subject,unit,page,10)
	
	def get_all_unit_available_texts(self,unit_key):
		return text_material_model().get_all_unit_available_texts(unit_key)
	
	def get_unit_available_texts(self,unit_key,page):
		return text_material_model().get_unit_available_texts(unit_key,page,10)
	##
	'''
	##Este es el de prueba
	def get_list_text_material_of_one_subject_unit(self,tutor,unit_id,subject,page):
		s = subject_management().get_subject(subject.id())
		return self.get_unit_available_texts(tutor,s.key(),u.key(),page)
	###
	'''
	def get_tutor_available_texts(self,tutor_key, page):		
		return text_material_model().get_tutor_available_texts(tutor_key,page)

	def get_tutors_available_texts(self,page):		
		list_tutor = tutor_management().get_all_tutors()
		list_list_tm = []
		for t in list_tutor:			
			list_tm = text_material_model().get_tutor_available_texts(t.key(),page)
			list_list_tm.append(list_tm)
		return list_list_tm
	##prueba2
	'''
	def get_unit_available_texts(self,subject_key,unit_key,page):
		return text_material model().get_unit_available_texts(subject_key,unit_key,page,10)
	'''
	def get_subject_available_texts(self, subject_key, page):
		return text_material_model().get_subject_available_texts(subject_key,page,10)	

	def get_subject_available_texts(self,subject,page):#este es prueba 
		list_tm = []			
		list_tm = text_material_model().get_subject_available_texts(subject.key(),page,10)
		return list_tm	

	def get_all_texts_material(self,tutor,subject,page):
		return text_material_model().get_all_text_material(tutor,subject,page)

	def get_all_tutor_available_texts(self,tutor,page):
		return text_material_model().get_all_tutor_available_texts(tutor,page)

	def get_all_subject_available_texts(self,subject,page):
		return text_material_model().get_all_subject_available_texts(subject,page)






