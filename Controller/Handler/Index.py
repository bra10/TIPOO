'''
Created on Dec 12, 2013
Last modified on Nov 14, 2014
@author: Raul, Adriel, Omar
'''
import os
import jinja2

from Controller.Lib.UserType import UserType as user_type
#from RequestManager import RequestManagement as request_management
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import AdminManagement as admin_management
from Controller.Management.CollegeManagement.UnitManagement import UnitManagement as unit_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Lib.UserType import UserType as user_type
from Controller.DataProcessing.InputField import InputField as input_field
from time import sleep
#DEBUG
from Model.User import Student
import datetime
import hashlib
from Model.User import Tutor
from Model.Subject.Subject import Subject
from Model.UserTracking.StudentRecords import StudentRecords
from Model.UserTracking.Action import Action
#END DEBUG

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
index_template = JINJA_ENVIRONMENT.get_template('index_template.tmp')


class Index(request_management):
	'''
	Index
	'''
	def get(self):
		user=self.get_user_type()
		if user == user_type.visitor:  
			
			self.session['errort'] = ''							
			self.session['successt'] = ''							
			self.session['error1'] = ''	
			self.session['error2'] = ''			
			self.session['error3'] = ''								
			self.session['success'] = ''
			self.session['errort'] = ''		
			self.session['successt'] = ''
			template_values={            
			}
			
			#if not student_management().find_email("alumno@prueba.com"):
				
			
			if not tutor_management().find_email("tutor@prueba.com"):
				tutor=Tutor.Tutor()
				tutor.activate=True
				tutor.bday=datetime.datetime.strptime("1991-09-22","%Y-%m-%d").date()
				tutor.sex="male"
				tutor.password="ab1234"
				salt = 'iSG716Pcu#'
				m = hashlib.md5()
				m.update(salt+tutor.password)
				tutor.password=m.hexdigest()
				tutor.email="tutor@prueba.com"
				tutor.first="tutor"
				tutor.last="prueba"
				tutor.put()

				user=Student.Student()
				user.activate=True
				user.first="alumno"
				user.last="prueba"
				user.bday=datetime.datetime.strptime("1991-09-22","%Y-%m-%d").date()
				user.email="alumno@prueba.com"
				user.sex="male"
				user.password="ab1234"
				user.tutors_list.append(tutor.key())
				salt = 'iSG716Pcu#'
				m = hashlib.md5()
				m.update(salt+user.password)
				user.password=m.hexdigest()
				user.put()



			if not subject_management().find_name('Programacion Orientada a Objetos'):
				s1 = Subject()
				s1.name = 'Programacion Orientada a Objetos'
				s1.put()
			if not subject_management().find_name('IA'):
				s2 = Subject()
				s2.name = 'IA'
				s2.put()
			if not subject_management().find_name('Programacion Orientada a Objetos Avanzada'):
				s3 = Subject()
				s3.name = 'Programacion Orientada a Objetos Avanzada'
				s3.put()
			if not subject_management().find_name('Algoritmos'):
				s4 = Subject()
				s4.name = 'Algoritmos'
				s4.put()
			if not subject_management().find_name('Circuitos Digitales'):
				s5 = Subject()
				s5.name = 'Circuitos Digitales'
				s5.put()
			if not unit_management().get_unit_by_name('Introduccion a Java'):
				subject = subject_management().find_name('Programacion Orientada a Objetos')
				unit_management().add('Introduccion a Java',subject.key(),1)
				sleep(0.1)
				unit_management().add('Variables, objetos y clases',subject.key(),2)
				sleep(0.1)
				unit_management().add('Codificacion de imagenes',subject.key(),3)
				sleep(0.1)
				unit_management().add('Ambiente de ejecucion y arreglos',subject.key(),4)
				sleep(0.1)
				unit_management().add('Topicos avanzados de java',subject.key(),5)
				sleep(0.1)
				unit_management().add('Manejo de Excepciones',subject.key(),6)
				sleep(0.1)
				unit_management().add('Recursos Escenciales de Java',subject.key(),7)
				sleep(0.1)
				unit_management().add('Hilos',subject.key(),8)
				sleep(0.1)
				unit_management().add('Manipulacion de medios',subject.key(),9)
				sleep(0.1)
			# Action().deleteall()
			# StudentRecords().deleteall()
			self.response.write(index_template.render(template_values))
			
			return 0			
		elif user == user_type.student:
			self.redirect('/explorer')
			return 1
		else:
			self.redirect('/home')
			return 2
