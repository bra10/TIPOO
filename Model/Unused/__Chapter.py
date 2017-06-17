'''
Created on Dec 10, 2013

@author: Raul
'''
from google.appengine.ext import db


class Chapter(db.Model):
    '''
    Chapters
    '''
    chapter=db.StringProperty(required=True)
    subjects=db.ListProperty(required=True)