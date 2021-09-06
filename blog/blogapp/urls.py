from django.urls import path

from blogapp import views

urlpatterns=[
    path('register',views.register, name='register'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('add',views.add_blog,name='add_blog'),
    path('home',views.demo,name='demo'),
    path('detail/<int:blog_id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    

]