from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('create_blog/', views.create_blog),
    path('save_contact', views.save_contact),
    path('search', views.search),
    path('signup', views.handleSingup),
    path('login', views.handlelogin),
    path('logout', views.handlelogout),
    path('Profile_auther', views.Profile_auther),
    path('remove-contact/<int:id>',views.removecontact),
    path('list-contact',views.listcontact),
    path('edit-contact/<int:id>',views.editcontact),
    path('update-contact/<int:id>',views.updatecontact)



]
