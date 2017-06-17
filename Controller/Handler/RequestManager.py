'''
Created on Dec 6, 2013
Last modified Nov 4, 2014
@author: Raul, Tristian, Adriel
'''

import webapp2
from webapp2_extras import sessions
import settings
from Controller.Lib.UserType import UserType

from Controller.Management.SecurityManagement import \
    SecurityManagement as security_management


class RequestManagement(webapp2.RedirectHandler):
    """Request Manager
    The request manager handles the user session and protects routes that require authetication
    by redirecting to the signin route.
    """

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def get_user_type(self):
        """
        Ask if the type of user have a session, if not then the user is a visitor,
        else then it's a user of the system and returns this type of session
        """
        if 'user' not in self.session:
            self.user_type = UserType.visitor
        else:        
            self.user_type = self.session['user']
        return self.user_type
    
    def get_user_id(self):
        return self.session.get('user-id')

    def dispatch(self):
        """
        This retrieve the session stored by the cookie, evaluate the type of user
        if this one it's a visitor and want to access any static route of the app,
        this one it's redirect to the signin module to restrict the security
        And if it's a valid user then the session it's save

        Still need to secure when an valid user it's already on the app and want
        to access by a static router
        """
        self.session_store = sessions.get_store(request=self.request)        
        if self.get_user_type() == UserType.visitor and not self.request.path in settings.STATIC_ROUTES:
            self.redirect('/')
            return
        elif not self.request.path in settings.STATIC_ROUTES:
            self.redirect('/home')
            return
            
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
