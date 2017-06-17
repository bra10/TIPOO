'''
Last modified on Mar 7, 2015
@author: Adriel
'''
from google.appengine.ext import db
from google.appengine.ext import blobstore

class Video(db.Model):
	
	content = blobstore.BlobReferenceProperty()	
	number_views = db.IntegerProperty()		
	description = db.StringProperty(multiline=True)	
	youtube_url = db.StringProperty()
	duration = db.DateTimeProperty()
	ext_format = db.StringProperty()
	size = db.IntegerProperty()

	def get_video(self,video_id):
		return Video.get_by_id(video_id)

	def get_all(self):
		query_str = "SELECT * FROM Video"
		return db.GqlQuery(query_str).fetch(limit=5)

	def get_video_content(self,content):
		query_str = "SELECT content FROM Video WHERE content=:content"
		return db.GqlQuery(query_str,content=content).get()

	def get_number_views(self,video_instance):
		return video_instance.number_views
		
