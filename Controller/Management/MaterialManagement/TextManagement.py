'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel, Omar
'''
from datetime import datetime
from google.appengine.ext import db
from Model.ContentMaterial.TextMaterial import TextMaterial as text_material_model
from Model.ContentMaterial.Text import Text as text_model

class TextManagement():
	'''
	TextManagement
	'''
	def add(self,text_key,description,ext_format,size,number_views):
		
		text_instance = self.get_text(text_key.id())		
		text_instance.description = description
		text_instance.number_views = number_views
		text_instance.ext_format = ext_format
		text_instance.size = size		
		return text_instance.put()				

	def add_content(self,content):
		text_instance = text_model()
		text_instance.content = content
		text_instance.description = ''
		text_instance.number_views = 0
		text_instance.ext_format = ''
		text_instance.size = 0			
		return text_instance.put()

	def modify(self,text_key,description,size):
		text_instance = self.get_text(text_key.id())
		text_instance.description = description
		text_instance.size = size
		text_instance.put()		
		return True		

	def get_number_views(self,text_instance):
		return text_model().get_number_views(text_instance)

	def update_number_views(self,text_instance):
		text_instance.number_views = text_instance.number_views + 1
		text_instance.put()
		return True

	def get_text(self,text_id):
		return text_model().get_text(text_id)

	def get_text_content(self,text_instance):
		return text_model().get_text_content(text_instance.content)

	def delete(self,text_id):
		text_instance = self.get_text(text_id)
		text_instance.delete()



