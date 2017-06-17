'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course

class Task(db.Model):
    created = db.DateTimeProperty()
    name = db.StringProperty()
    course = db.ReferenceProperty(Course)
    description = db.StringProperty()
    weighing = db.FloatProperty()