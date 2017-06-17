'''
Last modified on Nov, 2014
@author: Raul, Tristian, Adriel, Omar
'''
from google.appengine.ext import blobstore
import webapp2

import settings
from Controller.Handler.Home import Home as home, HomeContent as home_content
from Controller.Handler.Home_text import Home_text as home_text, Home_textContent as home_text_content
from Controller.Handler.SubjectContent import SubjectContent as subject_content
from Controller.Handler.Login import Login as login
from Controller.Handler.Material.AdminText import AdminText as admin_text
from Controller.Handler.Material.Exam import Exam as exam
from Controller.Handler.Material.AdminVideo import AdminVideo as admin_video
from Controller.Handler.Material.AdminExam import AdminExam as admin_exam
from Controller.Handler.Material.ExamDirections import ExamDirections as exam_directions
from Controller.Handler.Material.EditExam import EditExam as edit_exam
from Controller.Handler.Material.DeleteExam import DeleteExam as delete_exam
from Controller.Handler.Index import Index as index
from Controller.Handler.Logout import Logout as logout
from Controller.Handler.Signin import Signin as signin
from Controller.Handler.Signup import Signup as signup
from Controller.Handler.Profile import Profile as profile
from Controller.Handler.Explorer import Explorer as explorer
from Controller.Handler.Material.DataVideo import DataVideo as data_video
from Controller.Handler.Material.UploadVideo import UploadVideo as upload_video
from Controller.Handler.Material.ViewVideo import ViewVideo as view_video
from Controller.Handler.Material.UploadExam import UploadExam as upload_exam
from Controller.Handler.Material.DataText import DataText as data_text
from Controller.Handler.Material.UploadText import UploadText as upload_text
from Controller.Handler.Material.ViewText import ViewText as view_text
from Controller.Handler.Tracker import Tracker as tracker
from Controller.Handler.Material.DownloadMaterial import DownloadMaterial as download_material
from Controller.Handler.Tutor import Tutor as tutor
#from Controller.Video_Testing.Video_Upload import VideoUpload as video_upload
#from Controller.Handler.Upload import ViewVideo as view_video2
from Controller.Handler.ConfirmRegistration import ConfirmRegistration as confirm_registration
#from Controller.Handler.Upload import DownloadBlobHandler as download_material, \
from Controller.Handler.Upload import Upload as upload, UploadHandler as upload_material, \
    UploadOptions as upload_options, UploadTest as upload_test

class deleteBlobs(webapp2.RequestHandler): 
    def get(self): 
        all_blob = blobstore.BlobInfo.all();  
        blobs=all_blob.fetch(100)
        if blobs:
            for blob in blobs:
                self.response.write("Blob %s eliminado<br>"% blob.key())
                blob.delete()
         
app = webapp2.WSGIApplication([
    ('/',index),
    ('/home',home),
    ('/home_text',home_text),
    ('/login',login),
    ('/signup',signup),
    ('/confirm_registration',confirm_registration),
    ('/upload',upload),
    ('/upload_material',upload_material),
    ('/s/([^/]+)?',download_material),
    ('/signin',signin),
    ('/logout',logout),
    ('/deleteBlob',deleteBlobs),
    ('/profile',profile),
    ('/home-content',home_content),
    ('/home-text-content',home_text_content),
    ('/upload-options',upload_options),
    ('/upload-test',upload_test),
    ('/data_video',data_video),
    ('/upload_video',upload_video),
    ('/view_video',view_video), 
    ('/data_text',data_text),
    ('/upload_text',upload_text),
    ('/view_text',view_text),    
    #('/view_video2',view_video2),
    ('/explorer',explorer),
    ('/tracker',tracker),
    ('/tutor',tutor),
    ('/admin_text',admin_text),
	('/admin_video',admin_video),
	('/admin_exam',admin_exam),
    #('/video_upload',video_upload),    
	('/subject_content',subject_content),
    ('/upload_exam',upload_exam),
    ('/exam_directions',exam_directions),
    ('/exam',exam),
    ('/edit_exam',edit_exam),
    ('/delete_exam',delete_exam),
    ], debug=settings.DEBUG, config=settings.WEBAPP2_CONFIG)


 
def main():
    app.run()
    
if __name__ == '__main__':
    main()
