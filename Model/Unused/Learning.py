'''
Last Modified on Jan 26, 2015
@author: Adriel,Raul
'''
'''
from google.appengine.ext import db
from Model.User.User import User
from Model.User.Tutor import Tutor as Tutor
from Model.User.Student import Student as Student

class Subject(db.Model):
    """A learning subject"""
    subject = db.StringProperty()
    knowledge_fraction = db.FloatProperty()
    description = db.StringProperty();

    def find_subject(self,subject_id):    
        return Subject.get_by_id(subject_id)


class Topic(db.Model):
    """A learning Topic"""
    topic = db.StringProperty();
    description = db.StringProperty()
    subject = db.ReferenceProperty(Subject)

class LearningType(db.Model):
    name = db.StringProperty()
    description = db.StringProperty()


class Material(db.Model):
    creator = db.ReferenceProperty(Tutor)
    level = db.IntegerProperty()
    subject = db.ReferenceProperty(Subject)
    learning_type = db.ReferenceProperty(LearningType)

    def delete(self,key):
        material=db.get(key)
        db.delete(material)
        db.put()
        
    def find(self,subject,level,type_material):
        query_str="SELECT * FROM TeachingMaterial WHERE subject=\'"+subject+"\' AND level=\'"+level+"\' AND type=\'"+type_material+"\'"
        return db.GqlQuery(query_str)
    
    def find_subject(self,subject):
        query_str="SELECT * FROM TeachingMaterial WHERE subject=\'"+subject+"\'"
        return db.GqlQuery(query_str)
    
    def get_all(self):
        query_str = "SELECT * FROM TeachingMaterial LIMIT 10"
        return db.GqlQuery(query_str).get()
'''