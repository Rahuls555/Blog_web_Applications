from email import message
from django.shortcuts import redirect, render,HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):

    AllPost=BlogPost.objects.all()
    return render(request,"home/home.html",{'AllPost':AllPost})

def contact(request):
    return render(request,"home/contact.html")

# Save contact data in database.
def save_contact(request):
    contact=Contact()
    contact.name=request.POST['name']
    contact.email=request.POST['email']
    contact.phone=request.POST['phone']
    contact.massage=request.POST['massage']
    contact.save()  
    messages.success(request,"Data successfully saved..")  
    return redirect ("/contact")

def about(request):
    return render(request,"home/about.html")

def create_blog(request):
    return redirect("/login")

# Search query.
def search(request):
    query=request.GET['query']
    if len(query)>75:
       allPost = BlogPost.objects.none()
    else:
       allPostTitle=BlogPost.objects.filter(title__icontains=query)
       allPostContent = BlogPost.objects.filter(content__icontains=query)
       allPostAuthor = BlogPost.objects.filter(author__icontains=query)
       allPost = allPostTitle.union(allPostContent)
       allPost = allPostTitle.union(allPostAuthor)
       
    if allPost.count() == 0:
        messages.warning(request,"No search results found. Please refine your query")
        
    rahul={'allPost':allPost, 'query':query}
       # allPost=Post.objects.all()
    return render(request,"home/search.html",rahul)
 

    #signup data save query.
def handleSingup(request):
    if request.method == 'POST':
        #get the all parameters
        username = request.POST['username']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #checks for errorneous input
        if len(username)>10:
           messages.error(request,"username must be under 10 characters")
           return redirect("/")
       
        #checks for special character
        if not username.isalnum():
           messages.error(request,"username should only contain letters and numbers")
           return redirect("/")
        
        #checks for password match or not
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            return redirect("/")        

        #create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been successfully created")
        return redirect("/") 
    else:
        return HttpResponse('404 - Not Found')
    
    #Login data query.
def handlelogin(request):
    if request.method == 'POST':
        #get the all parameters
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        
        user= authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalide ctredentials, Please try again")
            return redirect('/')  
    
    else:
      return HttpResponse('404 - Not Found')   
        
    #Logout data query.
def handlelogout(request):
    logout(request)
    messages.success(request,"successfully Logged Out")
    return redirect('/')


def Profile_auther(request):
    return render(request,"home/about.html")


def listcontact(request):
    lst=Contact.objects.all()
    return render(request,"home/contact-list.html",{'lst':lst})


def removecontact(request,id):
    rmv=Contact.objects.get(id=id)
    rmv.delete()
    messages.success(request,"Data successfully Removed..")
    return redirect("/list-contact")

def editcontact(request,id):
    edt=Contact.objects.get(id=id)
    return render(request,"home/contact-update-form.html",{'edt':edt})

def updatecontact(request,id):
    updt=Contact.objects.get(id=id)
    updt.name=request.POST['name']
    updt.email=request.POST['email']
    updt.phone=request.POST['phone']
    updt.massage=request.POST['massage']
    updt.save()
    messages.success(request,"Data successfully Updated..")
    return redirect("/list-contact")