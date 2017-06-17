from datetime import datetime
from google.appengine.ext import db

from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Unit import Unit as unit_model

class UnitManagement():
	def add(self,unit_name,subject_key,number):
		unit_instance = unit_model()
		unit_instance.name = unit_name
		unit_instance.subject = subject_key
		unit_instance.number = number
		unit_instance.put()
		return True
	
	def modify(self,unit_name,subject_key,number):
		unit_instance = unit_model().get_unit(subject_key.id())
		unit_instance.name = unit_name
		unit_instance.subject = subject_key
		unit_instance.number = number
		unit_instance.put()
		return True

	def get_unit(self,unit_id):
		return unit_model().get_unit(unit_id)

	def get_all_units_of_subject(self,subject_key):
		return unit_model().get_all_units_of_subject(subject_key)

	def get_unit_by_name(self,name):
		return unit_model().get_unit_by_name(name)





