'''
Last Modified on Nov 15, 2014
@author: Tristian, Adriel
'''
from google.appengine.ext import db
import json
from Model.User.User import User
from Model.User.Tutor import Tutor as Tutor
from Model.User.Student import Student as Student
from Model.Subject.Subject import Subject as Subject
from Model.Subject.Unit import Unit as Unit
from google.appengine.ext import blobstore


class Question(db.Model):
    """Represents a question that is used in an exam"""

    text = db.StringProperty()
    answers = db.StringListProperty()
    correct_answers = db.ListProperty(int)
    value = db.IntegerProperty()
    image = blobstore.BlobReferenceProperty()
    def to_json(self):
        """Obtain a JSON representation of the model"""

        return json.dumps({
            'text': self.text,
            'answers': [a for a in self.answers],
            'weight': self.weight
        })
    def find_question(self,question_id):
        return Question.get_by_id(question_id)

    def get_all(self):
        query_str = "SELECT * FROM Question"
        return db.GqlQuery(query_str).fetch(limit=5)

class Answer(db.Model):
    """This class represents an answer to a given question"""
    question = db.ReferenceProperty(Question)
    value = db.ListProperty(int)


class Exam(db.Model):
    """This class defines an exam, it's questions, creator and category. It
    is not used to contain the answers of a particular exam that has been applied"""
    user = db.ReferenceProperty(Tutor)
    name = db.StringProperty()

    '''
    Store the index of level and learning_type, to make it easier the retrieve of the value
    in that index
    '''
    level = db.IntegerProperty()
    
    learning_type = db.IntegerProperty()
    unit = db.ReferenceProperty(Unit)
    topic = db.StringProperty()
    available = db.BooleanProperty()
    subject = db.ReferenceProperty(Subject)

    questions = db.ListProperty(db.Key)
    knwoledge_fraction = db.FloatProperty()

    def grade_test(self, test, as_fraction=False):
        '''
        Tristian knwoledge_fraction ??? explicacion!!!!        
        '''
        """Obtain the grade of the test.

            :param test A test model that will contain the answers of an exam
            :param as_fraction A flag indicating if the grade will be 
            expressed as a fractional number from 0.0 to 1.0
        """
        score = 0
        for no, answer in enumerate(test.answers):
            q = self.questions[no]
            if answer in q.correct_answers:
                score += 1

        # Handle the case when as_fraction is True
        # and the score was 0
        if score == 0:
            return 0

        return score if not as_fraction else score/float(len(self.questions))
    def find_exam(self, exam_id):                
        return Exam.get_by_id(exam_id)

    def remove(self, exam_id):
        exam = self.find_exam(exam_id)
        return db.delete(exam)

    def find_unit(self,unit):
        query_str = "SELECT * FROM Exam WHERE unit=:unit"
        return db.GqlQuery(query_str,unit=unit).get()
    
    def get_all_exams(self,tutor_id):
        query_str = "SELECT * FROM Exam WHERE user=:tutor ORDER BY Exam.name"
        return db.GqlQuery(query_str,tutor=tutor_id).fetch(limit=50)

    def get_exams_by_subject(self,subject):
        query_str = "SELECT * FROM Exam WHERE subject=:subject"
        return db.GqlQuery(query_str,subject=subject).fetch(limit=1000)

    def get_exams_by_unit(self,unit):
        query_str = "SELECT * FROM Exam WHERE unit=:unit"
        return db.GqlQuery(query_str,unit=unit).fetch(limit=1000)
    '''AND subject=:subject'''
    def get_all_exam_material(self,tutor,subject):
        query_str = "SELECT * FROM Exam WHERE user =:tutor AND subject=:subject ORDER BY uploaded_time DESC"
        return db.GqlQuery(query_str,tutor=tutor,subject=subject).fetch(limit=1000)
    
    def get_all_unit_available_exams(self,unit):
		query_str = "SELECT * FROM Exam WHERE unit=:unit AND available = true"
		return db.GqlQuery(query_str,unit=unit).fetch(limit=1000)
    
    def get_unit_available_exams(self,unit,page,limit):
        offset = limit * page
        query_str = "SELECT * FROM Exam WHERE unit=:unit AND available = true"
        return db.GqlQuery(query_str,unit=unit).fetch(limit=limit,offset=offset)
    
    def get_list_exam_material(self,tutor,subject,page,limit):
        offset = limit * page
        query_str = "SELECT * FROM Exam WHERE user=:tutor ORDER BY uploaded_time DESC"  
        return db.GqlQuery(query_str,tutor=tutor).fetch(limit=limit,offset=offset)
    



    def to_json(self):
        """Obtain a JSON representation of the model"""

        return json.dumps({
            'user': self.user,
            'name': self.name,
            'questions': [ q.to_json() for q in self.questions ],
        })

class Test(db.Model):
    """This class defines a test. A test represents a current evaluation of an exam,
    it is designed to holde the answers of an exam"""

    # time duration
    date = db.DateProperty()
    completion_time = db.TimeProperty()
    congitive_state = db.FloatProperty()
    applicant = db.ReferenceProperty(Student)
    exam = db.ReferenceProperty(Exam)
    #question_answers = db.ListProperty(db.Key)
    question_answers = db.ListProperty(int)
    approved = db.BooleanProperty()

    def find_test(self,test_id):        
        return Test.get_by_id(test_id)
    
    def find_same_exam(self,exam_id,student_id):        
        query_str = "SELECT * FROM Test WHERE __key__ = KEY('Exam',{0}) AND __key__ = KEY('Student',{1})".format(exam_id,student_id)
        return db.GqlQuery(query_str).get()
