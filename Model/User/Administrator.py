'''
Last Modified on Jan 26, 2015
author: Raul, Adriel
'''
from google.appengine.ext import db

from User import User as User


class Administrator(User):
    description=db.StringProperty()

    def set_or_get(self,email):
        query_str="SELECT * FROM Administrator WHERE email =:email"
        user=db.GqlQuery(query_str,email=email).get()
        if user is None:
            user=Administrator()
            user.put()
        return user
    
    def get_user(self,user_id):
        #key=db.Key.from_path('Student',user_id)
        #return Student.get(key)
        return Administrator.get_by_id(user_id)

    def delete(self,user_id):

        administrator_instance = self.get_user(user_id)
        if administrator_instance:
            db.delete(administrator_instance)
            return True
        return False







     
    def find_name(self,name):
        query_str="SELECT * FROM Administrator WHERE first=\'"+name+"\'"
        return db.GqlQuery(query_str).get()
     
    def find_last(self,last):
        query_str="SELECT * FROM Administrator WHERE last=\'"+last+"\'"
        return db.GqlQuery(query_str).get()
     
    def find_email(self,email):
        query_str="SELECT * FROM Administrator WHERE email=\'"+email+"\'"
        return db.GqlQuery(query_str).get()
    ''' 
    def set_or_get(self,email):
        query_str="Select * From Administrator WHERE email = \'"+email+"\'"
        user=db.GqlQuery(query_str).get()
        if user is None:
            user=Administrator()
            user.put()
        return user
    
    def get_user(self,user_id):
        key=db.Key.from_path('Administrator',user_id)
        return Administrator.get(key)

    def delete(self,user_id):
        query_str="SELECT * FROM Administrator WHERE email=\'"+user_id+"\'"
        user=db.GqlQuery(query_str)
        db.delete(user)
        db.put()
    '''