'''
Created on Dec 12, 2013

@author: Raul
'''


class FuzzyRecommendation():
    '''
    Fuzzy Recommendation
    '''
    fuzzy_value={0:"Low",1:"Medium",2:"High"}
    low="Low"
    medium="Medium"
    high="High"
    
    def __init__(self,complex_value,exercises_value,study_value):
        self.complex=complex_value
        self.exercises=exercises_value
        self.study=study_value
        
        
class DefuzzyRecommendation():
    '''
    Defuzzy Recommendation
    '''
    fuzzy_value={0:"Low",1:"Medium",2:"High"}
    low="Low"
    medium="Medium"
    high="High"
    
    def __init__(self,actual_complex, exercises_amount, study_time):
        self.actual_complex=actual_complex
        self.exercises_amount=exercises_amount
        self.study_time=study_time
        
    