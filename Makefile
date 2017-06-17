help:
	@echo 'Makefile for TIPOO Google App Engine application	'
	@echo '													'
	@echo 'Usage: 											'
	@echo '	clean-pyc		Remove *.pyc files				'
	@echo '	instance 		Initiate local GAE instance *.pyc files				'


clean-pyc:
	rm -f settings.pyc;
	find . -name *.pyc -exec rm {} \;

instance: clean-pyc
	dev_appserver.py .
