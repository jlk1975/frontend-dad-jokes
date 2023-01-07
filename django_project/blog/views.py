from django.shortcuts import render
from .models import Post

# We are getting this data from our post model instead!
# posts = [
#     {
#         'author': 'Jason',
#         'title': 'Blog Post 1',
#         'content': '1st post content',
#         'date_posted': 'Jan 07, 2023'
#     },
#     {
#         'author': 'CMoney',
#         'title': 'Blog Post 2',
#         'content': '2nd post content',
#         'date_posted': 'Jan 06, 2023'
#     }
# ]

def home(request):
    # Getting the data from above JSON
    # context = {
        # 'posts': posts  #use this to use json above.
    # }
    # Getting the data from our DB
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT!'})

