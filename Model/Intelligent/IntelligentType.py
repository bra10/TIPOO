'''
Last Modified on Feb 10, 2015
@author: Raul
'''
from google.appengine.ext import db

from Model.Intelligent import IntelligentModel


class IntelligentType(db.Model):
    '''
    IntelligentType
    '''
    name = db.StringProperty()
    description = db.StringProperty()
    model = db.StringProperty(IntelligentModel)
