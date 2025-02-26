from django.shortcuts import render, get_object_or_404
from .models import Text


def textbooks(request):
    books = Text.objects.all()
    return render(request, 'textbooks/textbooks.html', {'books': books})

def render_text(request, url):
    book = get_object_or_404(Text, url=url)
    return render(request, f"textbooks/template.html", {"book": book})