#-*- coding: utf-8 -*-
'''
To get easygui using the following
pip install --upgrade easygui
'''
from easygui import *

def ToKnowAboutMe():
    msgbox("Name             : Macha Pujitha\nDate of Birth : January 02, 1997\nEmail             : machapujitha@gmail.com\nMobile           : 8867626764\nLinkedIn        : www.linkedin.com/in/macha-pujitha")

def EducationDetails():
    msgbox("Course   %/GPA   Year of Passing                   Institution   \nCSE             79             July 2018             BNM Institute of Technology\nPCM             97            June 2014               Narayana IIT Academy\nSSLC           9.7            April 2012        Little Flower E.M. High School")

def Projects():
    msgbox("1:PICTIONARY: An interactive picture dictionary which uses NLTK database, Google’s text to speech module and the online dictionary ipicthat.com\n2.PROGRAM TO CALCULATE NUMERICAL INTEGRATION AND DIFFERENTIATION: A given expression is converted to postfix expression and is evaluated using weddle’s rule for integration")

def Achievements():
    msgbox("->HR Coordinator at a Bhumi(NGO) centre\n->IBNC Campus Ambassador\n->Department level winners in IPL Summer Competitions held in 2017 and 2018\n->Bhumi Earth Award for contribution to the Little Einsteins – Mathematics project\n->Paper presentation on Support Vector Machine\n->Statement of Completion from University of Waikato, Netherlands on Data Mining with Weka")

def objective():
    msgbox("To ensure concurrent growth of the organization and my personal career by effectively utilizing the acquired skills.")

def Skills():
    msgbox("Programming    : C, C++, Python\nPlatforms            : Windows, Linux\nTools used        :Visual Studio,PyCharm, Weka")

def options():
    msg ="What do you wanna look into"
    title = "Macha Pujitha Resume"
    choices = ["To know about me", "Objective", "Education Details", "Projects", "Achievements", "Exit", "Skills"]
    choice = choicebox(msg, title, choices)
    if(choice == "To know about me"):
        ToKnowAboutMe()
        options()
    elif(choice == "Education Details"):
        EducationDetails()
        options()
    elif(choice == "Projects"):
        Projects()
        options()
    elif(choice == "Objective"):
        objective()
        options()
    elif(choice == "Exit"):
        exit(0)
    elif(choice == "Skills"):
        Skills()
        options()
    else:
        Achievements()
        options()

def start():
    message =  "Hello! This is Macha Pujitha and here's my resume!! Hit ENTER to continue or NO To continue;)"
    yes = "Yes"
    no = "NO"
    title = ""
    if boolbox(message, title, [yes, no]):
        options()
    else:
        options()

if __name__ == '__main__':
    start()
