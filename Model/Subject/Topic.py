'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Subject.Subject import Subject

class Topic(db.Model):
    name = db.StringProperty()
    description = db.StringProperty()
    subject = db.ReferenceProperty(Subject)

    def get_topic(self,topic_id):
        return Topic.get_by_id(topic_id)
    '''
    def get_all_subject(self):
        query_str = "SELECT * FROM Subject"
        return db.GqlQuery(query_str).fetch(limit=5)

    def find_name(self,name):
        query_str = "SELECT * FROM Subject WHERE name=:name"
        return db.GqlQuery(query_str,name=name).get()
    '''