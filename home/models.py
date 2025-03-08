from django.db import models

SPR24_COURSES = [('Math 117', 'Math 117'), ('Math 108A', 'Math 108A'), ('Econ 2', 'Econ 2')]
SUM24A_COURSES = [('Engl 134AA', 'Engl 134AA'), ('Writ 2', 'Writ 2')]
SUM24B_COURSES = [('Econ 10A', 'Econ 10A'), ('Pstat 120B', 'Pstat 120B')]
FALL24_COURSES = [('Math 118A', 'Math 118A'), ('Math 108B', 'Math 108B'), ('Math 113', 'Math 113'), ('Pstat 126', 'Pstat 126')]
WIN25_COURSES = [('Math 118B', 'Math 118B'), ('Math 132A', 'Math 132A'), ('Pstat 160A', 'Pstat 160A'), ('Cmpsc 16', 'Cmpsc 16')]
SPR25_COURSES = [('Math 118C', 'Math 118C'), ('Math 132B', 'Math 132B'), ('Pstat 160B', 'Pstat 160B'), ('Pstat 122, Pstat 122'), ('Math 147A', 'Math 147A')]

class Task(models.Model):
    task = models.CharField(max_length=64)
    course = models.CharField(max_length=12, choices=WIN25_COURSES)
    due = models.DateField(null=True)

    def __str__(self):
        return f"{self.task}; {self.course}"

class Assignment(models.Model):
    course = models.CharField(max_length=12, choices=WIN25_COURSES)
    category = models.CharField(max_length=24)
    score = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        if str(self.score).split('.')[1] == '0':
            newscore = str(self.score).split('.')[0]
        else:
            newscore = self.score
        if str(self.total).split('.')[1] == '0':
            newtotal = str(self.total).split('.')[0]
        else:
            newtotal = self.total
        return f"{self.course} {self.category}: {newscore}/{newtotal}"