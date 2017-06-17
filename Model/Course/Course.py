'''
Last Modified on Feb 17, 2015
@author: Raul
'''
from google.appengine.ext import db
from Model.User import Tutor
from Model.Subject import Subject


class Course(db.Model):
    registered = db.TimeProperty(auto_now_add=True)
    tutor = db.ReferenceProperty(Tutor)
    subject = db.ReferenceProperty(Subject)
    start_date = db.DateTimeProperty()
    end_date = db.DateTimeProperty()
    unique_code = db.StringProperty()
    description = db.StringProperty()
    objectives = db.StringProperty()
    keys = db.StringProperty()


