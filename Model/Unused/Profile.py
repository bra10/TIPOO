'''
Created on Dec 10, 2013

@author: Raul
'''
from google.appengine.ext import db


class Profile(db.Model):
    '''
    Profile
    '''
    user=db.StringProperty(required=True)
    visual_acuity=db.StringProperty()
    