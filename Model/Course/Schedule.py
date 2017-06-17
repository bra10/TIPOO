'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course
from Model.Evaluation.Exam import Exam
from Model.Course import DirectedExercise


class Schedule(db.Model):
    created = db.DateTimeProperty()
    activity_name = db.StringProperty()
    deadline = db.DateTimeProperty()
    weighing = db.FloatProperty()
    course = db.ReferenceProperty(Course)
    exam = db.ReferenceProperty(Exam)
    #exercise db.ReferenceProperty()
    directed_exercise = db.ReferenceProperty(DirectedExercise)
    activity_type = db.StringProperty(choices=('Exámen','Ejercicio','Ejercicio Particular'))
    description = db.StringProperty()
