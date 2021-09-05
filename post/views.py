from django.template import RequestContext, loader
from post.models import Post
from post.models import Celebs
from post.models import Comment
from post.forms import PostForm, CommentForm, CelebsForm
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('http://localhost:8000/posts/')
    return render(template_name = 'add_post.html',
                  context={"form":form},
                  request = request)
 

def detail(request, post_id):
  p = Post.objects.get(pk=post_id)
  c = Comment.objects.filter(p=post).order_by('-id')
  form = CommentForm(request.POST or None)
  if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect('http://localhost:8000/posts/')
  p = Post.objects.get(pk=post_id)
  return render_to_response('detail3.html', context={'post': p, 'comment': c, 'form':form})


###@@1####2#Celebs
def celebs_index(request):
    latest_celebs_list = Celebs.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index3.html', context={"latest_celebs_list":latest_celebs_list})
      # (request, {'latest_post_list': latest_post_list}
      
def add_celebs(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('http://localhost:8000/posts/')
    return render(template_name = 'add_post.html',
                  context={"form":form},
                  request = request)
 

def celebs_detail(request, celebs_id):
  c = Celebs.objects.get(pk=celebs_id)
  form = CelebsForm(request.POST or None)
  if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect('http://localhost:8000/posts/')
  c = Celebs.objects.get(pk=celebs_id)
  return render_to_response('detail3.html', context={'celebs': c, 'form':form})


#nder_to_response('detail3.html', context={'celebs': c, 'form':form})

#

#

#

def add_comment(request, post_id):
	post = get_object_or_404(Post, id=id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():    	
			comment= form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post:detail', id=post.id)
	else:
		form = CommentForm
		context={"form":form}


       
