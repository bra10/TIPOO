'''
Created on Dec 11, 2013

@author: Raul
'''
import sys

from ExerciseTime import ExerciseTime as exercise_time
from StudyTime import StudyTime as study_time
from TestTime import TestTime as test_time


def main():
    st=study_time()
    et=exercise_time()
    tt=test_time()
    if len(sys.argv)>=2:
        value=float(sys.argv[1])
    else:
        value=.5
    print "Study Time: {0} = {1}".format(value ,st.fuzzy(value))
    print "Exercise Time: {0} = {1} ".format(value ,et.fuzzy(value))
    print "Test Time: {0} = {1} ".format(value ,tt.fuzzy(value))

if __name__ == '__main__':
    main()