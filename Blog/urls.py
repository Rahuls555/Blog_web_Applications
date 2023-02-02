from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.blogHome),
    path('Add_BlogPost', views.Add_BlogPost),
    path('<int:id>', views.blogPost),
    path('crt_post', views.crt_post),
    path('Edit_Post/<int:id>', views.Edit_Post),
    path('Save_Edit_Post/<int:id>', views.Save_Edit_Post),
    path('Delete_Post/<int:id>', views.Delete_Post),

    # path('postComment', views.postComment),
    
]