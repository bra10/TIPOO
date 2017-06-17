'''
Last Modified on Feb 17, 2015
@author: Raul
'''
from google.appengine.ext import db


class University(db.Model):
    '''
    University
    '''
    registered = db.TimeProperty(auto_now_add=True)
    name = db.StringProperty()
    location = db.GeoPtProperty()
    contact_phone_number = db.PhoneNumberProperty()
    contact_name = db.StringProperty()
    contact_appointment = db.StringProperty()
    contact_email = db.EmailProperty();
    description = db.StringProperty();
    #datos unicos de universidad
