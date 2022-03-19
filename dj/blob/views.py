from django.shortcuts import render
from blob.models import Post # <==

# мой проект/blob/views.py
def post_list(request):
    posts = Post.objects.all()# <==
    return render(request,
                  'blob/post_list.html',
                  {'posteki':posts})# <==
