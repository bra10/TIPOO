'''
Last Modified on Feb 10, 2015
@author: Raul
'''
from google.appengine.ext import db


class IntelligentModel(db.Model):
    '''
    Intelligent Model
    '''
    name = db.StringProperty()
    description = db.StringProperty()
    author = db.StringProperty()
    # should add others parameters of author
