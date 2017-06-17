#
# from Controller.Handler.RequestManager import RequestManagement as request_management
#
# import httplib
# import argparse
# import os
# import random
# import sys
# import time
# from lib.python_gflags import gflags
#
# from lib.httplib2 import httplib2
# from lib.google_api_python_client.apiclient.discovery import build
# from lib.google_api_python_client.apiclient.errors import HttpError
# from lib.google_api_python_client.apiclient.http import MediaFileUpload
# from lib.google_api_python_client.oauth2client.client import flow_from_clientsecrets
# from lib.google_api_python_client.oauth2client.file import Storage
# from lib.google_api_python_client.oauth2client.tools import run_flow
# from lib.google_api_python_client.oauth2client import tools
#
# httplib2.RETRIES = 1
# MAX_RETRIES = 10
# RETRIABLE_EXCEPTIONS=(httplib2.HttpLib2Error, IOError, httplib.NotConnected,
# 		httplib.IncompleteRead, httplib.ImproperConnectionState,
# 		httplib.CannotSendRequest, httplib.CannotSendHeader,
# 		httplib.ResponseNotReady, httplib.BadStatusLine)
#
# RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
# #DIR = os.path.dirname('Controller/')
# #DIR = ""
# #CLIENT_SECRETS_FILE = DIR+"client_secrets.json"
# CLIENT_SECRETS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),"client_secrets.json"))
#
# YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
#
# MISSING_CLIENTS_SECRETS_MESSAGE = """
# WARNING: Please configure OAuth 2.0
#
# To make this sample run you will need to populate the client_secrets.json file
# found at:
#
#    %s
#
# with information from the Developers Console
# https://console.developers.google.com/
#
# For more information about the client_secrets.json file format, please visit:
# https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
# """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                    CLIENT_SECRETS_FILE))
#
# VALID_PRIVACY_STATUSES = ("public","private","unlisted")
#
# def get_authenticated_service(args,debug):
# 	#os.path.dirname('/')
# 	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
# 			scope=YOUTUBE_UPLOAD_SCOPE,
# 			message=MISSING_CLIENTS_SECRETS_MESSAGE)
# 	if flow:
# 		auth_uri = flow.step1_get_authorize_url()
# 		debug.response.write(auth_uri)
# 	else:
# 		debug.response.write('da')
# 	#parser = argparse.ArgumentParser(parents=[tools.argparser])
# 	#debug.response.write(parser)
# 	#flags = parser.parse_args()
#
# 	#storage = Storage("%s-oauth2.json" % sys.argv[0])
# 	storage = Storage("algo.dat")
# 	credentials = storage.get()
#
# 	'''
# 	if credentials is None or credentials.invalid:
# 		debug.response.write('????')
# 		#credentials = run_flow(flow, storage, flags,None)
# 		credentials = tools.run(flow, storage,debug)
# 	'''
# 	'''
# 	return build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,
# 			http=credentials.authorize(httplib2.Http()))
# 	'''
# def initialize_upload(youtube,options,debug):
# 	tags = None
# 	'''
# 	if options.keywords:
# 		tags = options.keywords.split(",")
#
# 	body=dict(
# 		snippet=dict(
# 			title=options.title,
# 			description=options.description,
# 			tags=tags,
# 			categoryId=options.category
# 		),
# 		status=dict(
# 			privacyStatus = options.privacyStatus
# 		)
# 	)
#
# 	insert_request = youtube.videos().insert(
# 		part=",".join(body.keys()),
# 		body=body,
# 		media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
# 	)
# 	'''
# def resumable_upload(insert_request):
# 	response = None
# 	error = None
# 	retry = 0
# 	while response is None:
# 		try:
# 			print "Uploading file..."
# 			status, response = insert_request.next_chunk()
# 			if 'id' in response:
# 				print "Video id '%s' was successfully uploaded." % response['id']
# 			else:
# 				exit('The upload failed with a unexpected response: %s' % response)
# 		except HttpError, e:
# 			if e.resp.status in RETRIABLE_STATUS_CODES:
# 				error = "A retriable HTTP error %d ocurred:\n%s" % (e.resp.status, e.content)
# 			else:
# 				raise
#
# 		except RETRIABLE_EXCEPTIONS, e:
# 			error = "A retriable error ocurred: %s" % e
#
# 		if error is not None:
# 			print error
# 			retry += 1
# 			if retry > MAX_RETRIES:
# 				exit('No longer attempting to retry.')
#
# 			max_sleep = 2 ** retry
# 			sleep_seconds = random.random() * max_sleep
# 			print "Sleeping %f seconds and then retrying..." % sleep_seconds
# 			time.sleep(sleep_seconds)
#
#
# class Video():
#
# 	def __init__(self,title,file,detail,category,keywords,privacyStatus):
#
# 		self.title = title
# 		self.file = file
#
# class VideoUpload(request_management):
#
# 	def get(self):
# 		video = Video("SV.mp4","Silicon Valley","Video prueba","22","",VALID_PRIVACY_STATUSES[0])
#
#
# 		argparser = argparse.ArgumentParser()
# 		argparser.add_argument("--file", required=True, help="Video file to upload")
# 		argparser.add_argument("--title",help="Video title",default="Test title")
# 		argparser.add_argument("--description",help="Video description",default="Test Description")
# 		argparser.add_argument("--category",default="22",help="Numeric video category. " + "See ...")
# 		argparser.add_argument("--keywords", help="Video keywords, comma separated", default="")
# 		argparser.add_argument("--privacyStatus",choices=VALID_PRIVACY_STATUSES,
# 			default=VALID_PRIVACY_STATUSES[0],help="Video privacy status.")
#
#
# 		args = argparser.parse_args()
# 		if not os.path.exists(args.file):
# 			exit("Please specify a valid file using --file=parameter.")
#
#
# 		youtube = get_authenticated_service(video,self)
#
# 		try:
# 			initialize_upload(youtube,args)
# 		except HttpError,e:
# 			print "A HTTP error %d ocurred:\n:s" % (e.resp.status,e.content)
# 		pass
#
# 	def post(self):
# 		pass
