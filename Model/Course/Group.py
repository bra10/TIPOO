'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course
from Model.User import Student

class Group(db.Model):
    registered = db.DateTimeProperty(auto_now_add=True)
    student = db.ReferenceProperty(Student)
    course = db.ReferenceProperty(Course)
