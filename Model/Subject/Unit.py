
from google.appengine.ext import db
from Model.User.Tutor import Tutor as tutor
from Model.Subject.Subject import Subject as subject

class Unit(db.Model):
	name = db.StringProperty()
	tutor = db.ReferenceProperty(tutor)
	subject = db.ReferenceProperty(subject)
	number = db.IntegerProperty()

	def get_all_units(self , tutor):
		query_str = "SELECT * FROM Unit WHERE tutor=:tutor ORDER BY number ASC"
		return db.GqlQuery(query_str,tutor=tutor).fetch(limit=1000)

	def get_all_units_of_subject(self,subject):
		query_str = "SELECT * FROM Unit WHERE subject=:subject ORDER BY number ASC"
		return db.GqlQuery(query_str,subject=subject).fetch(limit=1000)
	
	def get_unit(self,unit_id):
		return Unit.get_by_id(unit_id)

	def get_unit_by_name(self,name):
		query_str = "SELECT * FROM Unit WHERE name=:name ORDER BY number ASC"
		return db.GqlQuery(query_str,name=name).fetch(limit=5)