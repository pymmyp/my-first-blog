# Function render to render html
from django.shortcuts import render
from django.utils import timezone

# Import from views
from .models import Post

# Create your views here.

def post_list(request):
    #Django query set
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
