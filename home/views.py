"""
Change of Quarter Directions
In models.py, change choices to new quarter and migrate
In views.py, change all to new courses, changing categories and weights as needed
   remove all dropped grade restrictions
In index.html, change all variables and headers to new courses

New Implementations
1. Update Calendar to week calender
2. To make room, move library to right column and add drop bars to grades
"""

from django.shortcuts import render
from .models import *

from bs4 import BeautifulSoup
import requests
import datetime

def index(request):

    math118cassigments = Assignment.objects.filter(course='Math 118C')
    math118cgrades = {
        'att': [],
        'quiz': [],
        'home': [],
        'mid': [],
        'final': [],
    }

    math118cattweight = 0.1
    math118cquizweight = 0.1
    math118chomeweight = 0.3
    math118cmidweight = 0.25
    math118cfinalweight = 0.25

    for grade in math118cassigments:
        if grade.category == 'Attendence':
            math118cgrades['att'].append(grade.score/grade.total)
        elif grade.category == 'Quiz':
            math118cgrades['quiz'].append(grade.score/grade.total)
        elif grade.category == 'Homework':
            math118cgrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            math118cgrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            math118cgrades['final'].append(grade.score/grade.total)

    math118catt = sum(math118cgrades['att']) / max(len(math118cgrades['att']), 1)
    math118cquiz = sum(math118cgrades['quiz']) / max(len(math118cgrades['quiz']), 1)
    math118chome = sum(math118cgrades['home']) / max(len(math118cgrades['home']), 1)
    math118cmid = sum(math118cgrades['mid']) / max(len(math118cgrades['mid']), 1)
    math118cfinal = sum(math118cgrades['final']) / max(len(math118cgrades['final']), 1)

    math118cdivisor = 1
    if math118catt == 0:
        math118cdivisor -= math118cattweight
    if math118cquiz == 0:
        math118cdivisor -= math118cquizweight
    if math118chome == 0:
        math118cdivisor -= math118chomeweight
    if math118cmid == 0:
        math118cdivisor -= math118cmidweight
    if math118cfinal == 0:
        math118cdivisor -= math118cfinalweight
    if math118cdivisor == 0:
        math118cdivisor = 1

    math118c = round((math118catt*math118cattweight + math118cquiz*math118cquizweight + math118chome*math118chomeweight + math118cmid*math118cmidweight + math118cfinal*math118cfinalweight)*100/math118cdivisor, 2)

    if math118c == 100:
        math118cletter = "A+"
    elif math118c >= 93:
        math118cletter = "A"
    elif 93 > math118c >= 90:
        math118cletter = "A-"
    elif 90 > math118c >= 87:
        math118cletter = "B+"
    elif 87 > math118c >= 83:
        math118cletter = "B"
    elif 83 > math118c >= 80:
        math118cletter = "B-"
    elif 80 > math118c >= 77:
        math118cletter = "C+"
    elif 77 > math118c >= 73:
        math118cletter = "C"
    elif 73 > math118c >= 70:
        math118cletter = "C-"
    elif 70 > math118c >= 67:
        math118cletter = "D+"
    elif 67 > math118c >= 63:
        math118cletter = "D"
    elif 63 > math118c >= 60:
        math118cletter = "D-"
    elif 60 > math118c:
        math118cletter = "F"


    math132bassigments = Assignment.objects.filter(course='Math 132B')
    math132bgrades = {
        'home': [],
        'mid': [],
        'final': [],
    }

    math132bhomeweight = 0.25
    math132bmidweight = 0.25
    math132bfinalweight = 0.5

    for grade in math132bassigments:
        if grade.category == 'Homework':
            math132bgrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            math132bgrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            math132bgrades['final'].append(grade.score/grade.total)

    math132bhome = sum(math132bgrades['home']) / max(len(math132bgrades['home']), 1)
    math132bmid = sum(math132bgrades['mid']) / max(len(math132bgrades['mid']), 1)
    math132bfinal = sum(math132bgrades['final']) / max(len(math132bgrades['final']), 1)

    math132bdivisor = 1
    if math132bhome == 0:
        math132bdivisor -= math132bhomeweight
    if math132bmid == 0:
        math132bdivisor -= math132bmidweight
    if math132bfinal == 0:
        math132bdivisor -= math132bfinalweight
    if math132bdivisor == 0:
        math132bdivisor = 1

    math132b = round((math132bhome*math132bhomeweight + math132bmid*math132bmidweight + math132bfinal*math132bfinalweight)*100/math132bdivisor, 2)

    if math132b == 100:
        math132bletter = "A+"
    elif math132b >= 93:
        math132bletter = "A"
    elif 93 > math132b >= 90:
        math132bletter = "A-"
    elif 90 > math132b >= 87:
        math132bletter = "B+"
    elif 87 > math132b >= 83:
        math132bletter = "B"
    elif 83 > math132b >= 80:
        math132bletter = "B-"
    elif 80 > math132b >= 77:
        math132bletter = "C+"
    elif 77 > math132b >= 73:
        math132bletter = "C"
    elif 73 > math132b >= 70:
        math132bletter = "C-"
    elif 70 > math132b >= 67:
        math132bletter = "D+"
    elif 67 > math132b >= 63:
        math132bletter = "D"
    elif 63 > math132b >= 60:
        math132bletter = "D-"
    elif 60 > math132b:
        math132bletter = "F"


    pstat160bassigments = Assignment.objects.filter(course='Pstat 160B')
    pstat160bgrades = {
        'home': [],
        'quiz': [],
        'mid': [],
        'final': [],
    }

    pstat160bhomeweight = 0.2
    pstat160bquizweight = 0.2
    pstat160bmidweight = 0.25
    pstat160bfinalweight = 0.35

    for grade in pstat160bassigments:
        if grade.category == 'Homework':
            pstat160bgrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Quiz': 
            pstat160bgrades['quiz'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            pstat160bgrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            pstat160bgrades['final'].append(grade.score/grade.total)

    pstat160bhome = sum(pstat160bgrades['home']) / max(len(pstat160bgrades['home']), 1)
    pstat160bquiz = sum(pstat160bgrades['quiz']) / max(len(pstat160bgrades['quiz']), 1)
    pstat160bmid = sum(pstat160bgrades['mid']) / max(len(pstat160bgrades['mid']), 1)
    pstat160bfinal = sum(pstat160bgrades['final']) / max(len(pstat160bgrades['final']), 1)

    pstat160bdivisor = 1
    if pstat160bhome == 0:
        pstat160bdivisor -= pstat160bhomeweight
    if pstat160bquiz == 0:
        pstat160bdivisor -= pstat160bquizweight
    if pstat160bmid == 0:
        pstat160bdivisor -= pstat160bmidweight
    if pstat160bfinal == 0:
        pstat160bdivisor -= pstat160bfinalweight
    if pstat160bdivisor == 0:
        pstat160bdivisor = 1

    pstat160b = round((pstat160bhome*pstat160bhomeweight + pstat160bquiz*pstat160bquizweight + pstat160bmid*pstat160bmidweight + pstat160bfinal*pstat160bfinalweight)*100/pstat160bdivisor, 2)

    if pstat160b == 100:
        pstat160bletter = "A+"
    elif pstat160b >= 93:
        pstat160bletter = "A"
    elif 93 > pstat160b >= 90:
        pstat160bletter = "A-"
    elif 90 > pstat160b >= 87:
        pstat160bletter = "B+"
    elif 87 > pstat160b >= 83:
        pstat160bletter = "B"
    elif 83 > pstat160b >= 80:
        pstat160bletter = "B-"
    elif 80 > pstat160b >= 77:
        pstat160bletter = "C+"
    elif 77 > pstat160b >= 73:
        pstat160bletter = "C"
    elif 73 > pstat160b >= 70:
        pstat160bletter = "C-"
    elif 70 > pstat160b >= 67:
        pstat160bletter = "D+"
    elif 67 > pstat160b >= 63:
        pstat160bletter = "D"
    elif 63 > pstat160b >= 60:
        pstat160bletter = "D-"
    elif 60 > pstat160b:
        pstat160bletter = "F"


    pstat274assigments = Assignment.objects.filter(course='Pstat 274')
    pstat274grades = {
        'zy': [],
        'home': [],
        'mid': [],
        'final': [],
    }

    pstat274zyweight = 0.15
    pstat274homeweight = 0.3
    pstat274midweight = 0.25
    pstat274finalweight = 0.3

    for grade in pstat274assigments:
        if grade.category == 'Zybooks':
            pstat274grades['zy'].append(grade.score/grade.total)
        elif grade.category == 'Homework':
            pstat274grades['home'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            pstat274grades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            pstat274grades['final'].append(grade.score/grade.total)

    pstat274zy = sum(pstat274grades['zy']) / max(len(pstat274grades['zy']), 1)
    pstat274home = sum(pstat274grades['home']) / max(len(pstat274grades['home']), 1)
    pstat274mid = sum(pstat274grades['mid']) / max(len(pstat274grades['mid']), 1)
    pstat274final = sum(pstat274grades['final']) / max(len(pstat274grades['final']), 1)

    pstat274divisor = 1
    if pstat274zy == 0:
        pstat274divisor -= pstat274zyweight
    if pstat274home == 0:
        pstat274divisor -= pstat274homeweight
    if pstat274mid == 0:
        pstat274divisor -= pstat274midweight
    if pstat274final == 0:
        pstat274divisor -= pstat274finalweight
    if pstat274divisor == 0:
        pstat274divisor = 1

    pstat274 = round((pstat274zy*pstat274zyweight + pstat274home*pstat274homeweight + pstat274mid*pstat274midweight + pstat274final*pstat274finalweight)*100/pstat274divisor, 2)

    if pstat274 == 100:
        pstat274letter = "A+"
    elif pstat274 >= 93:
        pstat274letter = "A"
    elif 93 > pstat274 >= 90:
        pstat274letter = "A-"
    elif 90 > pstat274 >= 87:
        pstat274letter = "B+"
    elif 87 > pstat274 >= 83:
        pstat274letter = "B"
    elif 83 > pstat274 >= 80:
        pstat274letter = "B-"
    elif 80 > pstat274 >= 77:
        pstat274letter = "C+"
    elif 77 > pstat274 >= 73:
        pstat274letter = "C"
    elif 73 > pstat274 >= 70:
        pstat274letter = "C-"
    elif 70 > pstat274 >= 67:
        pstat274letter = "D+"
    elif 67 > pstat274 >= 63:
        pstat274letter = "D"
    elif 63 > pstat274 >= 60:
        pstat274letter = "D-"
    elif 60 > pstat274:
        pstat274letter = "F"


    math147aassigments = Assignment.objects.filter(course='Math 147A')
    math147agrades = {
        'home': [],
        'quiz': [],
        'mid': [],
        'final': [],
    }

    math147ahomeweight = 0.2
    math147aquizweight = 0.2
    math147amidweight = 0.25
    math147afinalweight = 0.35

    for grade in math147aassigments:
        if grade.category == 'Homework':
            math147agrades['home'].append(grade.score/grade.total)
        elif grade.category == 'Quiz': 
            math147agrades['quiz'].append(grade.score/grade.total)
        elif grade.category == 'Midterm':
            math147agrades['mid'].append(grade.score/grade.total)
        elif grade.category == 'Final':
            math147agrades['final'].append(grade.score/grade.total)

    math147ahome = sum(math147agrades['home']) / max(len(math147agrades['home']), 1)
    math147aquiz = sum(math147agrades['quiz']) / max(len(math147agrades['quiz']), 1)
    math147amid = sum(math147agrades['mid']) / max(len(math147agrades['mid']), 1)
    math147afinal = sum(math147agrades['final']) / max(len(math147agrades['final']), 1)

    math147adivisor = 1
    if math147ahome == 0:
        math147adivisor -= math147ahomeweight
    if math147aquiz == 0:
        math147adivisor -= math147aquizweight
    if math147amid == 0:
        math147adivisor -= math147amidweight
    if math147afinal == 0:
        math147adivisor -= math147afinalweight
    if math147adivisor == 0:
        math147adivisor = 1

    math147a = round((math147ahome*math147ahomeweight + math147aquiz*math147aquizweight + math147amid*math147amidweight + math147afinal*math147afinalweight)*100/math147adivisor, 2)

    if math147a == 100:
        math147aletter = "A+"
    elif math147a >= 93:
        math147aletter = "A"
    elif 93 > math147a >= 90:
        math147aletter = "A-"
    elif 90 > math147a >= 87:
        math147aletter = "B+"
    elif 87 > math147a >= 83:
        math147aletter = "B"
    elif 83 > math147a >= 80:
        math147aletter = "B-"
    elif 80 > math147a >= 77:
        math147aletter = "C+"
    elif 77 > math147a >= 73:
        math147aletter = "C"
    elif 73 > math147a >= 70:
        math147aletter = "C-"
    elif 70 > math147a >= 67:
        math147aletter = "D+"
    elif 67 > math147a >= 63:
        math147aletter = "D"
    elif 63 > math147a >= 60:
        math147aletter = "D-"
    elif 60 > math147a:
        math147aletter = "F"



    tasks = Task.objects.all().order_by('due', 'course')
    tasknum = len(tasks)

    days = []
    for task in tasks:
        day = task.due
        if day not in days:
            days.append(day)

    titles = paperscrape()

    return render(request, "home/index.html", {
        'days': days,
        'tasks': tasks[0: min(9, tasknum)], 
        'tasknum': tasknum,
        'titles': titles,
        'math118c': 0.0 if math118c == -0.0 else math118c,
        'math118cletter': math118cletter,
        'math118catt': round(math118catt*100, 1),
        'math118cquiz': round(math118cquiz*100, 1),
        'math118chome': round(math118chome*100, 1), 
        'math118cmid': round(math118cmid*100, 1), 
        'math118cfinal': round(math118cfinal*100, 1), 
        'math132b': 0.0 if math132b == -0.0 else math132b,
        'math132bletter': math132bletter,
        'math132bhome': round(math132bhome*100, 1), 
        'math132bmid': round(math132bmid*100, 1), 
        'math132bfinal': round(math132bfinal*100, 1), 
        'pstat160b': 0.0 if pstat160b == -0.0 else pstat160b,
        'pstat160bletter': pstat160bletter,
        'pstat160bhome': round(pstat160bhome*100, 1), 
        'pstat160bquiz': round(pstat160bquiz*100, 1),
        'pstat160bmid': round(pstat160bmid*100, 1), 
        'pstat160bfinal': round(pstat160bfinal*100, 1), 
        'pstat274': 0.0 if pstat274 == -0.0 else pstat274,
        'pstat274letter': pstat274letter,
        'pstat274zy': round(pstat274zy*100, 1),
        'pstat274home': round(pstat274home*100, 1), 
        'pstat274mid': round(pstat274mid*100, 1), 
        'pstat274final': round(pstat274final*100, 1), 
        'math147a': 0.0 if math147a == -0.0 else math147a,
        'math147aletter': math147aletter,
        'math147ahome': round(math147ahome*100, 1), 
        'math147aquiz': round(math147aquiz*100, 1),
        'math147amid': round(math147amid*100, 1), 
        'math147afinal': round(math147afinal*100, 1),

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
