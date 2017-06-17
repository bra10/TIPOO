'''
Last Modified on Feb 10, 2015
@author: Raul
'''
from google.appengine.ext import db

from Model.Intelligent import IntelligentModel


class IntelligentTest(db.Model):
    '''
    Intelligent Test
    '''
    name = db.StringProperty()
    intelligent_model = db.ReferenceProperty(IntelligentModel)
    # should be completed, Questions, Answers, etc.