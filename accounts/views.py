from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

##########################

from django.template import RequestContext, loader
from post.models import Post
from post.models import Celebs
from post.models import Comment
from post.forms import PostForm, CommentForm
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
from post.models import Celebs
from post.models import Comment
from post.forms import PostForm, CommentForm, CelebsForm
#from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


def home(request):
    latest_celebs_list, latest_post_list = Celebs.objects.all().order_by('-pub_date')[:1], Post.objects.all().order_by('-pub_date')[:1], 
    return render_to_response('home.html',
    context={"latest_celebs_list": latest_celebs_list, "latest_post_list": latest_post_list})
       

      # (request, {'latest_post_list': latest_post_list}))


#class PostList(generic.ListView):
#    model = Post
#    template_name = 'index.html'

#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'detail3.html'
#	 

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:9999]
    return render_to_response('index3.html', context={"latest_post_list":latest_post_list})






def top(request):
	return render(request, 'top.html')

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('http://localhost:8000/posts/')
    return render(template_name = 'add_post.html',
                  context={"form":form},
                  request = request)



class update(UpdateView):
	model : Post
	fields = ['Your_name', 'Your_Post_title', 'Your_Post', "Image", 'Your_Appreciation_or_Critics_about_this_movie']
      ## Thats a duplicate post view##

#class delete(DeleteView):
#	model : Post
#	success_url = reverse_lazy('post:index')
	

def celebs(request):
    latest_celebs_list = Celebs.objects.all().order_by('-pub_date')[:9999]
    return render_to_response('celebs.html', context={"latest_celebs_list":latest_celebs_list})


def add_celebs(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('http://localhost:8000/celebs/')
    return render(template_name = 'add_celebs.html',
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


def add_comment(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	if request.method == 'POST':
	    form = CommentForm(request.POST)
	    if form.is_valid():
	     	comment= form.save(commit=False)
	     	comment.post = post
	     	comment.save()
	     	return redirect('http://127.0.0.1:8000/posts/', id=post.id)
	else:
  	   form = CommentForm
	context={"form":form}
	template_name = 'add-comment.html'
	return render(request, template_name, context)

      
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
             #   login(request,user)
                return redirect('http://127.0.0.1:8000/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

def view_profile(request):
	args = {'user': request.user},
	return redirect(request, 'http://127.0.0.1:8000')  


