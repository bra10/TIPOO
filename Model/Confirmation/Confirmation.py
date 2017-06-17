'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.User import Tutor
from Model.Subject import Subject
from Model.University import University

class URL(db.Model):
    registered = db.DateTimeProperty(auto_now_add=True)
    url = db.StringProperty()
    expiration = db.DateTimeProperty()
    status = db.StringProperty(choices=('Confirmado', 'Iniciado','Vencido','Caducado'))
    user_type = db.StringProperty(choices=('SuperAdministrador','Administrador','Tutor','Student' ))
    student = db.ReferenceProperty()
    tutor = db.ReferenceProperty()
    admin = db.ReferenceProperty()
    super_admin = db.ReferenceProperty()
    ip = db.StringProperty()
    confirmation_date = db.DateTimeProperty()
    university = db.ReferenceProperty(University)


