'''
Last Modified on Feb 17, 2015
@author: Raul
'''

from google.appengine.ext import db
from Model.Course import Course
from Model.User import Student
from Model.File import StudentFile
from Model.Course import Task

class DirectedExercise(db.Model):
    course = db.ReferenceProperty(Course)
    student = db.ReferenceProperty(Student)
    score = db.FloatProperty()
    student_file = db.ReferenceProperty(StudentFile)
    task = db.ReferenceProperty(Task)
