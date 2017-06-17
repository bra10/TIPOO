'''
Created on Dec 10, 2013

@author: Raul
'''
from Controller.Lib import LearningStyle  as material_type
from Controller.Lib.MaterialLevel import MaterialLevel as material_level
from Model.User import Student  as student
from Model.Unused.TeachingMaterial import TeachingMaterial as teaching_material
from Model.User.Tutor import Tutor as tutor
from Tutor import TutorCredential as tutor_credential


#from Model.Subject import Subject as subject
class Student(object):
    '''
    Student
    '''
    
    def __init__(self, user_id):
        '''
        Constructor
        '''
        self.user=student().get_user(user_id)
        
        
        
    def get_tutors(self):
        list_tutors=self.user.tutors()
        tutor_credentials=[]
        for tutor in list_tutors:
            tutor_credentials.append(tutor_credential(tutor.key(),tutor.first,tutor.picture,tutor.last,tutor.email))
        return tutor_credentials
        
    def remove_tutor(self, tutor_id):
        if tutor_id in self.user.tutors:
            self.user.tutors.remove(tutor_id)
            return True 
        else:
            return False
    
    def add_tutor(self,tutor_id):
        tutors=tutor()
        if tutors.find_email(tutor_id) and not (tutor_id in self.user.tutors):
            self.user.tutors.append(tutor_id)
            return True
        else: 
            return False
        
    
    def get_material_type(self,subject,level, type_material):
        material=teaching_material()
        return material.find(subject, level, type_material)
        
    
    def get_material_level(self,subject,level):
        material=teaching_material()
        materials=[]
        for type_material in material_type.styles:
            materials.append(material.find(subject, level, type_material))
        return materials
    
    def get_material_subject(self,subject):
        material=teaching_material()
        materials=[]
        for level in material_level.levels:
            for type_material in material_type.styles:
                materials.append(material.find(subject, level, type_material))
        return materials
        
        
    def get_subjects(self):
        #return subject().all()
        return 1
    
    def get_advance(self):
        return self.user.progress
    
    def set_advance(self, advance):
        if advance>0 and advance<=100:
            self.user.progress=advance
            self.user.put()
            return True
        else:
            return False
        
    def set_learning_style(self, style):
        if style in material_type.styles:
            self.user.material_type=style
            self.user.put()
            return True
        return False

    def get_credential(self):
        '''
        get Credential
        '''
        credential=StudentCredential(self.user.key(),self.user.first,self.user.picture)
        return credential


    
        
class StudentCredential():
    '''
    Student Credential
    '''
    def __init__(self,student_id,name,picture):
        self.student_id=student_id
        self.name=name
        self.picture=picture

    '''
    sirve para mostrar la infomracion del user al frontend
    '''