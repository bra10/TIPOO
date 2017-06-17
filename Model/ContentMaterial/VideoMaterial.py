'''
Last modified on Mar 17, 2015
@author: Adriel
'''
from google.appengine.ext import db
from google.appengine.ext import blobstore
from Model.User.Tutor import Tutor as Tutor
from Model.ContentMaterial.Video import Video as Video
from Model.Subject.Topic import Topic as Topic
from Model.Subject.Subject import Subject as Subject

class VideoMaterial(db.Model):

	level = db.IntegerProperty()
	unit = db.IntegerProperty()
	topic = db.ReferenceProperty(Topic) 
	subject = db.ReferenceProperty(Subject)
	tags = db.StringListProperty()

	tutor = db.ReferenceProperty(Tutor)		
	video = db.ReferenceProperty(Video)
	available = db.BooleanProperty()
	uploaded_time = db.DateTimeProperty(auto_now=True)

	def get_video_material(self,video_material_id):
		return VideoMaterial.get_by_id(video_material_id)

	def get_all_videos_material(self,tutor,subject,page):
		query_str = "SELECT * FROM VideoMaterial WHERE tutor=:tutor AND subject=:subject ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,tutor=tutor,subject=subject).fetch(limit=100)

	def get_list_video_material(self,tutor,subject,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM VideoMaterial WHERE tutor=:tutor AND subject=:subject ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor,subject=subject).fetch(limit=limit,offset=offset)		

	def get_all_tutor_available_videos(self,tutor,page):
		query_str = "SELECT * FROM VideoMaterial WHERE tutor=:tutor AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,tutor=tutor).fetch(limit=1000)
	
	def get_unit_videos_available(self,tutor,subject,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM VideoMaterial WHERE tutor=:tutor AND subject=:subject AND unit=:unit AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor,subject=subject,unit=unit).fetch(limit=limit,offset=offset)	
	
	def get_unit_available_videos(self,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM VideoMaterial WHERE unit=:unit AND available=true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,unit=unit).fetch(limit=limit,offset=offset)
	
	def get_all_unit_available_videos(self,unit):
		query_str = "SELECT * FROM VideoMaterial WHERE unit=:unit AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,unit=unit).fetch(limit=1000)
		
	def get_tutor_available_videos(self,tutor,page):
		limit = 6
		if page == 1:
			offset = 0
		else:
			offset = 6
		query_str = "SELECT * FROM VideoMaterial WHERE tutor=:tutor AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor).fetch(limit=limit,offset=offset)

	def get_all_subject_available_videos(self,subject,page):
		query_str = "SELECT * FROM VideoMaterial WHERE subject=:subject AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,subject=subject).fetch(limit=1000)

	def get_subject_available_videos(self,subject,page):
		limit = 6
		if page == 1:
			offset = 0
		else:
			offset = 6
		query_str = "SELECT * FROM VideoMaterial WHERE subject=:subject AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,subject=subject).fetch(limit=limit,offset=offset)
