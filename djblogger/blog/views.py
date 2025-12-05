from django.shortcuts import render, HttpResponse, redirect
from . models import Technical_Post, Technical_Exercise, Post, Database_Structure
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# def home(request):

#     data = {
#         'posts': Post.objects.all() 
#     }
#     return render(request, "home.html", data)

def technical_post(request):

    data = {
        'tech_post': Technical_Post.objects.all() 
    }
    return render(request, "home.html", data)
    
def technical_ex(request):
    
    data = {
        'posts' : Technical_Exercise.objects.all()
    }
    return render(request, "home.html", data)

def database_hand(request):

    data = {
        'posts': Database_Structure.objects.all()
    }
    return render(request, 'home.html', data)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts' #this is a key that we are going to use in the template
    ordering = ['-date_posted'] # '-' is for ascending order and descending order    
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"  # <app>/<model>_<view_type>.html

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Post
    template_name = 'post_form.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):   #not cleared!!!!!
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





    