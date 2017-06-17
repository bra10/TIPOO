'''
Created on Dec 6, 2013

@author: Raul
'''
from google.appengine.ext import db


class CognitiveTest(db.Model):
    cognitive_test_id=db.StringProperty(required=True)
    test_xml=db.BlobProperty()
    
