'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Schedule
from Model.User import Student
from Model.Evaluation import Test
from Model.Course import DirectedExercise

class Records(db.Model):
    created = db.DateTimeProperty()
    activity = db.ReferenceProperty(Schedule)
    student = db.ReferenceProperty(Student)
    score = db.FloatProperty()
    exam = db.ReferenceProperty(Test)
    #exercise db.ReferenceProperty()
    directed_exercise = db.ReferenceProperty(DirectedExercise)