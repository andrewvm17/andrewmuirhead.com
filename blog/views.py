from django.shortcuts import render

posts = [
    {
        'author': 'Andrew M',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 12, 2022'
    },
    {
        'author': 'Sean Limon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 13, 2022'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

