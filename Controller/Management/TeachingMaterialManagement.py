
'''
Last Modified on Nov 15, 2014
@author: Raul, Tristian, Adriel
'''
#from tipoo.Model.TeachingMaterial import TeachingMaterial as material_model
#from tipoo.Model.Evaluation import Exam as exam_model
'''
from Model.Unused.TeachingMaterial import TeachingMaterial as material_model
from Model.Evaluation.Evaluation import Exam
from Model.Unused import  Learning as learning
from Model.User import Tutor
from google.appengine.ext import db
'''
class TeachingMaterialManagement(object):
    '''
    def __init__(self, user):
        self.user = user

    def get_learning_type(name):
        return learning.LearningType.get_by_id(db.GqlQuery("SELECT id FROM learning_type WHERE name = {}".format(name)))

    def create_text_exam(self, level, unit, chapter, subject, knowledge_fraction, questions):
        exam = Exam()
        exam.level = level
        exam.unit = unit
        exam.subject = subject 
        exam.questions = questions
        exam.learning_type = TeachingMaterialManagement.get_learning_type('text').key()
        exam.user = self.user.key()
        return exam.put()
    
    def __init__(self, user):
        self.user = user

    def get_learning_type(name):
        return LearningType.get_by_id(db.GqlQuery("SELECT id FROM learning_type WHERE name = {}".format(name)))
        
    def create_text_exam(self, level, unit, chapter, subject, knowledge_fraction, questions):
    def create_text_exam(self, user, learning_type, level, unit, subject, questions):
        exam = exam_model()
        exam.level = level
        exam.unit = unit
        exam.subject = subject 
        exam.questions = questions
        #exam.learning_type = TeachingMaterialManagement.get_learning_type('text').key()
        exam.learning_type = learning_type
        exam.user = user.key()
        return exam.put()
    classdocs

    def add_video(self,chapter,subject,level,material_type,url,user_id):

        material=material_model()
        material.chapter=chapter
        material.subject=subject
        material.level=level
        material.type=material_type
        material.url=url
        material.tutor=str(user_id)
        return material.put()
       
    def add_text(self,chapter,subject,level,material_type,data,user_id):
        material=material_model()
        material.chapter=chapter
        material.subject=subject
        material.level=level
        material.type=material_type
        material.text=data
        material.tutor=str(user_id)
        return material.put()
    
    def exist_subject_material_raw(self,subject):
        sbj=material_model().find_subject(subject)
        if sbj.get():
            return True
        else:
            return False
    
    def find_all_raw(self,subject,level,material_type):
        return material_model().find(subject, level, material_type)
    
    def find_subject_raw(self,subject):
        return material_model().find_subject(subject)
    
    def get_all(self):
        return material_model().get_all()
       
        
    '''