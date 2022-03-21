
from django.shortcuts import redirect, render


from .models import Faq, Jobs, Notifications, Members

# Create your views here.
def home(request):
    return render(request,'index.html')

def notifications(request):
    notifications = Notifications.objects.all().order_by('-posted')
    return render(request,'notifications.html',{'notifications':notifications})

def add(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pwd = request.POST['pwd']
    cpwd = request.POST['cpwd']
    if fname.isalpha() and lname.isalpha() and pwd==cpwd:
        form = Members(fname=fname,lname=lname,email=email,pwd=pwd)
        form.save()
        return render(request,'login.html')
    else:
        return redirect('register')

def register(request):
    return render(request,'register.html')
def faq(request):
    faq = Faq.objects.all()
    return render(request,'faq.html',{'faq':faq})

def login(request):
    return render(request,'login.html')

def apply(request):
    jobs = Jobs.objects.all()
    return render(request,'apply.html',{'jobs':jobs})