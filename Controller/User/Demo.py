'''
Created on Dec 12, 2013

@author: Raul
'''
from Controller.Lib import LearningStyle  as learning_style


def main():
    if  "Visual" in learning_style.styles:
        print "Done"
    else:
        print "Error"
    

if __name__ == '__main__':
    main()