'''
Created on Dec 10, 2013

@author: Raul
'''
from google.appengine.ext import blobstore, db

from Model.Unused.TeachingMaterial import TeachingMaterial as material


class TextMaterial():
    '''
    Text Material
    '''
    text=blobstore.BlobReferenceProperty()

    def get_all(self):
        query_str = "SELECT * FROM TextMaterial LIMIT 10"
        return db.GqlQuery(query_str).get()