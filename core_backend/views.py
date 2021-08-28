from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, About_Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView


posts = [
    {
        'location': 'CHA',
        'address': '1055 S Wells Ave Reno, Nv 89502',
        'title': 'Stop 1',
        'suite': '#1',
        'account': 'QAW16232',
        'time': '05/26/2021, 16:39',

    },
    {

        'location': 'NNMC',
        'address': '2375 East Prater Way Sparks, Nv 89434',
        'title': 'Stop 2',
        'suite': '1st floor',
        'account': 'QAW16232',
        'time': '05/26/2021, 16:49',
        'date_posted': 'May 26, 2019'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'core_backend/home.html', context)

class PostLoginView(LoginView):
    template_name = 'core_backend/login_page.html'
    


class PostListView(ListView):
    model = Post
    template_name = 'core_backend/home.html'
    context_object_name = 'posts'
    ordering = [ '-date_posted' ]


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['courier','location' ,'address','suite', 'account_number', 'note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['courier','location' ,'address','suite', 'account_number', 'note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.courier:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.courier:
            return True
        return False

    

    


        
 


def about(request):
    context = {
        'posts': About_Post.objects.all()
    }
    return render (request, 'core_backend/about.html', context)

