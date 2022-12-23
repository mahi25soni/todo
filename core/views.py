from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate
from .forms import *
from datetime import date as me
from datetime import  timedelta
import json
from .utils import *
from django.contrib.auth.decorators import login_required


def LogIn(request):
    if request.method == 'POST':
        loginform = LoginForm(data = request.POST)
        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            reg = authenticate(request , username = username, password=password)
            if reg is not None:
                login(request, reg)
                return HttpResponseRedirect('/') 
    else:
        loginform = LoginForm()
    return render(request, 'core/login.html', {'form':loginform})

def SignUp(request):
    if request.method == 'POST':
        userform = MyUser(data = request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect('/login/')

    else:
        userform = MyUser()
    return render(request, 'core/signup.html', {'form':userform})

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url= '/login/')
def home(request):
    user = request.user
    if request.method == 'POST':

        showdateform = Showdate(data = request.POST, prefix="form1")
        shownoteform = Shownote(data = request.POST, prefix="form2")          

        if request.POST.get('form2-time') is None:
            if showdateform.is_valid():
                date = showdateform.cleaned_data['date']
                usernotes = getdata(user, date)        
                shownoteform = Shownote(prefix="form2")
                return render(request, 'core/home.html', {'showdateform':showdateform, 'shownoteform':shownoteform, 'notes':usernotes})
                        
        else:   
            if showdateform.is_valid() and shownoteform.is_valid():
                date = showdateform.cleaned_data['date']
                task = shownoteform.cleaned_data['task']
                time = shownoteform.cleaned_data['time']
                userdate = Userdate.objects.get_or_create(user = user, date = date)
                usernote = Usernote.objects.get_or_create(userdate = userdate[0], time = time, task = task)
                return HttpResponseRedirect('/')

    else:
        if user.is_authenticated:
            showdateform = Showdate(prefix="form1")
            shownoteform = Shownote(prefix="form2")
            usernotes = getdata(user, me.today())         
        else:
            return HttpResponseRedirect('/login/')               
        return render(request, 'core/home.html', {'showdateform':showdateform, 'shownoteform':shownoteform, 'notes':usernotes})
    return HttpResponseRedirect('/')  


def aboutask(request, pk):
    Jsonbody = json.loads(request.body)
    value = Jsonbody['value']
    if value == 'remove':
        usernote = Usernote.objects.get(id= pk)
        usernote.delete()
    else:      
        usernote = Usernote.objects.get(id= pk)
        usernote.isdone = True
        usernote.save()
    return HttpResponseRedirect('/')

@login_required(login_url= '/login/')     
def showstats(request):
    user = request.user
    i = 0
    c = 0
    if request.method == 'POST':
        Jsonbody = json.loads(request.body)
        value = Jsonbody['value']
        i = Jsonbody['week']

        todays_date = me.today()
        todays_month = me.today() 
        todays_year = me.today() 
        if (value == 'increase-week') or (value == 'decrease-week') :
            todays_date = me.today() + timedelta(weeks=i)
            c = i
        elif (value == 'increase-month') or  (value == 'decrease-month'):
            todays_month = me.today() + timedelta(weeks=i*4)
            c = i
        elif (value == 'increase-year') or (value == 'decrease-year'):
            todays_year = me.today() + timedelta(weeks=i*52)
            c = i
        answer = carryon(user,todays_date,todays_month,todays_year,c)
        request.session['datalist'] = answer
        return HttpResponseRedirect('/nothing/')

    todays_date = me.today()
    todays_month = me.today() 
    todays_year = me.today() 
    answer = carryon(user,todays_date,todays_month,todays_year,c)
    request.session['datalist'] = answer
    return HttpResponseRedirect('/nothing/')

@login_required(login_url= '/login/')     
def nothing(request):
    datalist =  request.session['datalist'] 
    return render(request, 'core/stats.html', {'context':datalist})




