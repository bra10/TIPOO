'''
Last Modified on Feb 28, 2015
@author: Raul, Adriel
'''
from google.appengine.ext import db
from Model.University.University import University

class Faculty(db.Model):
    registered = db.TimeProperty(auto_now_add=True)
    name = db.StringProperty()
    university = db.ReferenceProperty(University)
