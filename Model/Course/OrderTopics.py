'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course
from Model.Subject import Topic

class OrderTopics(db.Model):
    order = db.IntegerProperty()
    course = db.ReferenceProperty(Course)
    topic = db.ReferenceProperty(Topic)
