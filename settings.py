import os
import jinja2

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname('View/'))
)

WEBAPP2_CONFIG = {
    'webapp2_extras.sessions': {
        'secret_key': 'some-secret-key',
    }
}

FORM_DATE_FORMAT = '\d{4}-\d{2}-\d{2}'
ISO_8601_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

# Static routes do not require the user to be authenticated
# but are also processed by the template engine
STATIC_ROUTES = [
    r'/',
    r'/signup',
	r'/signin',
	r'/login',
    r'/logout',
	r'/confirm_registration',
	r'/video_upload',
    r'/text_upload',
    r'/upload_exam',
    r'/upload',
    r'/upload_material',
    r'/s/([^/]+)?',
    r'/upload-options',
    r'/upload-test',    
    r'/upload_video',
    r'/upload_text',
    r'/view_video',
    r'/view_text',
    r'/home',
    r'/home_text',
    r'/extra',
    r'/data_video',
    r'/data_text',
    r'/tracker',
    r'/explorer',
    r'/tutor',
    r'/admin_text',
	r'/admin_video',
	r'/admin_exam',
	r'/subject_content',
    r'/exam_directions',
    r'/exam',
    r'/delete_exam',
    r'/edit_exam',
]

API_VERSION = 'v1'

DEBUG = False
