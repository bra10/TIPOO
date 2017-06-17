'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from google.appengine.ext import blobstore
from Model.User import Student

class StudentFile(db.Model):
    created = db.DateTimeProperty()
    student = db.ReferenceProperty()
    file = blobstore.BlobReferenceProperty()
