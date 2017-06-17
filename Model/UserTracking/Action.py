'''
Last Modified on Mar 20, 2015
@author: Thomas, Raul
'''
from google.appengine.ext import db
from Model.User.Student import Student
class Action(db.Model):
	'''
	Student's Actions
	'''
	type = db.StringProperty(choices=('Examen','Test Inteligencia', 'Ejercicio', 'Video', 'Leer'))    
	event = db.StringProperty() # event type
	information = db.StringProperty()
	site_url = db.StringProperty()
	content_url = db.StringProperty()
	recorded = db.DateTimeProperty(auto_now_add=True)
	user = db.ReferenceProperty(Student)

	def get_all_events(self):
		query = "SELECT * FROM Action"
		l = []
		list_actions = db.GqlQuery(query).fetch(limit = 1000)		
		for a in list_actions:
			l.append(a.event)
		list_aux = []
		list_aux = list(set(l))
		return list_aux		
	
	def get_all_sites(self):
		query = "SELECT * FROM Action"
		l = []
		list_actions = db.GqlQuery(query).fetch(limit = 1000)		
		for a in list_actions:
			l.append(a.site_url)
		list_aux = []
		list_aux = list(set(l))
		return list_aux	
		
	def get_all_content_urls(self):
		query = "SELECT * FROM Action"
		l = []
		list_actions = db.GqlQuery(query).fetch(limit = 1000)		
		for a in list_actions:
			l.append(a.content_url)
		list_aux = []
		list_aux = list(set(l))
		return list_aux	
	
	def count_events(self,event,url,user):
		query = "SELECT * FROM Action WHERE event=:event AND site_url=:url AND user=:user"		
		cont = db.GqlQuery(query,event=event,url=url,user=user).fetch(limit = 1000)
		return len(cont)
	
	def count_events_between_dates(self,startDate,endDate,event,site_url,user):				
		query = "SELECT * FROM Action WHERE event=:event AND site_url=:site_url  AND user=:user AND recorded > DATETIME('"+str(startDate)+" 00:00:00') AND recorded < DATETIME('"+str(endDate)+" 23:59:59')"
		cont = db.GqlQuery(query,event=event,site_url=site_url,user=user).fetch(limit = 1000)		
		return len(cont)
		
	def count_content_urls(self,content_url,user):
		query = "SELECT * FROM Action WHERE content_url=:content_url AND user=:user"
		cont = db.GqlQuery(query,content_url=content_url,user=user).fetch(limit = 1000)
		return len(cont)
		
	def count_content_urls_between_dates(self,startDate,endDate,content_url,user):		
		query = "SELECT * FROM Action WHERE content_url=:content_url  AND user=:user AND recorded > DATETIME('"+str(startDate)+" 00:00:00') AND recorded < DATETIME('"+str(endDate)+" 23:59:59')"
		cont = db.GqlQuery(query,content_url=content_url,user=user).fetch(limit = 1000)
		return len(cont)

	def deleteall(self):
		action = Action.all()
		for a in action:
			a.delete()

	