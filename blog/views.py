from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('publish_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
    return render(request,'blog/signup.html',{})

def inbox(request):
    return render(request,'blog/inbox.html',{})

def login(request):
    return render(request,'blog/login.html',{})
