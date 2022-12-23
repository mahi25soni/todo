from datetime import  timedelta
from .forms import *
from datetime import date as me


def getdata(user, date):
    try:
        userdate = Userdate.objects.get(user = user, date = date)
        usernotes = userdate.usernote_set.all().order_by('time')
    except:
        userdate = {}
        usernotes = {}  
    return usernotes 

def carryon(user,todays_date,todays_month,todays_year,c):
    last_date = todays_date + timedelta(weeks=1)
    last_month = todays_month + timedelta(weeks=4)
    last_year = todays_year + timedelta(weeks=52)

    rangedata = [todays_date,last_date,todays_month,last_month,todays_year,last_year]
    datalist = []
    for some in range(0, len(rangedata),2):
        userdate = Userdate.objects.filter(user = user,date__range=[rangedata[some], rangedata[some+1]])
        ifdone  = 0
        notdone = 0
        for x in userdate:
            usernotes = x.usernote_set.all()
            for y in usernotes:
                if y.isdone == True:
                    ifdone += 1
                else:
                    notdone += 1
        
        dicti = {'ifdone':ifdone, 'notdone':notdone}
        datalist.append(dicti)
    datalist.append(c)
    return datalist

