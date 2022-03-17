from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def blogs(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/blogs.html', context)

def postdetail(request, pk): 
    post = Post.objects.get(pk = pk)
    context = {
        "post": post,
        "title": "Blog"
    }


    return render(request, "blog/blog_post.html", context)
