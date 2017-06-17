'''
Last modified on Mar 17, 2015
@author: Omar
'''

from google.appengine.ext import db
from google.appengine.ext import blobstore

class Text(db.Model):

	title = db.StringProperty()
	content = blobstore.BlobReferenceProperty() #AUN SE DESCONOCE PERO SE PROPONE
	uploaded_time = db.TimeProperty()
	number_views = db.IntegerProperty()	
	description = db.StringProperty()
	ext_format = db.StringProperty()
	size = db.IntegerProperty()

	def get_text(self, text_id):
		return Text.get_by_id(text_id)

	def get_all(self):
		query_str = "SELECT * FROM Text"
		return db.GqlQuery(query_str).fetch(limit=5)

	def get_text_content(self,content):
		query_str = "SELECT content FROM Text WHERE content=:content"
		return db.GqlQuery(query_str,content=content).get()

	def get_number_views(self, text_instance):
		return text_instance.number_views