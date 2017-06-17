'''
Created on Dec 10, 2013

@author: Raul
'''
from Controller.Lib.Material import Material as material_object
from Controller.Lib.MaterialLevel import MaterialLevel as material_level
from Controller.Lib.MaterialType import MaterialType as material_type
from Model.Unused.Plan import Plan as subject_model
from Model.Unused.TeachingMaterial import TeachingMaterial as teaching_material
from Model.User.Tutor import Tutor as tutor_model


#from Model.VideoMaterial import VideoMaterial as visual_material
#from Model.TextMaterial import TextMaterial as text_material
#from Model.Subject import Subject as subject_model
class Tutor():
    '''
    Tutor
    '''

    def __init__(self, tutor_id):
        '''
        Constructor
        '''
        self.user=tutor_model().get(tutor_id)
        
    def remove_material(self,material_id,type_material):
        if material_id in self.upload_material:
            if type_material is material_type.pdf:
                teaching_material.delete(material_id)
                return True
            if type_material is material_type.video:
                teaching_material.delete(material_id)
                return True
        else:
            return False
            
    
    def get_materials(self):
        materials=self.user.uploaded_material
        list_material=[]
        for upload_material in materials:
            material=teaching_material().get(upload_material)
            if material:
                container=material_object(material.subject, material.level, material.type, upload_material)
                list_material.append(container)
            material=teaching_material().get(upload_material)
            if material:
                container=material_object(material.subject, material.level, material.type, upload_material)
                list_material.append(container)
        return list_material
        
    def upload_material(self,subject,level,type_material,data):
        if level in material_level.levels:
            if type_material in material_type.supported_materials:
                if type_material is material_type.video:
                    subjects=subject_model().get_all_chapters()
                    if subject in subjects:
                        material=teaching_material()
                        material.level=level
                        material.subject=subject                    
                        material.type=type_material
                        material.location=None
                        material.chapter=None
                        material.url=data
                        material.put()
                    else:#Subject
                        return False
                elif type_material is material_type.pdf:
                    subjects=subject_model().get_all_chapters()
                    if subject in subjects:
                        material=teaching_material()
                        material.level=level
                        material.subject=subject                    
                        material.type=type_material
                        material.location=None
                        material.chapter=None
                        material.text=data
                        material.put()
                    else:#Subject
                        return False
            else:#style
                return False
        else:#level
            return False

class TutorCredential():
    '''
    Tutor Credential
    '''
    def __init__(self,tutor_id,name,picture,description,contact):
        self.tutor_id=tutor_id
        self.name=name
        self.picture=picture
        self.description=description
        self.contact=contact
