'''
Created on Dec 6, 2013
Last Modified Nov 15, 2014
@author: Raul, Tristian
'''
from google.appengine.ext import db


class User(db.Model):    
    first = db.StringProperty()
    last = db.StringProperty()
    email = db.StringProperty()
    password = db.StringProperty()
    user_type = db.StringProperty()
    picture = db.BlobProperty()
    sex = db.StringProperty()
    bday = db.DateProperty()
    activate = db.BooleanProperty()

    registered = db.DateTimeProperty(auto_now_add=True)

    def get_fullname(self):
        return self.first + " " + self.last
        
