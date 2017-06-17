'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course

class DirectedNotifications(db.Model):
    course = db.ReferenceProperty(Course)
    message = db.StringProperty()
    importance = db.StringProperty(choices=('Aviso','Urgente','Recomendación'))
    registered = db.DateTimeProperty(auto_now_add=True)
    expiration = db.DateTimeProperty()
