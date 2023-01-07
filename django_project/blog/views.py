from django.shortcuts import render

posts = [
    {
        'author': 'Jason',
        'title': 'Blog Post 1',
        'content': '1st post content',
        'date_posted': 'Jan 07, 2023'
    },
    {
        'author': 'CMoney',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'Jan 06, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

