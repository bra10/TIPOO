'''
Created on Nov 17, 2014
@author: Adriel
'''
from datetime import datetime
class ElapsedTime():

	def elapsed_time(self,start,finish):
		'''
		Function that calculate the take it time to answer the whole test
		Args:
			start (Time): start of the test
			finish (Time): finish of the test
		Returns:
			The elapsed time that take to solve the test
		'''
		string_start=str(start)
		string_finish=str(finish)
		string_time_format_start = string_start[11:19]
		string_time_format_finish = string_finish[11:19]
		ti = datetime.strptime(string_time_format_start,'%H:%M:%S')
		tf = datetime.strptime(string_time_format_finish,'%H:%M:%S')
		difference = tf - ti
		seconds = int( difference.seconds % 60 )
		minutes = int( (difference.seconds / 60) % 60 )
		hours = int( difference.seconds / 60 / 60 )
		date = str(datetime.utcnow())
		year = str(date[0:4])
		month = str(date[5:7])
		day = str(date[8:10])
		args = '{0} {1} {2} {3} {4} {5}'.format(year,month,day,hours,minutes,seconds)
		return datetime.strptime(args,"%Y %m %d %H %M %S")