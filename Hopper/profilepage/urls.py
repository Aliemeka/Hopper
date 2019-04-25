from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    #/profile/
    path('', views.HomeView.as_view(), name = 'home'),

    #/profile/view-profiles
    path('view-profiles/', views.IndexView.as_view(), name = 'index'),

    #/profile/<profile_id>/
    path('<int:pk>/', views.ProfileView.as_view(), name='userprofile'),
    
    #/profile/add-profile/
    path('add-profile/', views.ProfileCreate.as_view(), name='profile-add'),

    #/profile/<profile-id>/edit/
    path('<int:pk>/edit/', views.EditProfile.as_view(), name='profile-edit'),
    
    #/profile/<profile-id>/delete/
    path('<int:pk>/delete/', views.DeleteProfile.as_view(), name='profile-delete'),

    #/profile/sign-up
    path('sign-up/', views.UserFormView.as_view(), name = 'register'),
    
    #/profile/login/
    path('login/', views.LoginFormView.as_view(), name = 'login'),

    #/profile/logout/
    path('logout/', views.LogoutView.as_view(), name = 'logout'),

    ##/profile/<profile-id>/addhobby
    path('<int:pk>/addhobby/', views.AddHobby.as_view(), name='add-hobby'),
    
    #/prrofile/13/
    #url(r'^(?P<hobby_id>[0-9])$', views.hobbydetial, name="hobbydetial"),
     
] 