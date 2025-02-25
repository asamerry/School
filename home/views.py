# Change of Quarter Directions
# In models.py, change choices to new quarter and migrate
# In views.py, change all to new courses, changing categories and weights as needed
#    remove all dropped grade restrictions
# In index.html, change all variables and headers to new courses


# New Implementations
# 1. Update Calendar to week calender
# 2. To make room, move library to right column and add drop bars to grades


from django.shortcuts import render
from .models import *

from bs4 import BeautifulSoup
import requests


'''
class Class:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.categories = categories
'''

def index(request):

    math118bassigments = Assignment.objects.filter(course='Math 118B')
    math118bgrades = {
        'att': [],
        'quiz': [],
        'home': [],
        'mid': [],
        'final': [],
    }

    math118battweight = 0.1
    math118bquizweight = 0.1
    math118bhomeweight = 0.3
    math118bmidweight = 0.25
    math118bfinalweight = 0.25

    for grade in math118bassigments:
        if grade.category == 'Attendence':
            math118bgrades['att'].append(grade.score/grade.total)
        elif grade.category == 'Quiz':
            math118bgrades['quiz'].append(grade.score/grade.total)
        elif grade.category == 'Homework':
            math118bgrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            math118bgrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            math118bgrades['final'].append(grade.score/grade.total)

    math118batt = sum(math118bgrades['att']) / max(len(math118bgrades['att']), 1)
    math118bquiz = sum(math118bgrades['quiz']) / max(len(math118bgrades['quiz']), 1)
    math118bhome = sum(math118bgrades['home']) / max(len(math118bgrades['home']), 1)
    math118bmid = sum(math118bgrades['mid']) / max(len(math118bgrades['mid']), 1)
    math118bfinal = sum(math118bgrades['final']) / max(len(math118bgrades['final']), 1)

    math118bdivisor = 1
    if math118batt == 0:
        math118bdivisor -= math118battweight
    if math118bquiz == 0:
        math118bdivisor -= math118bquizweight
    if math118bhome == 0:
        math118bdivisor -= math118bhomeweight
    if math118bmid == 0:
        math118bdivisor -= math118bmidweight
    if math118bfinal == 0:
        math118bdivisor -= math118bfinalweight
    if math118bdivisor == 0:
        math118bdivisor = 1

    math118b = round((math118batt*math118battweight + math118bquiz*math118bquizweight + math118bhome*math118bhomeweight + math118bmid*math118bmidweight + math118bfinal*math118bfinalweight)*100/math118bdivisor, 2)

    if math118b == 100:
        math118bletter = "A+"
    elif math118b >= 93:
        math118bletter = "A"
    elif 93 > math118b >= 90:
        math118bletter = "A-"
    elif 90 > math118b >= 87:
        math118bletter = "B+"
    elif 87 > math118b >= 83:
        math118bletter = "B"
    elif 83 > math118b >= 80:
        math118bletter = "B-"
    elif 80 > math118b >= 77:
        math118bletter = "C+"
    elif 77 > math118b >= 73:
        math118bletter = "C"
    elif 73 > math118b >= 70:
        math118bletter = "C-"
    elif 70 > math118b >= 67:
        math118bletter = "D+"
    elif 67 > math118b >= 63:
        math118bletter = "D"
    elif 63 > math118b >= 60:
        math118bletter = "D-"
    elif 60 > math118b:
        math118bletter = "F"


    math132aassigments = Assignment.objects.filter(course='Math 132A')
    math132agrades = {
        'home': [],
        'mid': [],
        'final': [],
    }

    math132ahomeweight = 0.25
    math132amidweight = 0.25
    math132afinalweight = 0.5

    for grade in math132aassigments:
        if grade.category == 'Homework':
            math132agrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            math132agrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            math132agrades['final'].append(grade.score/grade.total)

    math132ahome = sum(math132agrades['home']) / max(len(math132agrades['home']), 1)
    math132amid = sum(math132agrades['mid']) / max(len(math132agrades['mid']), 1)
    math132afinal = sum(math132agrades['final']) / max(len(math132agrades['final']), 1)

    math132adivisor = 1
    if math132ahome == 0:
        math132adivisor -= math132ahomeweight
    if math132amid == 0:
        math132adivisor -= math132amidweight
    if math132afinal == 0:
        math132adivisor -= math132afinalweight
    if math132adivisor == 0:
        math132adivisor = 1

    math132a = round((math132ahome*math132ahomeweight + math132amid*math132amidweight + math132afinal*math132afinalweight)*100/math132adivisor, 2)

    if math132a == 100:
        math132aletter = "A+"
    elif math132a >= 93:
        math132aletter = "A"
    elif 93 > math132a >= 90:
        math132aletter = "A-"
    elif 90 > math132a >= 87:
        math132aletter = "B+"
    elif 87 > math132a >= 83:
        math132aletter = "B"
    elif 83 > math132a >= 80:
        math132aletter = "B-"
    elif 80 > math132a >= 77:
        math132aletter = "C+"
    elif 77 > math132a >= 73:
        math132aletter = "C"
    elif 73 > math132a >= 70:
        math132aletter = "C-"
    elif 70 > math132a >= 67:
        math132aletter = "D+"
    elif 67 > math132a >= 63:
        math132aletter = "D"
    elif 63 > math132a >= 60:
        math132aletter = "D-"
    elif 60 > math132a:
        math132aletter = "F"


    pstat160aassigments = Assignment.objects.filter(course='Pstat 160A')
    pstat160agrades = {
        'home': [],
        'quiz': [],
        'mid': [],
        'final': [],
    }

    pstat160ahomeweight = 0.2
    pstat160aquizweight = 0.2
    pstat160amidweight = 0.25
    pstat160afinalweight = 0.35

    for grade in pstat160aassigments:
        if grade.category == 'Homework':
            pstat160agrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Quiz': 
            pstat160agrades['quiz'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            pstat160agrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            pstat160agrades['final'].append(grade.score/grade.total)

    pstat160ahome = sum(pstat160agrades['home']) / max(len(pstat160agrades['home']), 1)
    pstat160aquiz = sum(pstat160agrades['quiz']) / max(len(pstat160agrades['quiz']), 1)
    pstat160amid = sum(pstat160agrades['mid']) / max(len(pstat160agrades['mid']), 1)
    pstat160afinal = sum(pstat160agrades['final']) / max(len(pstat160agrades['final']), 1)

    pstat160adivisor = 1
    if pstat160ahome == 0:
        pstat160adivisor -= pstat160ahomeweight
    if pstat160aquiz == 0:
        pstat160adivisor -= pstat160aquizweight
    if pstat160amid == 0:
        pstat160adivisor -= pstat160amidweight
    if pstat160afinal == 0:
        pstat160adivisor -= pstat160afinalweight
    if pstat160adivisor == 0:
        pstat160adivisor = 1

    pstat160a = round((pstat160ahome*pstat160ahomeweight + pstat160aquiz*pstat160aquizweight + pstat160amid*pstat160amidweight + pstat160afinal*pstat160afinalweight)*100/pstat160adivisor, 2)

    if pstat160a == 100:
        pstat160aletter = "A+"
    elif pstat160a >= 93:
        pstat160aletter = "A"
    elif 93 > pstat160a >= 90:
        pstat160aletter = "A-"
    elif 90 > pstat160a >= 87:
        pstat160aletter = "B+"
    elif 87 > pstat160a >= 83:
        pstat160aletter = "B"
    elif 83 > pstat160a >= 80:
        pstat160aletter = "B-"
    elif 80 > pstat160a >= 77:
        pstat160aletter = "C+"
    elif 77 > pstat160a >= 73:
        pstat160aletter = "C"
    elif 73 > pstat160a >= 70:
        pstat160aletter = "C-"
    elif 70 > pstat160a >= 67:
        pstat160aletter = "D+"
    elif 67 > pstat160a >= 63:
        pstat160aletter = "D"
    elif 63 > pstat160a >= 60:
        pstat160aletter = "D-"
    elif 60 > pstat160a:
        pstat160aletter = "F"


    cmpsc16assigments = Assignment.objects.filter(course='Cmpsc 16')
    cmpsc16grades = {
        'zy': [],
        'home': [],
        'mid': [],
        'final': [],
    }

    cmpsc16zyweight = 0.15
    cmpsc16homeweight = 0.3
    cmpsc16midweight = 0.25
    cmpsc16finalweight = 0.3

    for grade in cmpsc16assigments:
        if grade.category == 'Zybooks':
            cmpsc16grades['zy'].append(grade.score/grade.total)
        elif grade.category == 'Homework':
            cmpsc16grades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            cmpsc16grades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            cmpsc16grades['final'].append(grade.score/grade.total)

    cmpsc16zy = sum(cmpsc16grades['zy']) / max(len(cmpsc16grades['zy']), 1)
    cmpsc16home = sum(cmpsc16grades['home']) / max(len(cmpsc16grades['home']), 1)
    cmpsc16mid = sum(cmpsc16grades['mid']) / max(len(cmpsc16grades['mid']), 1)
    cmpsc16final = sum(cmpsc16grades['final']) / max(len(cmpsc16grades['final']), 1)

    cmpsc16divisor = 1
    if cmpsc16zy == 0:
        cmpsc16divisor -= cmpsc16zyweight
    if cmpsc16home == 0:
        cmpsc16divisor -= cmpsc16homeweight
    if cmpsc16mid == 0:
        cmpsc16divisor -= cmpsc16midweight
    if cmpsc16final == 0:
        cmpsc16divisor -= cmpsc16finalweight
    if cmpsc16divisor == 0:
        cmpsc16divisor = 1

    cmpsc16 = round((cmpsc16zy*cmpsc16zyweight + cmpsc16home*cmpsc16homeweight + cmpsc16mid*cmpsc16midweight + cmpsc16final*cmpsc16finalweight)*100/cmpsc16divisor, 2)

    if cmpsc16 == 100:
        cmpsc16letter = "A+"
    elif cmpsc16 >= 93:
        cmpsc16letter = "A"
    elif 93 > cmpsc16 >= 90:
        cmpsc16letter = "A-"
    elif 90 > cmpsc16 >= 87:
        cmpsc16letter = "B+"
    elif 87 > cmpsc16 >= 83:
        cmpsc16letter = "B"
    elif 83 > cmpsc16 >= 80:
        cmpsc16letter = "B-"
    elif 80 > cmpsc16 >= 77:
        cmpsc16letter = "C+"
    elif 77 > cmpsc16 >= 73:
        cmpsc16letter = "C"
    elif 73 > cmpsc16 >= 70:
        cmpsc16letter = "C-"
    elif 70 > cmpsc16 >= 67:
        cmpsc16letter = "D+"
    elif 67 > cmpsc16 >= 63:
        cmpsc16letter = "D"
    elif 63 > cmpsc16 >= 60:
        cmpsc16letter = "D-"
    elif 60 > cmpsc16:
        cmpsc16letter = "F"

    tasks = Task.objects.all().order_by('due', 'course')
    tasknum = len(tasks)

    titles = paperscrape()

    return render(request, "home/index.html", {
        'tasks': tasks[0: min(9, tasknum)], 
        'tasknum': tasknum,
        'titles': titles,
        'math118b': 0.0 if math118b == -0.0 else math118b,
        'math118bletter': math118bletter,
        'math118batt': round(math118batt*100, 1),
        'math118bquiz': round(math118bquiz*100, 1),
        'math118bhome': round(math118bhome*100, 1), 
        'math118bmid': round(math118bmid*100, 1), 
        'math118bfinal': round(math118bfinal*100, 1), 
        'math132a': 0.0 if math132a == -0.0 else math132a,
        'math132aletter': math132aletter,
        'math132ahome': round(math132ahome*100, 1), 
        'math132amid': round(math132amid*100, 1), 
        'math132afinal': round(math132afinal*100, 1), 
        'pstat160a': 0.0 if pstat160a == -0.0 else pstat160a,
        'pstat160aletter': pstat160aletter,
        'pstat160ahome': round(pstat160ahome*100, 1), 
        'pstat160aquiz': round(pstat160aquiz, 1),
        'pstat160amid': round(pstat160amid*100, 1), 
        'pstat160afinal': round(pstat160afinal*100, 1), 
        'cmpsc16': 0.0 if cmpsc16 == -0.0 else cmpsc16,
        'cmpsc16letter': cmpsc16letter,
        'cmpsc16zy': round(cmpsc16zy*100, 1),
        'cmpsc16home': round(cmpsc16home*100, 1), 
        'cmpsc16mid': round(cmpsc16mid*100, 1), 
        'cmpsc16final': round(cmpsc16final*100, 1), 
    })


def paperscrape():

    page_to_scrape = requests.get('https://www.ams.org/journals/cams/home-2024.html?active=current')
    htmldoc = BeautifulSoup(page_to_scrape.text, 'lxml')
    titles = htmldoc.findAll('dt')
    titlelist = {}

    for title in titles:
        newtitle = str(title).split('\">')[1].split('<')[0]
        titlelist[newtitle] = newtitle

    return titlelist
