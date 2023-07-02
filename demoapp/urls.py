from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('userhome',views.userhome,name='userhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userprofileview',views.userprofileview,name='userprofileview'),
    path('profileupdate/<int:id>/',views.profileupdate, name='profileupdate'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('updateproduct/<int:id>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('userviewproduct',views.userviewproduct,name='userviewproduct'),

    ]