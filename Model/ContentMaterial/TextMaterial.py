'''
Last modified on Mar 17, 2015
@author: Omar
'''

from google.appengine.ext import db
from google.appengine.ext import blobstore
from Model.User.Tutor import Tutor as Tutor
from Model.ContentMaterial.Text import Text as Text
from Model.Subject.Topic import Topic as Topic
from Model.Subject.Unit import Unit as Unit
from Model.Subject.Subject import Subject as Subject

class TextMaterial(db.Model):

	level = db.IntegerProperty()
	unit = db.IntegerProperty()
	topic = db.ReferenceProperty(Topic) 
	subject = db.ReferenceProperty(Subject)
	tags = db.StringListProperty()
	tutor = db.ReferenceProperty(Tutor)		
	text = db.ReferenceProperty(Text)
	available = db.BooleanProperty()
	uploaded_time = db.DateTimeProperty(auto_now=True)

	def get_text_material(self,text_material_id):
		return TextMaterial.get_by_id(text_material_id)

	def get_all_text_material(self,tutor,subject,page):
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND subject=:subject ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,tutor=tutor,subject=subject).fetch(limit=1000)

	def get_list_text_material(self,tutor,subject,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND subject=:subject ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor,subject=subject).fetch(limit=limit,offset=offset)
	##Pureba
	def get_unit_texts_available(self,tutor,subject,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND subject=:subject AND unit=:unit AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor,subject=subject,unit=unit).fetch(limit=limit,offset=offset)	
	
	def get_all_unit_available_texts(self,unit):
		query_str = "SELECT * FROM TextMaterial WHERE unit=:unit AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,unit=unit).fetch(limit=1000)
	
	def get_unit_available_texts(self,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE unit=:unit AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,unit=unit).fetch(limit=limit,offset=offset)
	'''
	def get_unit_available_texts(self,tutor,subject,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND subject=:subject AND unit=:unit AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor,subject=subject,unit=unit).fetch(limit=limit,offset=offset)		
	'''
	def get_all_tutor_available_texts(self,tutor,page):
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,tutor=tutor).fetch(limit=1000)

	def get_tutor_available_texts(self,tutor,page):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE tutor=:tutor AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,tutor=tutor).fetch(limit=limit,offset=offset)

	def get_all_subject_available_texts(self,subject,page):
		query_str = "SELECT * FROM TextMaterial WHERE subject=:subject AND available = true ORDER BY uploaded_time DESC"
		return db.GqlQuery(query_str,subject=subject).fetch(limit=1000)

	def get_subject_available_texts(self,subject,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE subject=:subject AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,subject=subject).fetch(limit=limit,offset=offset)
	'''
	##Esta es la prueba2
	def get_unit_available_texts(self,subject,unit,page,limit):
		offset = limit * page
		query_str = "SELECT * FROM TextMaterial WHERE subject=:subject AND unit=:unit AND available = true ORDER BY uploaded_time DESC"	
		return db.GqlQuery(query_str,subject=subject,unit=unit).fetch(limit=limit,offset=offset)
	'''
