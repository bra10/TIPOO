'''
Created on Dec 10, 2013
Last Modified on Mar 20, 2015
@author: Raul, Adriel, Omar
'''
import datetime

from google.appengine.ext import db

from Model.User.Administrator import Administrator as admin_model
from Model.User.Student import Student as student_model
from Model.UserTracking.Action import Action as action_model
from Model.UserTracking.StudentRecords import StudentRecords as student_records_model




class StudentRecordsManagement():
    '''
    StudentRecords
    '''
    def add(self, student, site, event, content, information):

        student = student_model().get_user(student)
        student_record = student_records_model()
        student_record.user = student.key()

        action = action_model()
        action.user = student.key()
        action.site_url = site
        action.event = event
        action.content_url = content
        action.information = information
        action.type = 'Video'
        action_key = action.put()

        student_record.action = action_key
        student_record.put()
        return True

    #StudentRecords functions

    def get_average_student_records(self, startDate, endDate, user):
        return student_records_model().get_average_student_records(startDate, endDate, user)

    def get_student_records_date_lapse(self, startDate, endDate, user):
        return student_records_model().get_student_records_date_lapse(startDate,endDate,user)

    def get_all_student_records(self, user):
        return student_records_model().get_all_student_records(user)

    def get_average_student_records_site_url(self, user, startDate = None, endDate = None):
        return student_records_model().get_average_student_records_site_url(user, startDate, endDate)


    #action functions

    def get_all_events(self):
        return action_model().get_all_events()

    def get_all_sites(self):
        return action_model().get_all_sites()

    def get_all_content_urls(self):
        return action_model().get_all_content_urls()

    def count_events(self, event, url, user):
        return action_model().count_events(event, url, user)

    def count_events_between_dates(self, startDate, endDate, event, url, user):
        return action_model().count_events_between_dates(startDate, endDate, event, url, user)

    def count_content_urls(self, contentUrl, user):
        return action_model().count_content_urls(contentUrl, user)

    def count_content_urls_between_dates(self, startDate, endDate, contentUrl, user):
        return action_model().count_content_urls_between_dates(startDate, endDate, contentUrl, user)

