'''
Created on Dec 12, 2013

@author: Raul
'''
import os
import urllib

#from Model.Video import Video as video_model

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import jinja2

from Controller.Lib.MaterialLevel import MaterialLevel as mat_level
from Controller.Lib.MaterialType import MaterialType as mat_type
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.TeachingMaterialManagement import \
    TeachingMaterialManagement as material_management
from Model.Unused.Plan import Plan as plan
from RequestManager import RequestManagement as request_management


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
template = JINJA_ENVIRONMENT.get_template('upload_video_template.tmp')

other_template = JINJA_ENVIRONMENT.get_template('view_video_template.tmp')


class ViewVideo(request_management,blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        pass
        '''
        video_id = self.request.get('video_id')
        video_instance = None        
        if video_id:
            
            video_instance = video_model().get_video_content(video_id)            
        
        template_values = {
            "video":video_instance,            
        }
        self.response.write(other_template.render(template_values))
        '''
class DownloadBlobHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        pass
        '''
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)        
        self.send_blob(blob_info)
        '''
class UploadHandler(request_management, blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        pass
        '''
        upload_video = self.get_uploads('file')
        blob_info = upload_video[0]        
        video_instance = video_model()
        video_instance.content = blob_info
        video_instance.title = 'Silicon Valley'
        video_key = video_instance.put()        
        #self.redirect('/?' + urllib.urlencode({'': }))
        self.redirect('/')
        '''
        '''
        video_id = video_key.id()
        video = video_model().get_by_id(video_id)
        self.response.write(str(video.content))
        self.redirect('/s/%s' %video.content.key())
        #self.redirect('/s/%s' %blob_info.key())
        '''
        '''
        errors={}
        #user=self.get_user_type()
        #if user is user_type.tutor:
        chapter=self.request.get('chapter',None)
        if not chapter:
            errors['chapter']="Unidad erroneo"
        
        subject=self.request.get('subject',None)
        if not subject:
            errors['subject']="Tema erroneo"
            
        level=self.request.get('level',None)
        if not level:
            errors['level']="Complejidad erronea"
        
        
        
        material_type=self.request.get('type',None)
        if not material_type:
            errors['type']="Tipo de material erroneo"
        else:
            if material_type=='0':#VIDEO
                url=self.request.get('url',None)
                if not url:
                    errors['url']="Tipo de material erroneo"
            elif material_type=='1':#TEXT
                data=self.request.get('pdf',None)
                if not data:
                    errors['data']="Error en archivo"  
                else:
                    upload_files = self.get_uploads('pdf')  
                    blob_info = upload_files[0]
              
            
        if len(errors)>0:
            for k,msg in errors.iteritems():
                    self.response.write("Error en {0}: {1}<br />".format(k,msg ))
        else:
            user_id=self.get_user_id()
            if(material_type=='0'):#VIDEO         
                if material_management().add_video(chapter,subject, level, material_type,url,user_id):
                    self.response.write("Hecho")
                    self.response.write('<br><a href="/">Inicio</a>')
                else:
                    self.response.write("Error")
            else:#TEXT
                if material_management().add_text(chapter,subject, level, material_type, blob_info.key(),user_id):#material_management().add_text(chapter,subject, level, material_type, blob_info.key()):
                    self.response.write("Hecho")
                    self.response.write('<br><a href="/">Inicio</a>')
                else:
                    self.response.write("Error")
        '''        
       
class Upload(request_management):
        def get(self):
            user=self.get_user_type()
            if user == user_type.visitor:
               
                return 0
            elif user == user_type.student:
                #DEBUG
                upload_url = blobstore.create_upload_url('/upload_material')
                '''
                chapters=sorted(plan().get_chapters("spanish").keys())
                db_chapters=sorted(plan().get_chapters("uni").keys())
                chapter=[(db_chapters[i],chapters[i]) for i in range(len(chapters)) ]
                
                subjects=plan().get_chapters("spanish")[chapters[0]]
                db_subjects=plan().get_chapters("uni")[db_chapters[0]]
                subject=[(db_subjects[i],subjects[i]) for i in range(len(subjects))]
                            
                material_types=mat_type().get_material_type("spanish")
                db_material_types=mat_type().get_material_type("uni")
                material_type=[(db_material_types[i],material_types[i]) for i in range(len(material_types))]
                
                video_field='Video (url):<input  type="text" name="url" />'
                text_field='Pdf(max 5Mb):<input type="file"  name="pdf"/>'
                fields=[video_field,text_field]
                field=[(db_material_types[i],fields[i]) for i in range(len(material_types))]
                
                levels=mat_level().get_material_level("spanish")
                db_levels=mat_level().get_material_level("uni")
                level=[(db_levels[i],levels[i]) for i in range(len(levels))]
                '''
                template_values={
                    'upload_url':upload_url,
                    'title':'testvideo',
                    'file':'SV.mp4',
                    'user':'Student'
                    '''
                    'chapters':chapter,
                    'subjects':subject,
                    'types':material_type,
                    'fields':field,
                    'levels':level,
                    '''
                }
                self.response.write(template.render(template_values))
                return 1
                
            else:
                self.redirect("/home")
                return 3

class UploadOptions(request_management):
    def post(self):
        chapter=self.request.get('chapter',None)
        db_subjects=plan().get_chapters("uni")[chapter] #href
        chp=plan().get_lang_chapter("spanish", chapter)
        subjects=plan().get_chapters("spanish")[chp]
        subject=[(db_subjects[i],subjects[i]) for i in range(len(subjects))]
        selector=""
        for href,name in subject:
            selector+='<option value="'+href+'">'+name+'</option>'
        self.response.write(selector)
    
class UploadTest(request_management):
    def get(self):
        user=self.get_user_type()
        if user is user_type.visitor:
            self.response.write("Usuario no identificado")
            self.response.write('<a href="/">Inicio</a>')
            return 0
        elif user is user_type.tutor:
            template = JINJA_ENVIRONMENT.get_template('test_template.tmp')
            #DEBUG
            upload_url = blobstore.create_upload_url('/upload_material')
            chapters=sorted(plan().get_chapters("spanish").keys())
            db_chapters=sorted(plan().get_chapters("uni").keys())
            chapter=[(db_chapters[i],chapters[i]) for i in range(len(chapters)) ]
            
            subjects=plan().get_chapters("spanish")[chapters[0]]
            db_subjects=plan().get_chapters("uni")[db_chapters[0]]
            subject=[(db_subjects[i],subjects[i]) for i in range(len(subjects))]
                        
            material_types=mat_type().get_material_type("spanish")
            db_material_types=mat_type().get_material_type("uni")
            material_type=[(db_material_types[i],material_types[i]) for i in range(len(material_types))]
            
            video_field='Video (url):<input  type="text" name="url" />'
            text_field='Pdf(max 5Mb):<input type="file"  name="pdf"/>'
            fields=[video_field,text_field]
            field=[(db_material_types[i],fields[i]) for i in range(len(material_types))]
            
            levels=mat_level().get_material_level("spanish")
            db_levels=mat_level().get_material_level("uni")
            level=[(db_levels[i],levels[i]) for i in range(len(levels))]
            
            template_values={
                'upload_url':upload_url,
                'chapters':chapter,
                'subjects':subject,
                'types':material_type,
                'fields':field,
                'levels':level,
            }
            self.response.write(template.render(template_values))
            return 4
        else:
            self.redirect("/home")
            return 1
    
    def post(self):
        user=self.get_user_type()
        if user is user_type.visitor:
            self.response.write("Usuario no identificado")
            self.response.write('<a href="/">Inicio</a>')
            return 0
        elif user is user_type.tutor:
            errors={}
            #user=self.get_user_type()
            #if user is user_type.tutor:
            chapter=self.request.get('chapter',None)
            if not chapter:
                errors['chapter']="Unidad erroneo"
            
            subject=self.request.get('subject',None)
            if not subject:
                errors['subject']="Tema erroneo"
            
            question=self.request.get("question",None)
            if not question:
                errors["question"]="Selecci&oacute;n incorrecta"
            
            option=self.request.get("option",None)
            if not option:
                errors["option"]="Selecci&oacute;n incorrecta"
            
                
            if len(errors)>0:
                for k,msg in errors.iteritems():
                        self.response.write("Error en {0}: {1}<br />".format(k,msg ))
            else:
                HTML='<form action="upload-test method="post">'
                for i in range(int(question)):
                    HTML+='<br>Pregunta'+str(i+1)+'<input type="text"><br>'
                    for j in range(int(option)):
                        HTML+='Opci&oacute;n '+str(j+1)+'<input type="text"><br>'
                    HTML+='Opci&oacute;n correcta<br><input type="number" name="option" min="1" max="'+str(option)+'" value="1"><br><br>'
                HTML+='<input type="submit" value="Enviar"></form>'
                self.response.write(HTML)
                
            return 3
        