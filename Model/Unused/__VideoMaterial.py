'''
Created on Dec 10, 2013

@author: Raul
'''
from google.appengine.ext import db

from Model.Unused.TeachingMaterial import TeachingMaterial as material


class VideoMaterial():
    '''
    Video Material
    '''
    url=db.URLProperty(required=True)