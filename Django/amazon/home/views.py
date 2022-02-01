from django.shortcuts import render
from .models import MyRegister2
from django.shortcuts import redirect , HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here
from django.http import HttpResponse

def index(request,name):
   return HttpResponse(f'<h1>Welcome {name}</h1>')

def navbar(request):
   return render(request , 'nv.html')

def contactus(request):
   return render(request, 'contactus.html')

def about(request):
   return render(request, 'about.html')

def register(request):

   if(request.method == 'GET'):
     return render(request, 'register.html')
   else:
      MyRegister2.objects.create(userName=request.POST['userName'] , password2=request.POST['password2'] , email=request.POST['email'])
      User.objects.create_user(username=request.POST['userName'] , password=request.POST['password2'] ,email=request.POST['email'] , is_staff=True)
      return redirect(login)
def selectedusers(request):
    students =MyRegister2.objects.all()
    context={}
    context['student'] = students
    return render(request , 'student.html' , context)
def delete(request , id):
    MyRegister2.objects.filter(id=id).delete()
    students = MyRegister2.objects.all()
    context ={}
    context['student'] = students
    return render(request, 'student.html', context)
def search(request ):
    if request.method == 'GET':
        userName= request.GET.get('userName')
        students = MyRegister2.objects.filter(userName=userName)
        context = {}
        context['student'] = students
        return render(request, 'search.html', context)

def login(request):
   if(request.method == 'GET'):
      return render(request, 'Login.html')
   else:
      pass
def checklogin(request):
  if(request.method == 'POST'):
       #check Pass & UserName
      user= MyRegister2.objects.filter(userName=request.POST['userName'] , password2=request.POST['password2'])
      if(user is not None):
         # context={}
          #context['userName'].user[0].userName
          request.session['userName']=request.POST['userName']
          return HttpResponseRedirect('about')

          #return render(request, 'nv.html')
      else:
          return render(request, 'login.html')





