from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'url_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'url_app/post_detail.html', {'post': post})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	posts = Post.objects.all().order_by('title')
	return render(request, 'url_app/post_list.html', {'posts': posts})

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