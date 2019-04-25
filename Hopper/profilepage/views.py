from django.views import generic 
from django.views.generic import View
from .models import Profile, Hobby
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User




class HomeView(View):
    user_class = User
    template_name = 'profilepage/home.html' 

    def get(self, request):
        user = self.user_class(None)
        if user.is_authenticated:
            return render(request, self.template_name, {'user':user})
        else:
            return redirect('login')    


class IndexView(generic.ListView):
    '''
    Shows view of all profiles
    '''
    template_name = 'profilepage/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return Profile.objects.all()

class ProfileView(generic.DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profilepage/myinfo.html'

class ProfileCreate(CreateView):
    model = Profile
    fields = ['name', 'username', 'age', 'email', 'photo']

class EditProfile(UpdateView):
    model = Profile
    fields = ['name', 'username', 'age', 'email', 'photo']

class DeleteProfile(DeleteView):
    model = Profile
    success_url = reverse_lazy('index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'profilepage/sign-up.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    #registers user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'profilepage/login.html'

    #display login form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        
            #authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        
        return render(request, self.template_name, {'form':form})

class AddHobby(CreateView):
    model = Hobby
    fields = ['hobby', 'hobby_nature', 'is_favorite']


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')















