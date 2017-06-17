'''
Last Modified on Feb 10, 2015
@author: Raul
'''
from google.appengine.ext import db

from Model.Intelligent import IntelligentModel


class FuzzyEngine(db.Model):
    '''
    Fuzzy Engine Control
    '''
    intelligent_model = db.ReferenceProperty(IntelligentModel)
    description = db.StringProperty()
    version = db.StringProperty()
    inputs = db.StringProperty()
    outputs = db.StringProperty()