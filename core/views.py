from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Journal, Profile, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import JournalModelForm, JournalForm
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, SignUpForm, CommentForm
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib.auth import get_user_model
from django import forms



# Create your views here.
def home(request):
    template_name = 'home.html'
    jn = Journal.objects.order_by("-timestamp")
    context = {'journal': jn}
    return render(request, template_name, context)

# EVERYTHING JOURNAL

def journal_list_view(request):

    template_name = 'index3.html'
    qs = Journal.objects.all().published()
    context = {'journal': qs}
    return render(request, template_name, context)




def journal_list_view(request):

    template_name = 'index3.html'
    jn = Journal.objects.order_by("-timestamp")
    context = {'journal': jn}
    return render(request, template_name, context)



@login_required
def journal_create_view(request):
    form = JournalModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        request_csrf_token = request.POST.get('csrfmiddlewaretoken')
        obj.user = request.user
        obj.slug = request_csrf_token[:20:-2]
        obj.save()
        return redirect('/journal/')
        form = JournalModelForm()
    template_name = 'add_post.html'
    context = {'form': form}
    return render(request, template_name, context)  


def journal_detail_view(request, slug):
    template_name = 'journal_detail.html'
    instance = get_object_or_404(Journal, slug=slug)
    #content_type = ContentType.objects.get_for_model(Journal)
    #obj_id = instance.id
    

    initial_data = {
        'content_type':instance.get_content_type,
        'object_id': instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = request.POST.get("parent_id")
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(parent__id=parent_id) 
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = Parent_qs.first()
        new_comment, created = Comment.objects.get_or_create(
                        user=request.user,
                        content_type = content_type,
                        object_id = obj_id,
                        content = content_data,
                        parent = parent_obj
            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())



    comments = instance.comments#Comment.objects.filter_by_instance(instance)
    context ={ 'journal' : instance, 'comments': comments, 'comment_form':form}
    return render(request, template_name, context)

@login_required
def comment_delete_view(request, id):
    template_name = 'delete.html'
    jn = get_object_or_404(Comment, id=id)
    if jn.user != request.user:
        return redirect('/journal/')
        #response = HttpResponse("You can't delete this. This isn't your journal notes")
        #response.status.code = 403
        #return response
    if request.method == 'POST':
        jn.delete()
        return redirect('/journal/')
    context ={ 'journal' : jn }
    return render(request, template_name, context)


@login_required
def journal_update_view(request, slug):
    jn = get_object_or_404(Journal, slug=slug)
    if jn.user != request.user:
        return redirect('/journal/')
        #response = HttpResponse("You can't Update this. This isn't your journal notes")
        #response.status.code = 403
        #return response
    form = JournalModelForm(request.POST or None,request.FILES or None, instance=jn)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your post has been Updated!')
        return redirect('/journal/')

    template_name = "add_pos.html"
    context = {"title": f"Update {jn.content}", "form": form}
    return render(request, template_name, context)




@login_required
def journal_delete_view(request, slug):
    jn = get_object_or_404(Journal, slug=slug)
    template_name = 'delete.html'
    if request.method == 'POST':
        jn.delete()
        return redirect('/journal/')
    context ={ 'journal' : jn }
    return render(request, template_name, context)




#EVERYTHING ACCOUNTS AND USERS
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Account was created successfully!")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "signup.html",
                          context={"form":form})

    form = SignUpForm 
    return render(request = request,
                  template_name = "signup.html",
                                 context={"form":form}) 
                  
 

@login_required
def profile(request):
    profile_form = Profile(request.POST)
    profile = Profile.objects.all()
    #u = User.objects.get(username=request.user.username)
    jn = Journal.objects.filter(user=request.user).order_by('-timestamp')
    #jn = Journal.objects.order_by('-timestamp')
    
    context={'profile_form' : profile_form, 'profile':profile, 'jn':jn}
	
    return HttpResponse('You have successfully login')



class ProfileDetailView(DetailView):
    queryset = User.objects.filter(is_active=True)
        
    template_name = 'core/profile.html'
    model = Journal

    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(User, username__iexact=username, is_active=True)


@login_required
def profile_create_view(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/profile/')
        form = ProfileUpdateForm()
    template_name = 'core/profile_create.html'
    context = {'form': form}
    return render(request, template_name, context)     


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if  u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()  
            messages.success(request, f'Your account has been Updated!')
            return redirect('/profile')                        
    else:    
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'core/profile_update.html', context)

def search_newco(request):
    template_name = 'core/users.html'
    context = {}
    return render(request, template_name, context)


@login_required
def results(request):
    template_name = 'core/users.html'
    query = request.GET.get('q')
    result = Journal.objects.filter(content__icontains=query)
    results = Profile.objects.filter(Q(passion__icontains=query) | Q(plan__icontains=query))
    context = {
        "result":result,
        "results":results
    }
    return render(request, template_name, context)

def search_profile(request):
    template_name='core/search_profile.html'
    results = Profile.objects.all()
    jn = Journal.objects.filter(user=request.user).order_by('-timestamp')
    context = { 'results':results }
    return render(request, template_name, context )

def notifications(request):
    template_name = 'core/notifications.html'
    context = {}
    return render(request, template_name, context)