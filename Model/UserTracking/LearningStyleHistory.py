'''
Last Modified on Feb 10, 2015
@author: Raul
'''
from google.appengine.ext import db

from Model.Intelligent import IntelligentTest
from Model.User import Student
from Model.Intelligent import IntelligentType


class LearningStyleHistory(db.Model):
    '''
    Learning style history
    '''
    recorded = db.DateTimeProperty(auto_now_add=True)
    user = db.ReferenceProperty(Student)
    intelligent_type = db.ReferenceProperty(IntelligentType)
    realized_test = db.ReferenceProperty(IntelligentTest)