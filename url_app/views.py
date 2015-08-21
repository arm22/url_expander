from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from ratelimit.decorators import ratelimit
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from url_app.models import Post
from url_app.serializers import PostSerializer

@login_required(login_url='accounts/login/')
@ratelimit(key='ip', rate='10/m', block=True)
def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'url_app/post_list.html', {'posts': posts})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/accounts/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'url_app/post_detail.html', {'post': post})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/accounts/login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.all().order_by('title')
    return render(request, 'url_app/post_list.html', {'posts': posts})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/accounts/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            post.save()
            return redirect('url_app.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'url_app/post_edit.html', {'form': form})

@api_view(['GET', 'POST']) 
def api_list(request, format=None):     
    """     List all users, or create a new user.     """     
    if request.method == 'GET':         
        posts = Post.objects.all()         
        serializer = PostSerializer(posts, many=True)         
        return Response(serializer.data)
    elif request.method == 'POST':         
        serializer = PostSerializer(data=request.data)         
        if serializer.is_valid():             
            serializer.save()             
            return Response(serializer.data, status=status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)