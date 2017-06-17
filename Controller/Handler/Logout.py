'''
Created on 22/01/2014
Last Modified on Nov 13, 2014
@author: Raul, Adriel
'''
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Handler.UserSession import UserSession as user_session
#from tipoo.Lib.UserType import UserType as user_type



class Logout(request_management):
    '''
    Home
    '''
    def get(self):
        '''
        user_id=self.get_user_id()
        self.response.write(user_id)
        self.response.write('<br>')
        '''
        user_session().close(self.session)
        '''
        #self.response.write(logout)
        #if str(user_id) == str(logout):
        #for s in self.session.keys():
        #    self.session[s]=None
            #self.response.write(self.session[s])
            #self.response.write('<br/>')
        #self.session['user']=None
        #self.session['user-id']=None
        '''
        self.redirect('/')
        