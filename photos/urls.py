from django.urls import path
from . import views

urlpatterns = [

 #-Home page

    path('', views.home, name ="home"),

#- Login
    path('login/', views.loginUser, name="login"),

#- Logout
    path('logout/', views.logoutUser, name="logout"),

#- Register
    path('register/', views.registerUser, name="register"),

#- Gallery
    path('gallery/', views.gallery, name='gallery'),

#- View photos
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),

    
#- Edit description    
    path('photo/<int:photo_id>/update_description/', views.update_description, name='update_description'),


#- Add photo
    path('add/', views.addPhoto, name='add'),

#- Delete photo
    path('delete/<str:pk>/', views.deletePhoto, name = 'delete'),

#- Delete category
   path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    
   
]
