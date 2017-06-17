'''
Created on Mar 16, 2015
Last Modified on Mar 16, 2015
@author: Adriel
'''
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import urllib
class DownloadMaterial(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):              
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)                
        self.send_blob(blob_info, save_as=False)
        