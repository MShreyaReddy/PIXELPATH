from django.urls import path
from .views import photographer_register, photographers_list, photographer_detail,photographer_bookings,index,cuslogin,contact,about,photographer1
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('photographer_register/', photographer_register, name='photographer_register'),
    path('photographer_list', photographers_list, name='photographers_list'),
    path('photographer/<int:pk>/', photographer_detail, name='photographer_detail'),
    path('photographer/<int:pk>/bookings/', photographer_bookings, name='photographer_bookings'),
    path('contact', contact, name='contact'),
    path('about/', about, name='about'),
    path('photographer1',photographer1,name='photographer1'),
     path('photographers_list', views.photographers_list, name="photographers_list"),


]
