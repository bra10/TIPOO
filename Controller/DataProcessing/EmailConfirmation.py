'''
Created on Mar 1, 2015
@author: Adriel
'''
from google.appengine.api import mail
class EmailConfirmation():

	def send_mail(self, user_email):
		message = mail.EmailMessage(sender="<tipoo.project@gmail.com>", subject="Tu cuenta ha sido aprobada")		
		key = str(user_email) + '_UABC'		
		message.to = "<{0}>".format(user_email)
		message.body = """Tu cuenta ha sido creada exitosamente en el sistema TIPOO, solo da click en el enlace de abajo y listo
		    http://tipoodev.appspot.com/confirm_registration?key={0}""".format(key)
		message.send()            
		