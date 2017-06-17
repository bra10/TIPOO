'''
Created on Feb 22, 2015
Last modified on Mar 8, 2015
@author: Adriel
'''
from datetime import datetime
from google.appengine.ext import db
from Model.ContentMaterial.VideoMaterial import VideoMaterial as video_material_model
from Model.ContentMaterial.Video import Video as video_model

class VideoManagement():
	'''
	VideoManagement
	'''
	def add(self,video_key,description,duration,ext_format,size,number_views):
		
		video_instance = self.get_video(video_key.id())		
		video_instance.description = description
		video_instance.number_views = number_views
		video_instance.duration = duration
		video_instance.ext_format = ext_format
		video_instance.size = size		
		return video_instance.put()				

	def add_content(self,content):
		video_instance = video_model()
		video_instance.content = content
		video_instance.description = ''
		video_instance.number_views = 0
		#video_instance.duration = 
		video_instance.ext_format = ''
		video_instance.size = 0			
		return video_instance.put()

	def modify(self,video_key,description,size):
		video_instance = self.get_video(video_key.id())
		video_instance.description = description
		video_instance.size = size
		video_instance.put()		
		return True		

	def get_number_views(self,video_instance):
		return video_model().get_number_views(video_instance)

	def update_number_views(self,video_instance):
		video_instance.number_views = video_instance.number_views + 1
		video_instance.put()
		return True

	def get_video(self,video_id):
		return video_model().get_video(video_id)

	def get_video_content(self,video_instance):
		return video_model().get_video_content(video_instance.content)

	def delete(self,video_id):
		video_instance = self.get_video(video_id)
		video_instance.delete()



