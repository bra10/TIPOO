'''
Created on Feb 22, 2015
Last modified on Mar 17, 2015
@author: Adriel
'''
from datetime import datetime
from google.appengine.ext import db
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Model.ContentMaterial.VideoMaterial import VideoMaterial as video_material_model
from Controller.Management.MaterialManagement.VideoManagement import VideoManagement as video_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.UserManagement import TutorManagement as tutor_management

class VideoMaterialManagement():
	'''
	VideoMaterialManagement
	'''
	def add(self,video_key,level,unit,subject,topic,tags,tutor):	
		
		video_material_instance = video_material_model()
		video_material_instance.level = level
		video_material_instance.unit = unit
		video_material_instance.subject = subject
		video_material_instance.topic = topic
		video_material_instance.tags = tags
		video_material_instance.tutor = tutor
		video_material_instance.video = video_key		
		video_material_instance.available = False
		video_material_instance.put()
		return True


	def modify(self,video_material_key, video_key,level,unit,subject,topic,tags,tutor):

		video_material_instance = self.get_video_material(video_material_key.id())
		video_material_instance.level = level
		video_material_instance.unit = unit
		video_material_instance.subject = subject
		video_material_instance.topic = topic
		video_material_instance.tags = tags
		video_material_instance.tutor = tutor
		video_material_instance.video = video_key		
		video_material_instance.available = False
		video_material_instance.put()
		return True
	
	def remove(self,video_material_key,video_key):
		db.delete(video_material_key)
		db.delete(video_key)	
		return True	

	def make_available(self,video_material_id):
		video_material_instance = self.get_video_material(video_material_id)		
		if video_material_instance.available:
			video_material_instance.available = False
		else:
			video_material_instance.available = True								
		video_material_instance.put()
		return True

	def get_number_views(self,video_material_id):
		video_material_instance = self.get_video_material(video_material_id)
		if video_material_instance:
			video_instance =  self.get_video(video_material_instance)
			return video_management().get_number_views(video_instance)
		return None

	def update_number_views(self,video_material_id):
		video_material_instance = self.get_video_material()
		if video_material_instance:
			video_instance = self.get_video(video_material_instance)
			video_management().update_number_views(video_instance)
			return True
		return False		

	def get_video_material(self,video_material_id):
		return video_material_model().get_video_material(video_material_id)

	def get_video(self,video_material_instance):				
		return video_management().get_video(video_material_instance.video.key().id())

	def get_video_content(self,video_material_id):
		video_material_instance = self.get_video_material(video_material_id)
		if video_material_instance:
			video_instance = self.get_video(video_material_instance)		
			return video_instance.content
		return None

	def get_list_video_material(self,tutor,subject,page):
		return video_material_model().get_list_video_material(tutor,subject,page,10)

	def get_list_video_material_of_subject(self,tutor,page):
		list_subject = subject_management().get_all_subjects()
		list_list_vm = []
		for s in list_subject:
			list_vm = self.get_list_video_material(tutor,s.key(),page)			
			list_list_vm.append(list_vm)
		return list_list_vm
	def get_list_video_material_of_one_subject(self,tutor,subject,page):
		s = subject_management().get_subject(subject.id())
		return self.get_list_video_material(tutor,s.key(),page)

	def get_tutor_available_videos(self,tutor_key, page):		
		return video_material_model().get_tutor_available_videos(tutor_key,page)
		
	##Prueba
	def get_list_video_material_of_one_subject_unit(self,tutor,subject,unit,page):
		s = subject_management().get_subject(subject.id())
		u = unit_management().get_unit(unit.id())
		return self.get_list_video_material_unit(tutor,s.key(),u.key(),page)
		
	def get_list_video_material_unit(self,tutor,subject,unit,page):
		return video_material_model().get_unit_videos_available(tutor,subject,unit,page,10)
	
	def get_all_unit_available_videos(self,unit_key):
		return video_material_model().get_all_unit_available_videos(unit_key)
	
	def get_unit_available_videos(self,unit_key,page):
		return video_material_model().get_unit_available_videos(unit_key,page,10)
	##
	
	def get_tutors_available_videos(self,page):		
		list_tutor = tutor_management().get_all_tutors()
		list_list_vm = []
		for t in list_tutor:			
			list_vm = video_material_model().get_tutor_available_videos(t.key(),page)
			list_list_vm.append(list_vm)
		return list_list_vm

	def get_subject_available_videos(self, subject_key, page):
		return video_material_model().get_subject_available_videos(subject_key,page)	

	def get_subjects_available_videos(self,page):
		list_subject = subject_management().get_all_subjects()
		list_list_vm = []
		for s in list_subject:			
			list_vm = video_material_model().get_subject_available_videos(s.key(),page)
			list_list_vm.append(list_vm)
		return list_list_vm	

	def get_all_videos_material(self,tutor,subject,page):
		return video_material_model().get_all_videos_material(tutor,subject,page)

	def get_all_tutor_available_videos(self,tutor,page):
		return video_material_model().get_all_tutor_available_videos(tutor,page)

	def get_all_subject_available_videos(self,subject,page):
		return video_material_model().get_all_subject_available_videos(subject,page)






