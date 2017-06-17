'''
Last Modified on Mar 7, 2015
@author: Raul, Adriel
'''

from google.appengine.ext import db
from Model.University.Faculty import Faculty
from Model.University.University import University

class Subject(db.Model):
    faculty = db.ReferenceProperty(Faculty)
    university = db.ReferenceProperty(University)
    name = db.StringProperty()
    knowledge_fraction = db.FloatProperty()
    description = db.StringProperty()

    def find_subject(self,subject_id):    
        return Subject.get_by_id(subject_id)

    def get_subject(self,subject_id):
        return Subject.get_by_id(subject_id)

    def get_all_subject(self):
        query_str = "SELECT * FROM Subject"
        return db.GqlQuery(query_str).fetch(limit=5)

    def find_name(self,name):
        query_str = "SELECT * FROM Subject WHERE name=:name"
        return db.GqlQuery(query_str,name=name).get()