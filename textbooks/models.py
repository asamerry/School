from django.db import models


TYPES = {("Book", "Book"), ("Paper", "Paper"), ("Lecture Notes", "Lecture Notes")}

class Keyword(models.Model):
    name = models.CharField(max_length=99, unique=True)

    def __str__(self):
        return f"{self.name}"

class Text(models.Model):
    type = models.CharField(max_length=20, choices=TYPES)
    title = models.CharField(max_length=499)
    author = models.CharField(max_length=199)
    url = models.CharField(max_length=199)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return f"{self.title}; {self.author}"
