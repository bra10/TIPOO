'''
Created on Dec 10, 2014
Last Modified on Jan 27, 2015
@author: Adriel
'''
import datetime as dt
import hashlib
class InputField():		
	'''
	Class that validate the input of a given field
	'''
	def check_date_field(self, fields):
		'''
		Function that validate if a given date it's valid
		The algorithm works as follows
		given_year - actual_year < 0
		given_month - actual_month < 0
		given_date - actual_date <= 0
		if any of this arithmetic operations are true automatically
		it's no valid because there are not negatives dates
		Args:
			fields (List): it's a list of fields to validate
		Returns:
			A dictionary of all error encounter in the validation
		'''
		errors = {}
		date = fields[7]
		month = fields[8]
		year = fields[9]

		if not date or not month or not year:
			if not date:				
				errors['d']="Introducir dia valido"

			if not month:
				errors['m']="Introducir fecha nacimiento"

			if not year:
				errors['y']="Introducir fecha nacimiento"
		else:			
			actual_day = str(dt.datetime.utcnow())					
			if int(actual_day[0:4]) - int(str(year)) < 0 and \
				int(actual_day[5:7]) - int(str(month)) < 0 and \
				int(actual_day[8:10]) - int(str(date)) <= 0:
					errors['date'] = "Fecha invalida"			
		return errors

	def check_blank_fields(self,fields):
		'''
		Function that check all the fields and valid them

		Args:
			fields (List): it's a list of fields to validate
		Returns: 
			A dictionary of all error encounter in the validation
		'''
		email = fields[0]
		email_confirm = fields[1]
		first = fields[2]
		last = fields[3]
		pwd = fields[4]
		pwd_confirm = fields[5]
		sex = fields[6]
			   
		errors = {}
		if not email:
			errors['email']="Introducir correo"

		if not email_confirm:
			errors['email_confirm']="Confirmar correo"

		if email and email_confirm:
			if not email==email_confirm:
				errors['email_confirm']="No coincide correo"        

		if not first:
			errors['first']="Introducir nombre"

		if not last:
			errors['last']="Introducir Apellido"

		if not pwd:
			errors['pwd']="Introducir contrase&ntilde;a"

		if not pwd_confirm:
			errors['pwd_confirm']="Confirmar contrase&ntilde;a"
		    
		if pwd and pwd_confirm:
			if not pwd==pwd_confirm:
				errors['pwd_confirm']="No coincide contrase&ntilde;a"

		if not sex:
			errors['sex']="Seleccionar sexo"        				
		
		return errors

	def check_signup_fields(self,fields):
		'''
		Function that validate the signup fields of the signup handler class
		Args:
			fields (List): it's all the fields of the handler class

		Returns:
			All the encountered errros in the way of validation
		'''
		errors = {}	
		blank_field = self.check_blank_fields(fields)		
		date_field = self.check_date_field(fields)
		errors.update(blank_field)
		errors.update(date_field)
		return errors

	def encrypt_password(self,pwd):
		'''
		Function that encrypt a given password in the singup handler
		The algorithm is as follows
		Args:
			pwd (String): password introduced by the user to register
		Returns:
			The password encrypted to saved in the database of the user
		'''
		salt = 'iSG716Pcu#'
		m = hashlib.md5()
		m.update(salt+pwd)
		return m.hexdigest()

