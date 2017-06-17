'''
Created on Feb 22, 2015
@author: adriel
'''
from datetime import datetime
from google.appengine.ext import db
from Model.Material.VideoMaterial import VideoMaterial as video_material_model
from Model.Material.Video import VideoMaterial as video_model

class VideoMaterialManagement():
	'''
	VideoManagement
	'''
	def add(self,title,content,description,level,unit,topic,tags,tutor):

		video_instance = Video()
		video_instance.title = title
		video_instance.content = content
		video_instance.description = description
		video_instance.number_views = 0
		video_instance.duration = 0
		video_instance.video_format = None
		video_instance.size = 0
		video_key = db.put(video_instance)

		video_material_instance = VideoManagement()
		video_material_instance.level = level
		video_material_instance.unit = unit
		video_material_instance.topic = topic
		video_material_instance.tags = tags
		video_material_instance.tutor = tutor
		video_material_instance.video = video_key		

	def modify(self):

	def make_available(self):

	def update_number_views(self):

	def get_video(self):

	def get_video_content(self):

class TextManagement():
	pass

class ImageManagement():
	pass

class FileManagement():
	pass