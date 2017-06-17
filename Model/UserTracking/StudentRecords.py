'''
Last Modified on Mar 20, 2015
@author: Thomas, Raul
'''
from google.appengine.ext import db

from Model.Intelligent.IntelligentType import IntelligentType
from Model.User.Student import Student
from Model.Subject.Subject import Subject
from Model.UserTracking.Action import Action


class StudentRecords(db.Model):
	'''
	StudentRecords
	'''
	recorded = db.DateTimeProperty(auto_now_add=True)
	action = db.ReferenceProperty(Action)
	user = db.ReferenceProperty(Student)
	subject = db.ReferenceProperty(Subject)
	intelligent_type = db.ReferenceProperty(IntelligentType)

	def get_average_student_records(self,startDate,endDate,user):
		#query = "SELECT * FROM StudentRecords WHERE user=:user AND recorded > DATE("+str(startDate)+") AND recorded < DATE("+str(endDate)+")"
		#query = "SELECT * FROM StudentRecords WHERE user=:user AND recorded > DATE('"+str(startDate)+"') AND recorded < DATE('"+str(endDate)+"')"
		query = "SELECT * FROM StudentRecords WHERE user=:user AND recorded > DATETIME('"+str(startDate)+" 00:00:00') AND recorded < DATETIME('"+str(endDate)+" 23:59:59')"		
		average = db.GqlQuery(query,user = user)	
		return average.count()
		#return 2
	'''
	def get_average_StudentRecords_all_events(self,student_key,date_start,date_end):
		list_count = []
		list_event = get_all_events()
		for e in list_event:
			list_count.append(get_average_student_records(student_key,date_start,date_end,e))
		return list_count_event

	def get_average_StudentRecords_single_event(self,student_key,date_start,date_end,event):
		query = "SELECT * FROM StudentRecords WHERE user =: studentKey AND recorded > DATE(date_start) AND recorded < DATE(date_end) AND event =: Event"
		db.GqlQuery(query,studentKey = student_key, dateStart = date_start, dateEnd = date_end, Event = event).get()
		return len(db.GqlQuery(query).get())
	'''
	
	def get_student_records_date_lapse(self,startDate,endDate,user):
		query = "SELECT * FROM StudentRecords WHERE user=:user AND recorded > DATETIME('"+str(startDate)+" 00:00:00') AND recorded < DATETIME('"+str(endDate)+" 23:59:59')"
		return db.GqlQuery(query,user = user).fetch(limit = 1000)

	def get_all_student_records(self,user):
		query = "SELECT * FROM StudentRecords WHERE user=:user"
		return db.GqlQuery(query,user = user).fetch(limit = 1000)
		
	def get_average_student_records_site_url(self,user,startDate = None,endDate = None):
		list_site_url = Action().get_all_sites()
		if startDate and endDate:
			list_s_r = self.get_student_records_date_lapse(startDate,endDate,user)
		else:
			list_s_r = self.get_all_student_records(user)
		list_event_site = []
		list_events = []
		list_event_count = []
		for site_url in list_site_url:
			c=0
			for e in list_events:
				for st in list_s_r:
					st_a = action_model().get_action(st.user.key().id())
					if st_a.event == e:
						c += 1
				list_event_count.append(c)
			list_event_site.append(list_event_count)
		return list_event_site
		
	def deleteall(self):
		studentrecords = StudentRecords.all()
		for sr in studentrecords:
			sr.delete()