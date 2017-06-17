'''
Created on Dec 6, 2013

@author: Raul
'''
from google.appengine.ext import db
'''
from Model.User.User import User
from Model.User.Tutor import Tutor as Tutor
from Model.User.Student import Student as Student
from Model.Unused.Learning import LearningType as LearningType, Subject as Subject

from google.appengine.ext import blobstore, db
'''

class TeachingMaterial(db.Model):
    pass
    '''
    #material_id=db.StringProperty(required=True)
    level=db.StringProperty()
    subject=db.StringProperty()
    type=db.StringProperty()
    #location=db.URLProperty()
    datetime=db.DateTimeProperty(auto_now_add=True)
    chapter=db.StringProperty()
    text=blobstore.BlobReferenceProperty()
    url=db.StringProperty()
    tutor=db.StringProperty()#tutor id
    '''
    '''
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