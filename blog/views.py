from django.shortcuts import render
# Function render to render html
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
