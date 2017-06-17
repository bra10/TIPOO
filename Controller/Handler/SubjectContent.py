from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.MaterialManagement.VideoManagement import VideoManagement as video_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Model.Subject.Subject import Subject as subject_model
from Model.Subject.Topic import Topic as topic_model
from Model.ContentMaterial.Video import Video as video_model
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from Controller.Lib.UserType import UserType as user_type
import os
import os.path
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
subject_content_template = JINJA_ENVIRONMENT.get_template('subject_content_template.tmp')

class SubjectContent(request_management):
	def post(self):
		user = self.get_user_type()
		if user == user_type.visitor:
			return 0
		elif user == user_type.student:
			
			return 1
		elif user == user_type.tutor:
			return 2
		else:
			return 3
	def get(self):

		user = self.get_user_type()
		if user == user_type.visitor:
			return 0
		elif user == user_type.student:
			type = self.request.get('type',None)
			subject = subject_management().get_subject_by_name('Programacion Orientada a Objetos')
			subject_units = unit_management().get_all_units_of_subject(subject.key())
			list_units = []
			for unit in subject_units:
				uinfo = {}
				uinfo['name'] = unit.name
				uinfo['id'] = unit.key().id()
				list_units.append(uinfo)
			template_values = {
				"list_units":list_units,
				"type":type,
				"subject":subject.name,
				"user":"Student"
			}
			self.response.write(subject_content_template.render(template_values))
			return 1
		elif user == user_type.tutor:
			
			return 2
		else:
			return 3