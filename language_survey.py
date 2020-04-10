# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:55:19 2020

@author: Awam Victor
"""

from survey import AnonymousSurvey
#define a question and make a survey.
question = "what language did  you learn to first?"
my_survey =AnonymousSurvey(question)

#show the question and store responses
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language:")
    if response =='q':
        break
    my_survey.store_response(response)
    
#show the survey result
print("Thanks to everyine who participated in the survey")
my_survey.show_results()