from django.shortcuts import render,redirect,HttpResponse
from .models import BlogPost
from .models import blogcomment
from django.contrib import messages

# Create your views here.

def Add_BlogPost(request):
    return render(request,"blog/Add_BlogPost.html")

def crt_post(request):

       createPost=BlogPost()
       createPost.title=request.POST['title']
       createPost.content=request.POST['content']
       createPost.author=request.POST['author']
       createPost.slug=request.POST['slug']
       createPost.timestamp=request.POST['timestamp']
       createPost.save()  
       return redirect("/blog/")

def blogHome(request):
    AllPost=BlogPost.objects.all()
    return render(request,"blog/blogHome.html",{'AllPost':AllPost})

def blogPost(request,id):
    post=BlogPost.objects.get(id=id)
    context={'post':post}
    return render(request,"blog/blogPost.html",context)


def Edit_Post(request,id):
    EditP=BlogPost.objects.get(id=id)
    return render(request,"blog/Edit_Post.html",{'EditP':EditP})

def Save_Edit_Post(request,id):
       Edit_Save_Post=BlogPost.objects.get(id=id)
       Edit_Save_Post.title=request.POST['title']
       Edit_Save_Post.content=request.POST['content']
       Edit_Save_Post.author=request.POST['author']
       Edit_Save_Post.slug=request.POST['slug']
       Edit_Save_Post.timestamp=request.POST['timestamp']
       Edit_Save_Post.save()  
       messages.success(request,"Your data hasbeen successfully saved...")
       return redirect("/blog/")
  

def Delete_Post(request,id):
    del_P=BlogPost.objects.get(id=id)
    del_P.delete()
    return redirect ("/blog/")

   
